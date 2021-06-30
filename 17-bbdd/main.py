import mysql.connector

# Connect to BBDD
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="master_python"
)
print(database)
cursor = database.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
# CREATE TABLE
cursor.execute("CREATE TABLE IF NOT EXISTS vehiculos ("
               "id int(10) auto_increment not null, "
               "marca varchar(40) not null, "
               "modelo varchar(40) not null, "
               "precio float(10,2) not null,"
               "CONSTRAINT pk_id PRIMARY KEY(id))")

# cursor.execute("INSERT INTO vehiculos VALUES(null,'Opel','Astra',150000)")
cursor.execute("SELECT * FROM vehiculos")
results = cursor.fetchall()
for car in results:
    print(car)