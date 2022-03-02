from sqlite3 import Cursor
import sympy
import numpy as np
import psycopg2
def IVA(): #precioSinIva*0.12+precioSinIva = PrecioTotal
    print("Ingrese el precio en quetzales :")
    precio = entradaEntera()
    precio_sin_iva= precio/(1.12)
    Iva = 0.12*precio_sin_iva
    return [precio,precio_sin_iva,Iva]

def entradaEntera():
        try:
            x = float(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera()

def menu():
    try:
        print("\n0. Mostrar Iva y precio sin iva \n1. Ver historial \n2. Eliminar datos \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")

def conectar():
    try:
        conexion = psycopg2.connect(
            host = "localhost",port = "5432", database = "Parcial1", user = "postgres", password = "123456")
        return conexion
    except psycopg2.Error: 
        print("no se pudo conectar")

def obtener(curs):
    curs.execute('SELECT*FROM iva')
    valores= curs.fetchall()
    print(valores)

def insertar(conexion,curs, precio,iva,preciosin):
    curs.execute("INSERT INTO iva(precio,iva,precio_sin_iva) VALUES(%s,%s,%s);",( precio,iva,preciosin))
    conexion.commit()

def eliminarOpciones(conexion, curs):
        curs.execute('DELETE FROM iva')
        conexion.commit()


while True:
    conexion =conectar()
    cursor = conexion.cursor()
    opcion = menu()
    while opcion==None:
        opcion = menu()
    if opcion==0:
        resultado = IVA()
        print("Precio sin IVA [Q]: "+str(resultado[1]))
        print("IVA [Q]: "+str(resultado[2]))
        insertar(conexion,cursor,resultado[0],resultado[1],resultado[2])
        input("\n Presione enter para continuar")
    elif opcion ==1:
        obtener(cursor)
        input("\n Presione enter para continuar")
    elif opcion ==2:
        eliminarOpciones(conexion,cursor)
        input("\n Presione enter para continuar")
    elif opcion == 3:
        cursor.close()
        conexion.close()
        break
    else:
        print("seleccione una opcion valida")
        input("presione para continuar")
        cursor.close()
        conexion.close()