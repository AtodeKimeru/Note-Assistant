import mysql.connector


# conexión
database = mysql.connector.connect(
    host="localhost",
    user = 'root',
    passwd = '',
    database = 'master_python',
    )


cursor = database.cursor(buffered=True)

# crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)

# crear tablas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehiculos(
        id int(10) auto_increment not null,
        marca varchar(40) not null,
        modelo varchar(40) not null,
        precio float(10,2) not null,
        CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    )
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)


# insertar datos

# cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")

autos = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000),
    ('Ford', 'Focus', 5000),
]

# cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", autos)


cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'")

result = cursor.fetchall() 

print("----- todos los autos -----")   
for auto in result:
    print(auto[0], auto[1])

cursor.execute("SELECT * FROM vehiculos")
auto = cursor.fetchone()
print(auto)

# borrar registros

cursor.execute("DELETE FROM vehiculos WHERE marca = 'Citroen'")

print(cursor.rowcount, "borrados!!")

# actualizar registros
cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca = 'Mercedes'")
database.commit()
print(cursor.rowcount, "actulizado!!")

