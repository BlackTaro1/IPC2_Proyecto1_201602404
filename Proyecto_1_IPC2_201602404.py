from ListaSimpleTerrenos import listaSimpleTerrenos, nodoTerreno
from encabezado import listaEncabezado
from Terrenos import Terreno
from Posicion import Posicion
from listaDoblePosicion import listaDoblePosicion
import xml.etree.ElementTree as ET
import os
import json
ls = listaDoblePosicion()
lsS = listaSimpleTerrenos()
listaTerreno = Terreno('Terreno 1', '1,1', 1, 1,1,1, 1,1)
listaOficial = Terreno('', '1,1', 1, 1,1,1, 1,1)
Posicioninicial = Posicion(None, None, None)


def ImprimirDtEst():
    print('* Kevin Estuardo Secaida Molina')
    print('* 201602404')
    print('* Introducción a la programación y computación 2 sección "D"')
    print('* Ingenieria en Ciencias y Sistemas')
    print('* 4to. Semestre \n')
 
def CargarArch():
    tree = ET.parse("entrada.xml")
    #tree = ET.parse(ruta)
    inicio = tree.getroot()
    print(inicio)
    # for nodo in inicio.iter("TERRENO"):
    #     nombre = nodo.attrib["nombre"]
    #     for n, m in inicio.iter("DIMENSION"):
    #         n = int(nodo.attrib['n'])
    #         m = int(nodo.attrib['m'])
    #         print(m,n, nombre,"h")
    #         xini = None
    #         yini = None
    #         xfin = None
    #         yfin = None
    #         for inicio, fin in zip(nodo.iter("posicioninicio"), nodo.iter("posicionfin")):
    #             for xin, yin, xfi, yfi in zip(inicio.iter("x"), inicio.iter("y"), fin.iter("x"), fin.iter("y")):
    #                 xini = int(xin.text)
    #                 yini = int(yin.text)
    #                 xfin = int(xfi.text)
    #                 yfin = int(yfi.text)
    #                 print(xini, "x inicial")
    #lsS.insertarenlistaVacia(nombre, m, n, xini, yini, xfin, yfin)
    #lsS.iterar()
    
    print('\nTodos los Atributos')
    for elemento in inicio:
        print(elemento.tag, elemento.attrib)
        atributo = json.dumps(elemento.attrib)
        terrenoname = json.loads(atributo)
        nombre = terrenoname["nombre"]
        print(nombre, "nombre del terreno")
        listaTerreno.nombre = nombre
        print("\n", listaTerreno.nombre,"\n")
        a = Posicion(None, None, None)
        for subelemento in elemento:
            print(subelemento.tag)
            if subelemento.tag == "dimension":
                for subelemento1 in subelemento:
                    print(subelemento1.text)
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
    #             print(listaTerreno.inicioy, listaTerreno.iniciox)
            if subelemento.tag == "posicionfin":
                for subelemento1 in subelemento:
    #                 #print(subelemento1.text)
                    if subelemento1.tag == "x":
                         listaTerreno.finx = subelemento1.text
                    if subelemento1.tag == "y":
                         listaTerreno.finy = subelemento1.text
                print(listaTerreno.finx, listaTerreno.finy)
            if subelemento.tag == "posicion":
                     #Posicioninicial.combustible = subelemento.text
                    P1 = subelemento.text
                    gas = json.dumps(subelemento.attrib)
                    pos = json.loads(gas)
    #                 # Posicioninicial.posx = 
    #                 # Posicioninicial.posy = pos["x"]
    #                 # listaTerreno.posicion = Posicioninicial
    #                 #ls.insertar(pos["y"], pos["x"], Posicioninicial.combustible)
                    ls.insertar(pos["x"], pos["y"], P1)
    #                 #print(a, "hi")
    #               #  print(listaTerreno.posicion.posy, listaTerreno.posicion.posx, listaTerreno.posicion.combustible)
    #     #lst = ListaSimple.insertarTerreno(listaOficial, listaTerreno)
    #         #print(subelemento.attrib)
    #         #print("subelemento.text")
    #     #ls.imprimir()
    for i in ls.iterar():
         print(i)




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