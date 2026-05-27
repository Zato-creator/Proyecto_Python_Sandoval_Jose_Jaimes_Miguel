import json
import re
import modules.utils as ut

def auditar_datos(data):
    ut.borrar_pantalla()
    print("Iniciando auditoría de datos...")
    
    # Estructura unificada con llaves consistentes (Resumen con R mayúscula y contactos con c minúscula)
    reporte = {
        "usuarios_con_errores": [],
        "contactos_con_errores": [],
        "Resumen": {
            "total_usuarios": 0,
            "total_contactos": 0,
            "usuarios_con_errores": 0,
            "contactos_con_errores": 0,
            "usuarios_con_email_duplicado": 0,
            "contactos_con_id_duplicado": 0
        }
    }
    
    # 1. Validar Usuarios
    usuarios = data.get("usuarios", [])
    reporte["Resumen"]["total_usuarios"] = len(usuarios)
    emails_vistos = set()
    
    for usuario in usuarios:
        errores = []
        user_id = usuario.get("id", "Desconocido")
        
        # Búsqueda adaptada a las llaves de agenda.json
        email = usuario.get("correo electronico", usuario.get("email", ""))
        password = usuario.get("contrasena", usuario.get("password", ""))
        
        campos_req = ["id", "nombres", "apellidos", "telefono", "direccion", "rol"]
        for campo in campos_req:
            if not usuario.get(campo):
                errores.append(f"Falta o está vacío el campo obligatorio: {campo}")
        
        if not email:
            errores.append("Falta o está vacío el campo obligatorio: email / correo electronico")
        if not password:
            errores.append("Falta o está vacío el campo obligatorio: password / contrasena")
        
        telefono = usuario.get("telefono", "")
        if telefono and not str(telefono).replace(" ", "").isdigit():
            errores.append("El telefono no es un número válido")
            
        if email:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                errores.append("El email no tiene un formato válido")
            if email in emails_vistos:
                errores.append("Email duplicado")
                reporte["Resumen"]["usuarios_con_email_duplicado"] += 1
            else:
                emails_vistos.add(email)
                
        rol = usuario.get("rol", "")
        if rol not in ["admin", "operario"]:
            errores.append(f"Rol inválido: {rol}")
            
        if errores:
            reporte["usuarios_con_errores"].append({
                "email/id": f"{email if email else 'SinEmail'} / {user_id}",
                "errores": errores
            })
            reporte["Resumen"]["usuarios_con_errores"] += 1

    # 2. Validar Contactos
    contactos_dict = data.get("contactos", {})
    contactos = list(contactos_dict.values())
    reporte["Resumen"]["total_contactos"] = len(contactos)
    ids_vistos = set()
    
    for contacto in contactos:
        errores = []
        contacto_id = contacto.get("id", "")
        
        nombre = contacto.get("nombre", contacto.get("nombres", ""))
        apellido = contacto.get("apellido", contacto.get("apellidos", ""))
        email_contacto = contacto.get("correo electronico", contacto.get("correo electrónico", ""))
        tipo_contacto = contacto.get("rol", contacto.get("tipo_contacto", "")) 
        telefono = contacto.get("telefono", "")
        
        if not contacto_id:
            errores.append("Falta o está vacío el campo obligatorio: id")
        if not nombre:
            errores.append("Falta o está vacío el campo obligatorio: nombres")
        if not apellido:
            errores.append("Falta o está vacío el campo obligatorio: apellidos")
        if not telefono:
            errores.append("Falta o está vacío el campo obligatorio: telefono")
        if not email_contacto:
            errores.append("Falta o está vacío el campo obligatorio: email")
            
        if telefono and not str(telefono).replace(" ", "").isdigit():
            errores.append("El telefono no es un número válido")
            
        if email_contacto and not re.match(r"[^@]+@[^@]+\.[^@]+", email_contacto):
            errores.append("El email no tiene un formato válido")
            
        if tipo_contacto and tipo_contacto not in ["cliente", "proveedor", "aliado", "personal", "operario", "admin"]:
            errores.append(f"Tipo de contacto inválido: {tipo_contacto}")
            
        if contacto_id:
            if contacto_id in ids_vistos:
                errores.append("ID duplicado")
                reporte["Resumen"]["contactos_con_id_duplicado"] += 1
            else:
                ids_vistos.add(contacto_id)
                
        if errores:
            reporte["contactos_con_errores"].append({
                "id": contacto_id if contacto_id else "Desconocido",
                "errores": errores
            })
            reporte["Resumen"]["contactos_con_errores"] += 1

    # 3. Generar archivo JSON de reporte
    try:
        with open("reporte_auditoria_datos.json", "w", encoding="utf-8") as file:
            json.dump(reporte, file, indent=4, ensure_ascii=False)
        print("\nAuditoría finalizada.")
        print("Se ha generado el archivo 'reporte_auditoria_datos.json' exitosamente con los resultados.")
    except Exception as e:
        print(f"\nError al guardar el reporte: {e}")
        
    ut.pausar_pantalla()