"""
Universidad Tecmilenio

Evidencia - Actividad 2
Nombre:    Gustavo Salvador Leal Dominguez
Matrícula: 7225668

Materia:   Fundamentos de Programación
Profesor:  Ing. Carlos A. Sánchez Rivera
Fecha:     22 de Octubre de 2025

Descripción: Realizarás un programa en Python para cobrar la entrada
             a un museo de tu ciudad, aplicando los descuentos establecidos.

Objetivo: Aplicar tus conocimientos sobre tablas de verdad, manejo de condiciones
          y uso apropiado de ciclos, con sus cláusulas break y continue,
          para crear un programa que cobre las entradas de un museo.

💡 El desarrollo de este algoritmo fue realizado bajo el conocimiento del curso de Cisco
   Fundamentos de Python 1 (CRN 1001 y 1036) y de la guia del Ingeniero Carlos A. Sánchez Rivera.
"""

# Bienvenida a los visitantes
print(
"""
+================================================+
|     ¡Bienvenidos al Museo de Antropología e    |
|                    Historia!                   |
+------------------------------------------------+
|               TABLA DE PRECIOS                 |
|------------------------------------------------|
| • Mayor de Edad (+18):         $45.00          |
| • Menor de Edad:               $30.00          |
| • Menores de 3 años:           GRATIS          |
|            (Precios incluyen IVA)              |
+------------------------------------------------+
|              TABLA DE DESCUENTOS               |
|------------------------------------------------|
|    Tipo de Visitante    |       Descuento      |
|-------------------------|----------------------|
| Adulto Mayor (+65)      |   12%                |
| Profesor                |   10%                |
| Estudiante              |   10%                |
+------------------------------------------------+
|           ¡Que Disfrutes tu Visita!            |
+================================================+
"""
)
#⚠ Las siguientes funciones fue la unica intervencio que tuvo ChatGPT, se pidio
#  ayuda para el try-except y para el if any(char.isdigit() for char in valor),
#  Se busca que el usuario no ingrese datos diferentes al solicitado.

#Funcion para validar que la persona siempre agrege numeros en lugar de texto
def pedir_entero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.strip() == "":  # si está vacío
            print("¡No puedes dejar este campo vacío! Intenta de nuevo.")
            continue
        try:
            return int(valor)
        except ValueError:
            print("¡Debes ingresar un número válido! Intenta de nuevo.")

#Funcion para validar que la persona siempre agrege text en lugar de numeros
def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()  # quitamos espacios al inicio y fin
        if valor == "":
            print("¡No puedes dejar este campo vacío! Intenta de nuevo.")
            continue
        if any(char.isdigit() for char in valor):
            print("¡No puedes ingresar números aquí! Intenta de nuevo.")
            continue
        return valor

#Declaracion de variables y listas
visitantes = []
persona_precio = [45.00,30.00,0]
nombre_descuentos = ["Estudiante", "Profesor", "Adulto Mayor", "Sin descuento"]
num_visitantes = 0
total_pagar = 0

print("¿Cuántas personas nos visitan hoy?")
num_visitantes = pedir_entero("Ingrese el número de visitantes: ")

#Validacion para el tipo de visitante
for i in range(num_visitantes):
    nombre = pedir_texto(f"\nIngresa el Nombre de la persona {i + 1}: ")
    edad = pedir_entero(f"Ingresa la Edad de {nombre}: ")
    if edad >= 65:
        print("Cuentas con una Identificacion de Adulto mayor?\n1 = Sí\n2 = No")
        desicion_persona = int(input("Ingresa tu opción: "))
        if desicion_persona == 1:
            precio_adulto_may = persona_precio[0] * 0.88
            visitantes.append([nombre, edad, precio_adulto_may, nombre_descuentos[2]])
            print("Se te otorgara Descuento de Adulto Mayor 12%")
        else:
            visitantes.append([nombre, edad, persona_precio[0], nombre_descuentos[3]])
            print(f"Por no tener Identificación de Adulto Mayor, pagaras la cantidad de ${persona_precio[0]}")
    elif edad <= 3:
        visitantes.append([nombre, edad, persona_precio[2], nombre_descuentos[3]])
        print("Esta persona entra GRATIS")
        continue
    elif 3 < edad < 18:
        print("¿Cuenta con una identificación como Estudiante?\n1 = Sí\n2 = No")
        desicion_persona = int(input("Ingresa tu opción: "))
        if desicion_persona == 1:
            precio_estudiante = persona_precio[1] * 0.90
            visitantes.append([nombre, edad, precio_estudiante, nombre_descuentos[0]])
            print("Se te otorgara Descuento de Estudiante 10%")
        else:
            visitantes.append([nombre, edad, persona_precio[1], nombre_descuentos[3]])
            print("No se te aplicara un Descuento Especial")
    else:
        # Pregunta si tiene identificación válida
        while True: #(desicion_persona)
            print("¿Cuenta con una identificación como Estudiante o Profesor?\n1 = Sí\n2 = No")
            desicion_persona = int(input("Ingresa tu opción: "))

            if desicion_persona == 1:
                # Pregunta tipo de identificación
                while True: #(tipo_persona)
                    print("¿Con cuál identificación cuentas?\n1 = Estudiante\n2 = Profesor\n3 = Ir atras")
                    tipo_persona = int(input("Ingresa tu opción: "))

                    if tipo_persona in (1, 2, 3):
                        match tipo_persona:
                            case 1:
                                precio_estudiante = persona_precio[0] * 0.90
                                visitantes.append([nombre, edad, precio_estudiante, nombre_descuentos[0]])
                                print("Se te otorgara Descuento de Estudiante 10%")
                            case 2:
                                precio_profesor = persona_precio[0] * 0.90
                                visitantes.append([nombre, edad, precio_profesor, nombre_descuentos[1]])
                                print("Se te otorgara Descuento de Profesor 10%")
                        break  # sale del while tipo_persona
                    elif tipo_persona == 3:
                        break  # vuelve al menú anterior
                    else:
                        print("¡Opción no válida! Intenta de nuevo.\n")
                # si ya se agregó una persona, salimos del while principal
                if tipo_persona in (1, 2):
                    break
            elif desicion_persona == 2:
                print("No se te otorgará un descuento especial.")
                visitantes.append([nombre, edad, persona_precio[0], nombre_descuentos[3]])
                break  # sale del while desicion_persona
            else:
                print("¡Opción no válida! Intenta de nuevo.\n")

total_visitantes = len(visitantes)

#Ticket de Compra de Boletos
# Encabezado del ticket
print("""
+================================================+
|        Museo de Antropología e Historia         |
|                 Ticket de Venta                 |
+================================================+
""", end="")

print(f"| No. de visitantes: {total_visitantes:<28}|")
print("+-================================================+")

# Cabecera de la tabla con columnas alineadas
print(f"| {'Nombre':<10} {'Edad':<5} {'Costo':<10} {'Descuento':<19}|")
print("+------------------------------------------------+")

# Detalle de compra
for i in range(len(visitantes)):
    total_pagar += visitantes[i][2]
    print(f"| {visitantes[i][0]:<10} {visitantes[i][1]:<5} {visitantes[i][2]:<10.2f} {visitantes[i][3]:<19}|")

# Totales y cierre
print("+================================================+")
print(f"| Total a Pagar: ${total_pagar:<31.2f}|")
print("+================================================+")
print("|             ¡GRACIAS POR TU VISITA!            |")
print("+================================================+")