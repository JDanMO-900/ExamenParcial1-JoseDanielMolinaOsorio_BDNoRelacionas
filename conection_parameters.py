import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["cisc11c-v-prueba"]
collection = db["Peliculas"]


