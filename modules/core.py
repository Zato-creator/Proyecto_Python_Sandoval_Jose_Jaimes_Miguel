import os
import json

# persistencia de datos

MI_BASE_DE_DATOS = None   # Base de datos Vacia 

def NewFile(data):
    with open(MI_BASE_DE_DATOS, "w") as wf:
        json.dump(data, wf, indent=4) # Corregido indent

def ReadFile():
    with open(MI_BASE_DE_DATOS, "r") as rf:
        return json.load(rf)

def CheckFile(*param): # Verificar archivo json
    data = list(param)
    # CORRECCIÓN: Se elimina el "r", isfile solo recibe la ruta
    if os.path.isfile(MI_BASE_DE_DATOS): # Si ya existe lo lee
        if(len(param)):
            data[0].update(ReadFile())
    else: # Si no existe lo crea
        if(len(param)):
            NewFile(data[0])

def AddData(origin): # Guardar informacion en el archivo json
    with open(MI_BASE_DE_DATOS, "w") as rwf:
        json.dump(origin, rwf, indent=4)