import sqlite3
connection = sqlite3.connect("instance/MainDB.db")                                 
cursor = connection.cursor() 


# to insert into the recipes table using the json file
def insert_recipes_intotable(file):                                  
    for recipe in file:
        templist=file[recipe]
        for ingredientt in templist: 
            connection.execute("insert into Recipes (Recipe_name, Ingredient) VALUES (?, ?)", (str(recipe),str(ingredientt)))
            connection.commit()


def insert_instructions_intotable(file):
    for recipee in file:
        instructions=file[recipee]
        for instruction in instructions:
            connection.execute("insert into Instructions (Recipe_name, Instruction) VALUES (?,?)", (str(recipee), str(instruction)))
            connection.commit()

def insert_quantities_intotable(file):
    for line in file:
        quantities=file[line]
        for quantity in quantities:
            connection.execute("insert into Quantities (Recipe_name, Quantity) VALUES(?,?)",(str(line),str(quantity)))
            connection.commit()



connection.close()
