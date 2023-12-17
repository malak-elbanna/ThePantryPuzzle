import sqlite3
connection = sqlite3.connect("ThePantryPuzzle\instance\RecipesDB.db")                                 
cursor = connection.cursor()


def Ltuple_toList(tuplee):                       #function to change a list of tuples to a normal list
    List=[]
    for item in tuplee:
        for itemm in item:
            List.append(itemm)        # all the ingredients are now in a normal list
    return List

def get_recipeInfo(RecipeN):
        cursor.execute("Select Ingredient from Recipes where Recipe_name = ?", ([RecipeN]))
        ingredients=cursor.fetchall()
        return ingredients

cursor.execute("Select Distinct Ingredient from Recipes")
ingredientListofTuples=cursor.fetchall()                 #the database returns a list of tuples.
IngredientsList=Ltuple_toList(ingredientListofTuples)

RecipesandIngredientsDict={}

cursor.execute("Select Distinct Recipe_name from Recipes")
recipeT=cursor.fetchall()           #recipe list of tuples
recipeL=Ltuple_toList(recipeT)      #list of recipe names

# dictionary containing the recipe name and all its ingredients in a list
for recipe in recipeL:
    ingredientsT=get_recipeInfo(recipe)
    ingredientsL=Ltuple_toList(ingredientsT)
    RecipesandIngredientsDict[recipe]=ingredientsL    

class pantry():
    def __init__(self):
        self.PantryList=[]

    def AddIngredient_toPantry(self,ingredientt):
        for ingred1 in IngredientsList:
            if ingredientt==ingred1:
                self.PantryList.append(ingredientt)
        # if ingredientt not in IngredientsList:
        #     print("Sorry, We don't have enough info about this ingredient")       # no need for this, might switch it up to something else later

    def RemoveIngredient_fromPantry(self,ingred):
        for ingred2 in self.PantryList:
            if ingred==ingred2:
                self.PantryList.remove(ingred)

    def DisplayPantry(self):
        for i in self.PantryList:
            print(i)

    def RecommendARecipe(self):
        recommendedrecipes=[]
        for key in RecipesandIngredientsDict:
            available=[]
            navailable=[]
            for ingre1 in RecipesandIngredientsDict[key]:
                    for ingre2 in self.PantryList:
                        if ingre1==ingre2:
                            available.append(ingre1)    
                    if ingre1 not in self.PantryList:
                        navailable.append(ingre1)
            if len(available)==len(RecipesandIngredientsDict[key]) :       #if all the ingredients are available in the pantry
                recommendedrecipes.append(key)
            if len(RecipesandIngredientsDict[key])>=3:                     #if all are available except for one or two ingredients
                if 0<len(navailable)<=2:
                    recommendedrecipes.append(key)
        return recommendedrecipes

mypantry=pantry()
temp=["fruit cocktail","walnuts","fat-free milk","pound cake","Salt","Kosher salt","olive oil","garlic","carrots","dried oregano","dried basil","vegetables","honey"
    "unsalted butter","sugar","rice vinegar"]
for i in temp:
    mypantry.AddIngredient_toPantry(i)
print(mypantry.RecommendARecipe())





