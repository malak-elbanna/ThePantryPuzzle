import sqlite3
import json


connection = sqlite3.connect("instance/MainDB.db")
cursor = connection.cursor()
table = 'create table Ingredient(Ingredient_name varchar(255))'
drop_table = 'drop table Ingredient'
table_nutrients = 'create table Nutrients(Ingredient_name varchar(255), Nutrients varchar(255))'
drop_table_nutrients = 'drop table Nutrients'

#cursor.execute(table)

def find_ingredient(path):
    try:
        with open(path, "r") as infile:
            data = json.load(infile)
            ingredient_names = [ingredient.get("Ingredient Name: ") for ingredient in data]
            return ingredient_names
    except FileNotFoundError:
        return f"File not found: {path}"
    except json.JSONDecodeError:
        return f"Error decoding json in file: {path}"



def add_from_json_file(path):
    results = find_ingredient(path)
    for result in results:
        if result is not None:
            cursor.execute('insert into Ingredient values (?)', (result,))


def remove_duplicates_from_json(input_file, output_file):
    with open(input_file, 'r') as infile:
        data = json.load(infile)
    unique_data = [dict(tuple_item) for tuple_item in set(tuple(sorted(item.items())) for item in data)]
    with open(output_file, 'w') as outfile:
        json.dump(unique_data, outfile, indent=2)
  

def combine_json_files(file1, file2, file3, output_file):
    with open(file1, 'r') as infile1:
        data_1 = json.load(infile1)
    with open(file2, 'r') as infile2:
        data_2 = json.load(infile2)
    with open(file3, 'r') as infile3:
        data_3 = json.load(infile3)
    data_combined = data_1 + data_2 + data_3
    with open(output_file, 'w') as outfile:
        json.dump(data_combined, outfile, indent=2)


data = cursor.execute('select * from Ingredient') 
# then print the ingredients
for row in data:
    print(row)
#add_from_json_file('json files\\all_ingredients_unique.json')


connection.commit()
connection.close()
print("done")
