import sqlite3
import json

connection = sqlite3.connect("instance/MainDB.db")
cursor = connection.cursor()
table = '''create table if not exists Chef (
                id INTEGER,
                recipe_name varchar(255),
                recipe_image blob,
                foreign key (id) references User(id)
            )'''
cursor.execute(table)
connection.commit()
connection.close()
