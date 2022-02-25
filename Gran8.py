from os import curdir
import random
import psycopg2
from sympy import true
import numpy as np

#print(Dado)
def lanzar_Dado():
    input("presione enter para lanzar el dado")
    Dado = random.randint(1, 6)
    return Dado

def menu():
    try:
        print("\n0. Jugar \n1. Ver historial \n2. Eliminar datos \n3. Salir")
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
    curs.execute('SELECT*FROM Gran8')
    valores= curs.fetchall()
    print(valores)

def insertar(conexion,curs, Dado1, Dado2, Suma):
    curs.execute("INSERT INTO Gran8( Dado1, Dado2, Suma) VALUES(%s,%s,%s);",( Dado1, Dado2, Suma))
    conexion.commit()

def eliminarOpciones(conexion, curs):
        curs.execute('DELETE FROM Gran8')
        conexion.commit()

while True:
    conexion= conectar()
    cursor = conexion.cursor()
    opcion= menu()
    while opcion==None:
        opcion = menu()
    if opcion==0:
        jugar = True
        while jugar == True:
            print("Dado 1: ")
            Dado1 = lanzar_Dado()
            print(Dado1)
            print("Dado 2: ")
            Dado2 = lanzar_Dado()
            print(Dado2)
            suma = Dado1+Dado2
            if suma==8:
                print("Ganar")
                jugar = False
            elif suma ==7:
                print("Perder")
                jugar = False
            else:
                input("¡continue lanzando¡ , presione para continuar")
            insertar(conexion,cursor, Dado1, Dado2, suma) 
        input("\n presione para continuar")        
    elif opcion==1:
        obtener(cursor)
        input("\n presione enter para continuar")
    elif opcion == 2:
        eliminarOpciones(conexion,cursor)
    elif opcion == 3:
        cursor.close()
        conexion.close()
        break
    else:
        print("seleccione una opcion valida")
        input("presione para continuar")
        cursor.close()
        conexion.close()