# ------------------------------test the code after modifications---------------------------------------------------
import sqlite3
import json
from backend.controllers import database


my_database = database.database_base_model("instance/MainDB.db")
my_database.establish_connection()
cursor = my_database.cursor()

class Ingredients:
    def get_ingredient_from_database(self, cursor):
        data = cursor().execute('select * from Ingredient where Ingredient_name is not null') 
        ingredient_list = []
        # then print the ingredients
        for row in data:
            ingredient_list.append(row)
        return ingredient_list

    def delete_ingredient(self, cursor, ingredient_name):
        data = cursor().execute('select * from Ingredient where Ingredient_name = ?', (ingredient_name,))
        if data:
            cursor().execute('delete from Ingredient where Ingredient_name = ?', (ingredient_name,))
            return "Ingredient deleted"
        else:
            return "Ingredient not found"

    def fetch_nutrients_from_database(self, cursor, ingredient_name):
        cursor().execute('select Nutrients from Nutrients where Ingredient_name = ?', (ingredient_name,))
        data = cursor.fetchone()
        return data

    def display_nutrients(self, ingredient_name, cursor):
        ingredient_list = self.get_ingredient_from_database(cursor)
        for tuple_ingredient in ingredient_list:
            for ingredient in tuple_ingredient:
                if ingredient == ingredient_name:
                    nutrient_data = self.fetch_nutrients_from_database(database_name, ingredient)
                    return nutrient_data[0]
        return "Ingredient not found."


ingredient_object = Ingredients()
database_name = "C:\\Users\\salma\\Ingredients.db"
print(ingredient_object.display_nutrients("garlic", database_name))
print("done")
my_database.commit()
my_database.close()
