import modules.core as cr
import modules.utils as ut


def registrar (lista_contactos): # esta funcion resgistra o crea al usuario o empleado que vamos a registrar en la lista
    ut.borrar_pantalla()

    print("Registrar contacto usuarios administradores")
    
    num_identificacion = ut.pedir_numero_obligatorio("Ingresa el numero de identificacion: ")
    nombre = ut.pedir_texto_obligatorio("Ingrese el nombre: ")
    apellido = ut.pedir_texto_obligatorio("Ingrese el apellido: ")
    telefono = ut.pedir_numero_obligatorio("Ingrese su numero celular/telefono: ")
    email = ut.pedir_texto_obligatorio("Ingresa el correo electronico: ")
    direccion = ut.pedir_texto_obligatorio("Ingresa la direccion de residencia actual: ")
    rol = ut.pedir_texto_obligatorio("Ingresa el rol (admin / operario):" )
    contrasena = ut.pedir_numero_obligatorio("Ingresa la contraseña, debe ser de facil recordación y de 4 caracteres numericos: ")

    contactos= {
        "id": num_identificacion,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "correo electrónico": email,  # este va a se|r predefinido como su usuario
        "direccion": direccion,
        "rol" : rol,
        "contraseña": contrasena
    }

    lista_contactos[nombre] = contactos #agregar el nuevo contacto a la lista de diccionarios.
    
    cr.AddData(lista_contactos)
    print("Contacto agregado exitosamente")
    print(f"Contacto agregado: {nombre} {apellido}, numero de identificacion: {num_identificacion}, numero de telefono: {telefono}, e-mail: {email}, direccion de residencia: {direccion}, su rol en la empresa: {rol} y su contraseña: {contraseña} ")
    ut.pausar_pantalla()

def consultar (lista_contactos): # muestra la lista de todos los contactos con su respectiva información 
    ut.borrar_pantalla()
    print("Lista de contactos")
    for i, (nombre, contacto) in enumerate(lista_contactos.items()):
        print(f"{i+1}. {nombre} {contacto["apellido"]} - {contacto["telefono"]} - {contacto["email"]} - {contacto["direccion"]} - {contacto["rol"]} - {contacto["contrasena"]}")

    
def buscar (lista_contactos):
    ut.borrar_pantalla()
    print("Buscar contacto")
    nombre = input("Ingresa el nombre del contacto que deseas buscar: ").lower()
    if nombre in lista_contactos:
        contacto = lista_contactos[nombre]
        print(f"contacto encontrado: {nombre} {contacto["apellido"]} - {contacto["telefono"]} - {contacto["email"]} - {contacto["direccion"]} - {contacto["rol"]} - {contacto["contrasena"]} ") 
        ut.pausar_pantalla()
        return nombre
    else:
        print("Contacto no encontrado")
        ut.pausar_pantalla()

def actualizar (lista_contactos):
    nombre = buscar(lista_contactos)
    ut.borrar_pantalla()
    print("Actualizar contacto")
    num_identificacion = ut.pedir_numero_obligatorio("Ingresa el numero de identificacion: ")
    nombre = ut.pedir_texto_obligatorio("Ingrese el nombre: ")
    apellido = ut.pedir_texto_obligatorio("Ingrese el apellido: ")
    telefono = ut.pedir_numero_obligatorio("Ingrese su numero celular/telefono: ")
    email = input("Ingresa el correo electronico: ").lower()
    direccion=input("Ingresa la direccion de residencia actual: ").lower()
    rol = ut.pedir_rol("Ingresa el rol (admin / operario): ")
    contrasena = ut.pedir_numero_obligatorio("Ingresa la contraseña, debe ser de facil recordación y de 4 caracteres numericos: ")

    contacto = {
        "id": num_identificacion,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "correo electrónico": email,  # este va a se|r predefinido como su usuario
        "direccion": direccion,
        "rol" : rol,
        "contrasena": contrasena
    }

    lista_contactos[nombre] = contacto # Agrega el nuevo contacto al diccionario de la lista de contactos

    cr.AddData(lista_contactos)

    print("Contacto actualizado exitosamente.")


def eliminar_contacto (lista_contactos):
    ut.borrar_pantalla()
    print("Eliminar contacto")
    nombre = input("Ingrese el nombre del contacto que quiere eliminar: ").lower()

    if nombre in lista_contactos:
        lista_contactos.pop(nombre)
        print("contacto eliminado")
        cr.AddData(lista_contactos)
        ut.pausar_pantalla()
    else:
        print("El cojntacto no existe")
        ut.pausar_pantalla()
