import pymongo
from prettytable import PrettyTable

# Conectar a MongoDB
cliente = pymongo.MongoClient("mongodb://root:root@127.0.0.1:27017/")
db = cliente["concesionario"]
coleccion = db["coches"]

# Formatear la tabla
tabla = PrettyTable()
tabla.field_names = ["ID", "Marca", "Modelo", "Color", "Kilometraje", "Precio"]

for coche in coleccion.find():
    tabla.add_row([coche["id"], coche["marca"], coche["modelo"], coche["color"], coche["km"], coche["precio"]])

print("=== DATOS DESDE MONGODB ===")
print(tabla)
