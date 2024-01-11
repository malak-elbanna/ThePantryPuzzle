import sqlite3

create_table = """
    create table Reviews(
        User_ID varchar(50),
        comment varchar(255),
        Recipe_Name varchar(50)
    )
"""
drop_table = "drop table Reviews"

add_recipe = "alter table Reviews add Recipe_Name varchar(50)"
connection = sqlite3.Connection("instance/MainDB.db")
cursor = connection.cursor()

cursor.execute(create_table)
connection.commit()
connection.close()
