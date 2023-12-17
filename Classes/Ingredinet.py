import sqlite3
import json

class Ingredients:
    def get_ingredient_from_database(self, database_name):
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        data = cursor.execute('select * from Ingredient where Ingredient_name is not null') 
        ingredient_list = []
        # then print the ingredients
        for row in data:
            ingredient_list.append(row)
        connection.commit()
        connection.close()
        return ingredient_list

    def delete_ingredient(self, connection, ingredient_name):
        cursor = connection.cursor()
        cursor.execute('delete from Ingredient where Ingredient_name = ?', (ingredient_name))
        connection.commit()

    def fetch_nutrients_from_database(self, database_name, ingredient_name):
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        cursor.execute('select Nutrients from Nutrients where Ingredient_name = ?', (ingredient_name,))
        data = cursor.fetchone()
        connection.commit()
        connection.close()
        return data

    def display_nutrients(self, ingredient_name, database_name):
        ingredient_list = self.get_ingredient_from_database(database_name)
        for tuple_ingredient in ingredient_list:
            for ingredient in tuple_ingredient:
                if ingredient == ingredient_name:
                    nutrient_data = self.fetch_nutrients_from_database(database_name, ingredient)
        return nutrient_data[0]


ingredient_object = Ingredients()
database_name = "C:\\Users\\salma\\Ingredients.db"
print(ingredient_object.display_nutrients("garlic", database_name))
print("done")
