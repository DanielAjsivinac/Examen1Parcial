from queue import PriorityQueue
import sympy
import numpy as np
import statistics as stat
import psycopg2

def programa(notas):
    ordnum = notas
    a = len(ordnum)-1
    moda = stat.mode(notas)
    media = np.mean(notas)
    mediana = np.median(notas)
    ordnum.sort()
    rango = ordnum[a]-ordnum[0] 
    desviacionestandar = stat.pstdev(notas)
    varianza = desviacionestandar*desviacionestandar
    return [moda, media, mediana, rango,desviacionestandar, varianza]  

def menu():
    try:
        print("\n0. mostrar datos estadisticos \n1. Ver historial \n2. Eliminar datos \n3. Salir")
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
    curs.execute('SELECT*FROM calif')
    valores= curs.fetchall()
    print(valores)

def insertar(conexion,curs, calificaciones, moda, media,mediana, rango, desviacion, varianza):
    curs.execute("INSERT INTO calif( calificaciones, moda, media,mediana, rango, desviacion, varianza) VALUES(%s,%s,%s,%s,%s,%s,%s);",( calificaciones, moda, media,mediana, rango, desviacion, varianza))
    conexion.commit()

def eliminarOpciones(conexion, curs):
        curs.execute('DELETE FROM calif')
        conexion.commit()

while True:
    conexion= conectar()
    cursor = conexion.cursor()
    calificaciones = [60, 70, 80, 90, 100]
    opcion = menu()
    while opcion==None:
        opcion= menu()
    if opcion == 0:
        datos = programa(calificaciones)
        print("La moda es: "+str(datos[0])+"\n")
        print("La media es: "+str(datos[1])+"\n")
        print("La mediana es: "+str(datos[2])+"\n")
        print("La rango es: "+str(datos[3])+"\n")
        print("La desviacion estandar es: "+str(datos[4])+"\n")
        print("La varianza es: "+str(datos[5])+"\n")
        insertar(conexion,cursor,calificaciones,datos[0],datos[1],datos[2],datos[3],datos[4],datos[5])
        input("presione enter para continuar")

    elif opcion == 1:
        obtener(cursor)
        input("\n presione para continuar")
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