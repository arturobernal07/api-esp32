from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime

app = FastAPI()

# REEMPLAZA ESTA LÍNEA con tu Connection String de MongoDB Atlas [cite: 26]
MONGO_URI = "mongodb+srv://esp32:<esp32pass>@cluster0.glsxy4d.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client.iot
collection = db.sensores

@app.get("/") 
def root():
    return {"mensaje":"API funcionando"}

@app.post("/sensor")
def guardar_sensor(data: dict):
    data["fecha"] = datetime.now()
    collection.insert_one(data) 
    return {"status":"dato guardado"}