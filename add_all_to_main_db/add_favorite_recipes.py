import sqlite3

connection = sqlite3.connect("instance/MainDB.db")
cursor = connection.cursor()

table = '''
    create table Favorite(
        id int,
        Recipe_name varchar(255),
        foreign key (id) references User(id),
        foreign key (Recipe_name) references Recipes(Recipe_name)
    )
'''
drop_table = 'drop table Favorite'
cursor.execute(table)
connection.commit()
connection.close()
print('done')
