from Terrenos import Terreno
import xml.etree.ElementTree as ET
import os
import Lista_Simple as lstS
import Doble_enlazada as dEnz

def ImprimirDtEst():
    print('* Kevin Estuardo Secaida Molina')
    print('* 201602404')
    print('* Introducción a la programación y computación 2 sección "D"')
    print('* Ingenieria en Ciencias y Sistemas')
    print('* 4to. Semestre \n')

def CargarArch():
    tree = ET.parse("entrada.xml")
    #tree = ET.parse(ruta)
    raiz = tree.getroot()
    print(raiz)
    print('\nTodos los Atributos')
    for elemento in raiz: 
        print(elemento.tag, elemento.attrib)
        #print(elemento.attrib)
        for subelemento in elemento: 
            print(subelemento.tag, subelemento.attrib)
            # print(subelemento.attrib)
            print(subelemento.text)

   

def listArchivos():
    ejemplo_dir =  'C:/Users/SM/Documents/GitHub/P1/IPC2_Proyecto1_201602404'
    with os.scandir(ejemplo_dir) as ficheros:
        ficheros = [fichero.name for fichero in ficheros
        if fichero.is_file() and fichero.name.endswith('.xml')]
        print('\n', ficheros, '\n')

def listaDoble():
    return

# def menuProceso():
#     while(True):
#         print("-----Menu-----\n"+
#             "1.- Enlistar los terrenos \n"+
#             "2.- Procesar los terrenos \n"+
#             "3.- Regresar al menu principal \n")
#         num = input("Elija la opción: \n")
#         if num == "1":
#             listArchivos() #falta crear el metodo de las listas para guardar solo el nombre del terreno.
#         elif num == "1":
#             lstS.listadoTerrenos()
#         #elif num == "2":
#         elif num == "6":
#             Menu()


def Menu():

    while(True):
        print("-----Menu-----\n"+
            "0.- Enlistar los archivos (.xml) \n"+
            "1.- Cargar Archivo \n"+
            "2.- Procesar Archivo \n" +
            "3.- Escribir Archivo de salida \n" +
            "4.- Datos del estudiante \n" +
            "5.- Gererar gráfica \n" +
            "6.- Salir \n" )
        num = input("Elija la opción: \n")
        if num == "0":
            listArchivos()
        elif num == "1":
            #ruta = input("Nombre del archivo: ")
        #    CargarArch(ruta)
             CargarArch()
        #elif num == "2":

       # elif num == "3":

        elif num == "4":
            print('Los datos del estudiante son: \n')
            ImprimirDtEst()
        #elif num == "5":

        elif num == "6":
            return False
Menu()