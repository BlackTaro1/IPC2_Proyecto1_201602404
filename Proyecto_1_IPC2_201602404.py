from Terrenos import Terreno
from Posicion import Posicion
from Lista_Simple import ListaSimple
import xml.etree.ElementTree as ET
import os
import json
listaTerreno = Terreno('Terreno 1', '1,1', 1, 1,1,1, 1,1)
listaOficial = Terreno('', '1,1', 1, 1,1,1, 1,1)
Posicioninicial = Posicion(0,0, 0)

def ImprimirDtEst():
    print('* Kevin Estuardo Secaida Molina')
    print('* 201602404')
    print('* Introducción a la programación y computación 2 sección "D"')
    print('* Ingenieria en Ciencias y Sistemas')
    print('* 4to. Semestre \n')
 
def CargarArch():
    tree = ET.parse("test.xml")
    #tree = ET.parse(ruta)
    inicio = tree.getroot()
    print(inicio)
    print('\nTodos los Atributos')
    for elemento in inicio:
        #print(elemento.tag, elemento.attrib)
        atributo = json.dumps(elemento.attrib)
        terrenoname = json.loads(atributo)
        nombre = terrenoname["nombre"]
        listaTerreno.nombre = nombre
        print("\n", listaTerreno.nombre,"\n")
        for subelemento in elemento:
            #print(subelemento.tag)
            if subelemento.tag == "dimension":
                for subelemento1 in subelemento:
                    #print(subelemento1.text)
                    if subelemento1.tag == "m":
                        listaTerreno.dimensionm = subelemento1.text
                    if subelemento1.tag == "n":
                        listaTerreno.dimensionn = subelemento1.text
                print(listaTerreno.dimensionm, listaTerreno.dimensionn)
            if subelemento.tag == "posicioninicio":
                for subelemento1 in subelemento:
                    #print(subelemento1.text)
                    if subelemento1.tag == "x":
                        listaTerreno.iniciox = subelemento1.text
                    if subelemento1.tag == "y":
                        listaTerreno.inicioy = subelemento1.text
                print(listaTerreno.inicioy, listaTerreno.iniciox)
            if subelemento.tag == "posicionfin":
                for subelemento1 in subelemento:
                    #print(subelemento1.text)
                    if subelemento1.tag == "x":
                        listaTerreno.finx = subelemento1.text
                    if subelemento1.tag == "y":
                        listaTerreno.finy = subelemento1.text
                print(listaTerreno.finx, listaTerreno.finy)
            if subelemento.tag == "posicion":
                    Posicioninicial.combustible = subelemento.text
                    gas = json.dumps(subelemento.attrib)
                    pos = json.loads(gas)
                    Posicioninicial.posx = pos["y"]
                    Posicioninicial.posy = pos["x"]
                    listaTerreno.posicion = Posicioninicial
                    print(listaTerreno.posicion.posy, listaTerreno.posicion.posx, listaTerreno.posicion.combustible)
        #lst = ListaSimple.insertarTerreno(listaOficial, listaTerreno)
        tg = listaTerreno, "hola :3"
        lst = ListaSimple.imprimir(listaTerreno)
            #print(subelemento.attrib)
            #print("subelemento.text")





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
            #asd = ListaSimple.imprimir('fjalkñd')
        #elif num == "2":

       # elif num == "3":

        elif num == "4":
            print('Los datos del estudiante son: \n')
            ImprimirDtEst()
        #elif num == "5":

        elif num == "6":
            return False
Menu()