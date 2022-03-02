import psycopg2
def entradaEntera():
        try:
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera()

def divisores():
    div = []
    print("ingrese un numero: ")
    numero = entradaEntera()
    if numero==1:
        print("no es primo ni compuesto")
    else:
        for i in range(1, numero+1):
            if(numero % i)==0:
                div.append(i)
        if len(div)==2:
            clas = "Primo"
        else:
            clas= "Compuesto"
        return [numero, clas]

def menu():
    try:
        print("\n0. Promgrama clasificaion numeros (primos/comuestos) \n1. Ver historial \n2. Eliminar datos \n3. Salir")
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
    curs.execute('SELECT*FROM primos')
    valores= curs.fetchall()
    print(valores)

def insertar(conexion,curs, numero, primo):
    curs.execute("INSERT INTO primos(numero, primo_compuesto) VALUES(%s,%s);",( numero,primo))
    conexion.commit()

def eliminarOpciones(conexion, curs):
        curs.execute('DELETE FROM primos')
        conexion.commit()


while True:
    conexion= conectar()
    cursor = conexion.cursor()
    opcion = menu()
    while opcion == None:
        opcion = menu()
    if opcion ==0:
        resultado = divisores()
        print(resultado)
        insertar(conexion,cursor,resultado[0],resultado[1])
#        input("Presione enter para continuar")
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