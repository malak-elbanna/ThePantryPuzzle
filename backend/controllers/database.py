import sqlite3
from math import floor
import base64
class database_base_model:
    def __init__(self, database_name):
        self.database_name = database_name
    def l_tuple_to_list(self,tuplee):                       #function to change a list of tuples to a normal list
        listt =[]
        for item in tuplee:
            for itemm in item:
                listt.append(itemm)        # all the ingredients are now in a normal list
        return listt    
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
        query = f"Select * from User where id = '{user_id}'"
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

    def is_chef(self,id):
        cursor=self.cursor().execute("select count(*) from User where id = ? and isChef = 'on' ",(str(id),))
        count=cursor.fetchall()
        countt=self.l_tuple_to_list(count)
        if countt[0]>0:
            return True
        else:
            return False
    
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
        cursor=self.cursor().execute("Select distinct Quantity from Quantities where Recipe_name = ?", ([recipe_n]))
        ingredients=cursor.fetchall()
        ingredients=self.l_tuple_to_list(ingredients) 
        cursor.close()
        return ingredients
    def get_recipe_ingredients(self,recipe_n):
        cursor=self.cursor().execute("Select distinct Ingredient from Recipes where Recipe_name = ?", ([recipe_n]))
        ingredients=cursor.fetchall()
        ingredients=self.l_tuple_to_list(ingredients) 
        cursor.close()
        return ingredients
    def recipe_ingredient_dictt(self):
        recipes_and_ingredients_dictt={}
        recipe_l=self.return_all_recipe_names()
        for recipe in recipe_l:
            ingredients_l=self.get_recipe_ingredients(recipe)
            recipes_and_ingredients_dictt[recipe]=ingredients_l
        return recipes_and_ingredients_dictt
    
    def recommend_recipes(self,user_id):
        recommendedrecipes = []
        dictt=self.recipe_ingredient_dictt()
        for key in dictt:
            available=[]
            for ingre1 in dictt[key]:
                    for ingre2 in self.display_pantry(user_id):
                        if ingre1==ingre2:
                            available.append(ingre1)
            if len(available)>0: 
                recommendedrecipes.append(key)                               #if all the ingredients are available in the pantry
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
        if ingredient in all_ingredients and ingredient not in users_pantry:
            self.cursor().execute("insert into Userspantry(User_id, ingredient) values(?,?)",((user_id),(ingredient)))
            self.commit()
    def remove_from_pantry(self,user_id,ingredient):
        users_pantry=self.display_pantry(user_id)
        if ingredient in users_pantry:
            self.cursor().execute("delete from Userspantry where User_id = ? and ingredient = ?",(user_id,ingredient))
            self.commit()
    def get_recipe_image(self, recipe_name):
        image_data = self.cursor().execute("select Recipe_Image from Recipe_Images where Recipe_Name = ?", (recipe_name,)).fetchone()
        return image_data
    def get_recipe_directions(self,recipe_n):
        cursor=self.cursor().execute("Select distinct Instruction from Instructions where Recipe_name = ?", ([recipe_n]))
        ingredients=cursor.fetchall()
        ingredients=self.l_tuple_to_list(ingredients) 
        cursor.close()
        return ingredients
class chef_database(database_base_model):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.establish_connection()
    def add_recipe_name(self,id,recipe):
        self.cursor().execute("insert into Instructions (Recipe_name) VALUES (?)", (str(recipe),))
        self.commit()
        self.cursor().execute("insert into Quantities (Recipe_name) VALUES(?)",(str(recipe),))
        self.commit()
        self.cursor().execute("insert into Chef (id, recipe_name) VALUES(?,?)", (str(id), str(recipe)) )
        self.commit()
        self.cursor().execute("insert into Recipes (Recipe_name) VALUES(?)", (str(recipe),))
        self.commit()
        self.cursor().execute("insert into Recipe_Images (Recipe_Name) VALUES(?)", (str(recipe),))
        self.commit()
    def add_recipe_quantites(self,recipe_name,quantities):
        self.cursor().execute("update Quantities set Quantity=? where Recipe_name=? ",(str(quantities), str(recipe_name)))
        self.commit()
    def add_recipe_instructions(self,recipe_name,instructions):
        self.cursor().execute("update Instructions set Instruction =? where Recipe_name=? ",(str(instructions), str(recipe_name)))
        self.commit()
    def add_picture(self, recipe_name,pic):
        self.cursor().execute("update Chef set recipe_image = ? where recipe_name =?",((pic), str(recipe_name)))
        self.commit()
        self.cursor().execute("update Recipe_Images set Recipe_Image =? where Recipe_Name=?", ((pic), str(recipe_name)))
        self.commit()
    def get_chef_id(self, recipe_name):
        result = self.cursor().execute("SELECT id FROM Chef WHERE recipe_name = ?", (recipe_name,))
        chef_id = result.fetchall()
        if chef_id:
            return chef_id[0][0]
        else:
            return None
    def get_chef_rating(self, chefid):
        result = self.cursor().execute("SELECT Rating, rNum FROM User WHERE id = ?", (chefid,))
        data = result.fetchone()

        if data is not None:
            Rating, number = data
            if number != 0:
                return floor(Rating / number)
            else:
                return 0
        else:
            return None

    def add_Rating(self, chefid, rating_to_add):
        result = self.cursor().execute("SELECT Rating, rNum FROM User WHERE id = ?", (chefid,))
        chef_data = result.fetchone()

        if chef_data is None:
            result = self.cursor().execute("INSERT INTO User (id, Rating, rNum) VALUES (?, ?, ?)", (chefid, rating_to_add, 1))
        else:
            current_rating, rNum = chef_data

            if current_rating is not None and rNum is not None:
                new_rating = current_rating + rating_to_add
                new_rNum = rNum + 1
            else:
                new_rating = rating_to_add
                new_rNum = 1

            result = self.cursor().execute("UPDATE User SET Rating = ?, rNum = ? WHERE id = ?", (new_rating, new_rNum, chefid))
        self.commit()
        return

        
    def get_recipes(self, chef_id):
        query = "select recipe_name from Chef where id = ?"
        data = self.cursor().execute(query, (chef_id,)).fetchall()
        recipes_list = []
        for recipe in data:
            recipes_list.append(recipe[0])
        return recipes_list


#fetch all function gets whats stored in the database

class reviews_database(database_base_model):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.establish_connection()
    
    def add_review(self, user_id, review, recipe_name):
        query = "insert into Reviews values (?, ?, ?)"
        try:
            self.cursor().execute(query, (user_id, review, recipe_name))
            self.commit()
        except Exception as e:
            print(f"Error adding review: {e}")
    
    def remove_review(self, user_id, recipe_name):
        query = "delete from Reviews where User_ID = ? and Recipe_Name = ?"
        try:
            self.cursor().execute(query, (user_id, recipe_name))
        except Exception as e:
            print(f"error removing reviews: {e}")
    
    def display_review(self, recipe_name):
        query = "select User_ID, comment from Reviews where Recipe_Name = ?"
        data = self.cursor().execute(query, (recipe_name,)).fetchall()
        tempobject=user_database("instance/MainDB.db")
        finaltuple=()
        listfadya=[]
        for items in data:
            temp = tempobject.get_user(items[0])
            if temp:
                finaltuple = (temp[3], items[1])
                listfadya.append(finaltuple)
        return listfadya
        

    def edit_review(self, user_id, recipe_name, new_review):
        query = "update Reviews set comment = ? where User_ID = ? and Recipe_Name = ?"
        try:
            self.cursor().execute(query, (new_review, user_id, recipe_name))
        except Exception as e:
            print(f"error editing review: {e}")
    
    def connection_close(self):
        self.close()

class dietary_prefernces_database(database_base_model):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.establish_connection()
    
    def get_recipes_dietary(self, preference):
        query = "select Recipe_Name from Dietary where preference = ?"
        data = self.cursor().execute(query, (preference,)).fetchall()
        recipes_preferences = []
        for recipe in data:
            recipes_preferences.append(recipe[0])
        return recipes_preferences
    
    def connection_close(self):
        self.close()
