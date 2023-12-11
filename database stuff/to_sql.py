import sqlite3
import json 


def Get_ingredient(path, id):
    try:
        with open(path, "r") as infile:
            data = json.load(infile)
            for ingredient in data:
                if ingredient.get("Ingredient Id") == id:
                    return ingredient.get("ingredient")
            return f"No ingredient found with this id {id}"
    except FileNotFoundError:
        return f"File not found: {path}"
    except json.JSONecodeError:
        return f"Error decoding json in file: {path}"


def Delete_Ingredient(connection, id):
    cursor = connection.cursor()
    cursor.execute('delete from Ingredient where Ingredient_id = ?', (id))
    connection.commit()


connection = sqlite3.connect("Tasty.db")
cursor = connection.cursor()
# table = """create table Ingredient(Ingredient_id int, Ingredient_name varchar(255))"""
# cursor.execute(table)

path = "sample.json"
ingredient_id = 0

for i in range(152):
    result = Get_ingredient(path, ingredient_id)
    cursor.execute('insert into Ingredient values (?, ?)', (ingredient_id, result))
    ingredient_id += 1

print('done')
data = cursor.execute('select * from Ingredient')
for row in data:
    print(row)

connection.commit()
connection.close()

