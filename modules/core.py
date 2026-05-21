import os
import json

# persistencia de datos

MI_BASE_DE_DATOS = None   # Base de datos Vacia 

def NewFile(*param): # Creamos un archivo en json
    with open(MI_BASE_DE_DATOS, "W") as wf:
        json.dump(param[0],wf,ident=4)


def  ReadFile():
    with open (MI_BASE_DE_DATOS, "r") as rf:
        return json.load(rf)

def CheckFile(*param): # Verificar archivo json
    data = list(param)
    if(os.path.isfile(MI_BASE_DE_DATOS)): # Si ya existe lo lee
        if(len(param)):
            data[0].update(ReadFile())
    else: # Si no existe lo crea
        if(len(param)):
            NewFile(data[0])

def AddData(origin): # Guardar informacion en el archivo json
    with open(MI_BASE_DE_DATOS,"w") as rwf:
        json.dump(origin,rwf,indent=4)