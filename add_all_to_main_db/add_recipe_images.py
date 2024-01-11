import sqlite3

connection = sqlite3.connect("instance/MainDB.db")
cursor = connection.cursor()

table_query = "alter table Recipe_Images drop dietry_preference"
drop_table = "alter table Recipes drop column Recipe_Image"
new_table = """create table Recipe_Images(
        Recipe_Name varchar(50),
        Recipe_Image BLOB
)"""
cursor.execute(table_query)

connection.commit()
connection.close()


def convert_to_binary(filename):
    with open(filename, "rb") as file:
        blob_date = file.read()
    return blob_date

def insert_blob(recipe_name, image):
    try:
        connection = sqlite3.connect("instance/MainDB.db")
        cursor = connection.cursor()
        query = "insert into Recipe_Images values (?, ?)"
        recipe_img = convert_to_binary(image)
        cursor.execute(query, (recipe_name, recipe_img))
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("failed to insert blob data into sqlite table", error)
    finally:
        if connection:
            connection.close()

