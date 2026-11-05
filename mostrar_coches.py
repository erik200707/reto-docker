import json
import mysql.connector
from prettytable import PrettyTable

# Leer credenciales del JSON
with open('config.json', 'r') as file:
    config = json.load(file)

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host=config["host"],
    user=config["user"],
    password=config["password"],
    database=config["database"],
    port=config["port"]
)

cursor = conexion.cursor()
cursor.execute("SELECT id, marca, modelo, color, km, precio FROM coches")
coches = cursor.fetchall()

# Formatear la tabla
tabla = PrettyTable()
tabla.field_names = ["ID", "Marca", "Modelo", "Color", "Kilometraje", "Precio"]

for coche in coches:
    tabla.add_row(coche)

print(tabla)

cursor.close()
conexion.close()
