import sqlite3

connection = sqlite3.connect("instance/MainDB.db")
cursor = connection.cursor()
table_nutrients = 'create table Nutrients(Ingredient_name varchar(255), Nutrients varchar(255))'
#cursor.execute(table_nutrients)


data = cursor.execute('select * from Nutrients')
for row in data:
    print(row)

connection.commit()
connection.close()
print('done')
