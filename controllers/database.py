import sqlite3

class database_base_model:
    def l_tuple_to_list(self,tuplee):                       #function to change a list of tuples to a normal list
        listt =[]
        for item in tuplee:
            for itemm in item:
                listt.append(itemm)        # all the ingredients are now in a normal list
        return listt    
    def __init__(self, database_name):
        self.database_name = database_name
    def establish_connection(self):
        self.connection = sqlite3.connect(self.database_name, timeout = 5000)
    def cursor(self):
        return self.connection.cursor()
    def close(self):
        return self.connection.close()
    def commit(self):
        return self.connection.commit()

    def fetch_all(self, table_name):
        data = self.cursor().execute(f'select * from {table_name}')
        return data.fetchall()

class user_database(database_base_model):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.establish_connection()

    def create_user(self, user_id, email, password, first_name, last_name, is_chef):
        query = 'insert into User values (?, ?, ?, ?, ?, ?)'
        self.cursor().execute(query, (user_id, email, password, first_name, last_name, is_chef))

    def find_user(self, user_id):
        query = 'select * from User where id = ?'
        data = self.cursor().execute(query, (user_id,))
        if data.fetchone() is None:
            return False
        return True
    
    def get_user(self, user_id):
        query = f'Select * from User where id = {user_id}'
        cursor=self.cursor().execute(query)
        data=cursor.fetchall()                          
        data=self.l_tuple_to_list(data)                
        return data

    def delete_user(self, user_id):
        found = self.find_user(user_id)
        if found:
            query = 'delete from User where id = ?'
            self.cursor().execute(query, (user_id,))
            self.commit()
            return "User deleted"
        return "User not found"

    def change_password(self, user_id, new_password):
        query = 'update User set password = ? where id = ?'
        try:
            self.cursor().execute(query, (new_password, user_id))
            self.commit()
        except Exception as e:
            print(f"Error changing password: {e}")
            # Add additional logging or raise the exception if needed
        finally:
            self.close()
    
    def change_name(self, user_id, newfirstname, newlastname):
        query = 'update User set first_name = ?, last_name = ? where id = ?'
        try:
            self.cursor().execute(query, (newfirstname, newlastname, user_id))
            self.commit()
        except Exception as e:
            print(f"Error changing name: {e}")
        finally:
            self.close()

    def tuple_to_dict(self, user_tuple):
        user_info = user_tuple.fetchone()
        if user_info:
            dictionary = {
                "Id": user_info[0],
                "Email": user_info[1],
                "Password" :user_info[2],
                "First name" : user_info[3],
                "Last name" : user_info[4]
            }
            return dictionary
        else:
            return None
    
class favorite_recipe(database_base_model):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.establish_connection()

    def add_favorite_recipe(self, recipe_name, user_id):
        query = 'insert into Favorite values (?, ?)'
        try:
            self.cursor().execute(query, (user_id, recipe_name))
            self.commit()
        except Exception as e:
            print(f"Error adding favorite recipe: {e}")
        finally:
            self.close()

    
    # returns a list of the user's favorite recipe
    def display_favorite_recipe(self, id_user):
        query = 'select distinct Recipe_name from Favorite where id = ?'
        data = self.cursor().execute(query, (id_user,))
        list_recipes = []
        for recipe in data.fetchall():
            list_recipes.append(recipe[0])
        return list_recipes

    def remove_favorite_recipe(self, user_id, recipe_name):
        query = 'delete from Favorite where id = ? and Recipe_name = ?'
        try:
            self.cursor().execute(query, (user_id, recipe_name))
            self.commit()
        except Exception as e:
            print(f"Error removing favorite recipe: {e}")
            # Add additional logging or raise the exception if needed
        finally:
            self.close()


class shopping_list_database(database_base_model):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.establish_connection()
    
    def add_item(self, user_id, ingredient_name):
        query = 'insert into ShopList values (?, ?)'
        try:
            self.cursor().execute(query, (user_id, ingredient_name))
            self.commit()
        except Exception as e:
            print(f"Error adding shopping item: {e}")
    
    def display_shopping_list(self, user_id):
        query = 'select distinct * from ShopList where UserID = ?'
        data = self.cursor().execute(query, (user_id,))
        ingredients_tuple = data.fetchall()
        list_ingredients = []
        for ingredient in ingredients_tuple:
            list_ingredients.append(ingredient[1])
        return list_ingredients
    
    def remove_item(self, user_id, ingredient_name):
        query = 'delete from ShopList where UserID = ? and IngredientName = ?'
        try:
            self.cursor().execute(query, (user_id, ingredient_name))
            self.commit()
        except Exception as e:
            print(f"Error removing shopping item: {e}")
            # Add additional logging or raise the exception if needed

    def connection_close(self):
        self.close()

        
class pantry_database(database_base_model):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.establish_connection()

    def l_tuple_to_list(self,tuplee):                       #function to change a list of tuples to a normal list
        listt =[]
        for item in tuplee:
            for itemm in item:
                listt.append(itemm)        # all the ingredients are now in a normal list
        return listt
    
    def return_all_recipe_names(self):
        cursor=self.cursor().execute("Select Distinct Recipe_name from Recipes")
        recipe_t=cursor.fetchall()                            #recipe list of tuples
        recipe_l=self.l_tuple_to_list(recipe_t)                #list of recipe names
        cursor.close()
        return recipe_l
    
    def get_similar_recipes(self, recipename):
        cursor=self.cursor().execute("SELECT DISTINCT Recipe_name FROM Recipes WHERE Recipe_name LIKE ?", ('%' + recipename + '%',))
        recipe_t=cursor.fetchall()                          
        recipe_l=self.l_tuple_to_list(recipe_t)
        cursor.close()                
        return recipe_l
    
    def get_recipe_info(self,recipe_n):
        cursor=self.cursor().execute("Select distinct Ingredient from Recipes where Recipe_name = ?", ([recipe_n]))
        ingredients=cursor.fetchall()
        ingredients=self.l_tuple_to_list(ingredients) 
        cursor.close()
        return ingredients
    def recipe_ingredient_dict(self):
        recipes_and_ingredients_dict={}
        recipe_l=self.return_all_recipe_names()
        for recipe in recipe_l:
            ingredients_l=self.get_recipe_info(recipe)
            recipes_and_ingredients_dict[recipe]=ingredients_l
        return recipes_and_ingredients_dict
    def recommend_recipes(self,user_id):
        recommendedrecipes = []
        dict=self.recipe_ingredient_dict()
        for key in dict:
            available=[]
            for ingre1 in dict[key]:
                    for ingre2 in self.display_pantry(user_id):
                        if ingre1==ingre2:
                            available.append(ingre1)    
            if (len(dict[key])-len(available))<=3 :       #if all the ingredients are available in the pantry
                recommendedrecipes.append(key)
        return recommendedrecipes
    def ingredient_list(self):
        cursor=self.cursor().execute("Select Distinct Ingredient from Recipes")
        ingredient_list_of_tuples=cursor.fetchall()                 #the database returns a list of tuples.
        ingredients_list=self.l_tuple_to_list(ingredient_list_of_tuples)
        cursor.close()
        return ingredients_list
    def display_pantry(self,id):
        cursor=self.cursor().execute("Select distinct ingredient from Userspantry where User_id=?",(id,))
        ingredient_tuple=cursor.fetchall()
        users_ingredients=self.l_tuple_to_list(ingredient_tuple)
        return users_ingredients
    def insert_into_pantry(self,user_id,ingredient):
        all_ingredients= self.ingredient_list()
        users_pantry=self.display_pantry(user_id)
        if ingredient in all_ingredients:
            if ingredient not in users_pantry:
                self.cursor().execute("insert into Userspantry(User_id, ingredient) values(?,?)",(user_id,ingredient))
                self.commit()
    def remove_from_pantry(self,user_id,ingredient):
        users_pantry=self.display_pantry(user_id)
        if ingredient in users_pantry:
            self.cursor().execute("delete from Userspantry where User_id = ? and ingredient = ?",(user_id,ingredient))
            self.commit()
    def get_recipe_image(self, recipe_name):
        image_data = self.cursor().execute("select Recipe_Image from Recipe_Images where Recipe_Name = ?", (recipe_name,)).fetchone()
        print(image_data)
        return image_data

# database_connection = sqlite3.connect("D:\\SWE - project\\ThePantryPuzzle\\instance\\MainDB.db")
# cursor = database_connection.cursor()
# recipe_name = 'Meat Stock'
# image = cursor.execute("select Recipe_Image from Recipe_Images where Recipe_Name = ?", (recipe_name,)).fetchone()
# print(image[0])

# database_connection.commit()
# database_connection.close()