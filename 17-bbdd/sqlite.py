import sqlite3

# Connect
connection = sqlite3.connect('test.db')

# Cursor
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS products(" +
               "id integer primary key autoincrement, " +
               "title varchar(255), " +
               "description TEXT, " +
               "price int(255)" +
               ")"
               )
connection.commit()

# Insert data
cursor.execute("INSERT INTO products VALUES(null,'First product','The first product',10) ")
connection.commit()

# List data
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()
print(products)

# Close connection
connection.close()
