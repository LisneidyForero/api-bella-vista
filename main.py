from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API Bella Vista funcionando"}

@app.get("/salud")
def salud():
    return {"estado": "ok"}

@app.get("/productos")
def productos():
    return [
        {"id": 1, "nombre": "Cuaderno Bella Vista", "precio": 12000},
        {"id": 2, "nombre": "Camiseta Bella Vista", "precio": 35000},
        {"id": 3, "nombre": "Mochila Bella Vista", "precio": 65000},
    ]
