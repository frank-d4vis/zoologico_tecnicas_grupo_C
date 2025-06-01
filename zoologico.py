from libreria import sumar as sm
from libreria import restar as rs
from libreria import salir as sl
from libreria import genero as gn
from libreria import edad as ed


contMasc = 0
contFem = 0
contTotal = 0
acumTotalPago = 0
nombresVisitantes = []

def reportar():
    print("\n======== REPORTE GENERAL ========\n")
    print("Cantidad total de visitantes:\t\t", contTotal)
    print("Cantidad de visitantes masculinos:\t", contMasc)
    print("Cantidad de visitantes femeninos:\t", contFem)
    print("Monto total recaudado:\t\t\t", acumTotalPago)
    print("Nombres de los visitantes:")
    for nombre in nombresVisitantes:
        print("-", nombre)

def procesar():
    global contMasc, contFem, contTotal, acumTotalPago, nombresVisitantes

    nombre = input("Ingrese su nombre:\t\t")
    nombresVisitantes.append(nombre)

    while True:
        edad = int(input("Ingrese su edad:\t\t"))
        if not ed.validar_edad(edad):
            print("ERROR, vuelva a ingresar una edad válida")
        else:
            break

    while True:
        genero = input("Ingrese su género (M/F):\t")
        generomayus = genero.upper()
        if not gn.validar_genero(generomayus):
            print("ERROR, vuelva a ingresar el género")
        else:
            break

    if generomayus == 'M':
        contMasc = sm.sumar(contMasc, 1)
    elif generomayus == 'F':
        contFem = sm.sumar(contFem, 1)


    if edad < 12:
        tipoEntrada = "Niño"
        precio = 10
    elif edad >= 60:
        tipoEntrada = "Adulto Mayor"
        precio = 8
    else:
        tipoEntrada = "Adulto"
        precio = 15

    contTotal = sm.sumar(contTotal, 1)
    acumTotalPago = sm.sumar(acumTotalPago, precio)

    print("\n===== DETALLE DE ENTRADA =====")
    print("Nombre:\t\t", nombre)
    print("Edad:\t\t", edad)
    print("Género:\t\t", genero)
    print("Tipo de entrada:\t", tipoEntrada)
    print("Monto a pagar:\t\t", precio)

def menu():
    print("\n======== MENÚ DE OPCIONES ========\n")
    print("1. Registrar entrada")
    print("2. Ver reporte")
    print("3. Salir")

    while True:
        op = int(input("Ingrese una opción:\t"))
        if op < 1 or op > 3:
            print("ERROR, opción no válida")
        else:
            break

    match op:
        case 1: procesar()
        case 2: reportar()
        case 3:
            while True:
                rpta = input("¿Desea salir del programa? (S/N): ")
                rpta = rpta.upper()
                if rpta != 'S' and rpta != 'N':
                    print("ERROR, vuelva a ingresar")
                else:
                    break
            if rpta == 'S':
                sl.salir()
            else:
                menu()
    return op

def ejecutor():
    while True:
        opcion = menu()
        if opcion == 3:
            break

ejecutor()