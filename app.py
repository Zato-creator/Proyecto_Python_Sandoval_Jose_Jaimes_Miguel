import modules.core as cr
import modules.utils as ut
import modules.contacts as ct
import modules.messages as ms

if __name__ == "__main__":

    origen = {} # Variable donde guardamos los contactos
    cr.MI_BASE_DE_DATOS = "Datos/agenda.json"# Ruta de ubicacion de la base de datros}
    cr.CheckFile(origen) #  Verifica si el archivo de la base de datros existe si no lo crea

    print("Bienvenido a la gestor de contactos ACME")
    print("========================================")
    print("Ingresa el usuario y contraseña")
    
    autenticado = False
    while not autenticado: # aca realizamos autenticacion de credenciales
        usuario = input("Digita el usuario (que es tu correo electronico): ").lower()
        contraseña = input("Digita la contraseña")
        credenciales_correctas = False 
        for llave, contacto in origen.items():
            if contacto.get("email") == usuario and contacto.get("contraseña") == contraseña:
                credenciales_correctas = True
                break
        
        if credenciales_correctas:
            print("Acceso permitido")
            ut.pausar_pantalla()
            autenticado = True
        else:
            print("Usuario o contraseña incorrectos. Intenta nuevamente.")
            ut.pausar_pantalla()
            ut.borrar_pantalla()
            print("Ingresa el usuario y contraseña")
            
                

    isActive = True

    while isActive:
        try:
            ut.borrar_pantalla()
            opcion = int(input(ms.menu_principal))  # ingresa la opcion del meú prinsipal

            match opcion: # seleccion de opciones del menú principal
                case 1: 
                    ct.registrar(origen)
                case 2:
                    ct.consultar(origen)
                case 3:
                    ct.buscar(origen)
                case 4:
                    ct.actualizar(origen)
                case 5:
                    ct.eliminar_contacto(origen)
                case 0: 
                    print("Gracias por usar el gestor de contactos. ¡Hasta la proxima!")
                    isActive = False
                case _:
                    print("Seleccion invalida. Intente nuevamente.")
                    ut.pausar_pantalla()
        except: 
            print("Error al ingresar el dato, debe ser un numero entero")
            ut.pausar_pantalla()
                
