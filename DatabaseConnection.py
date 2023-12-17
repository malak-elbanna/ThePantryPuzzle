import sqlite3
import json
import pdb

connection = sqlite3.connect("RecipesDB")                                  #add the database name as it is saved on ur laptop
cursor = connection.cursor() 
with open('ThePantryPuzzle\egetables_queryIngredients.json', 'r') as json_file:     #add ur own json file path
    file = json.load(json_file)

# to insert into the recipes table using the json file
def insert_recipes_intotable(file):                                  
    for recipe in file:
        templist=file[recipe]
        for ingredientt in templist: 
            connection.execute("insert into Recipes (Recipe_name, Ingredient) VALUES (?, ?)", (str(recipe),str(ingredientt)))
            connection.commit()
# use when testing whether the database got the data or not::
cursor.execute("select * from Recipes")       
mydata=cursor.fetchall()                   #fetch all function gets whats stored in the database
for i in mydata:             
    print(i)

# def get_recipeInfo(RecipeN):
#         cursor.execute("Select Ingredient from Recipes where Recipe_name = ?", ([RecipeN]))
#         ingredients=cursor.fetchall()
#         return ingredients

# ingredientss=get_recipeInfo("Meat Loaf")    #choose the recipe that u want to get the ingredients for
# for ingredient in ingredientss:
#     print(ingredient)

connection.close()

