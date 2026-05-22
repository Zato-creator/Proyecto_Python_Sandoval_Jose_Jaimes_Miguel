import os



def borrar_pantalla():
    os.system("cls")

    

def pausar_pantalla():
    os.system("pause")



def pedir_texto_obligatorio(mensaje):
    """Solo valida que el campo no se vaya en blanco. Acepta letras, números y espacios."""
    while True:
        valor = input(mensaje).strip()
        
        if valor == "":
            print("Error: Este campo no puede estar vacío.")
        else:
            return valor

def pedir_numero_obligatorio(mensaje):
    """Pide un número, valida que no esté vacío y que solo contenga dígitos."""
    while True:
        valor = input(mensaje).strip()
        
        if valor == "":
            print("Error: Este campo no puede estar vacío.")
        elif not valor.isdigit(): # .isdigit() revisa si todo el string son números
            print("Error: Valor incorrecto. Solo debes ingresar números. Inténtalo de nuevo.")
        else:
            return valor
        
def pedir_rol(mensaje):
    """Pide el rol del usuario y valida que sea estrictamente admin u operario."""
    while True:
        # Aquí usamos el parámetro 'mensaje' que viene de crud_contacts.py
        rol = ut.pedir_texto_obligatorio(mensaje).lower() 
        
        if rol in ["admin", "operario"]:
            return rol
        else:
            print(" Error: El rol solo puede ser 'admin' u 'operario'.")