import xml.etree.ElementTree as ET
import os
from ListaSimpleTerrenos import listaSimpleTerrenos as LsT


class Principal:
    def __init__(self):
        self.LsT = LsT()

    def ImprimirDtEst():
            print('* Kevin Estuardo Secaida Molina')
            print('* 201602404')
            print('* Introducción a la programación y computación 2 sección "D"')
            print('* Ingenieria en Ciencias y Sistemas')
            print('* 4to. Semestre \n')

    def CargarArch(self, ruta): #para cuando lo solicite el aux ingresar el archivo poner ruta dentro de los parentesis de cargarARch
        #tree = ET.parse("test.xml")
        tree = ET.parse(ruta)
        inicio = tree.getroot()
        for nodo in inicio:
            nombre = nodo.attrib["nombre"]
            for subnodo, ini, fi in zip(nodo.iter("dimension"), nodo.iter("posicioninicio"), nodo.iter("posicionfin")):
                for n, m, xin, yin, xfi, yfi in zip(subnodo.iter("n"), subnodo.iter("m"), ini.iter("x"), ini.iter("y"), fi.iter("x"), fi.iter("y")):
                    n = int(n.text)
                    m = int(m.text)
                    xini = int(xin.text)
                    yini = int(yin.text)
                    xfin = int(xfi.text)
                    yfin = int(yfi.text)
                #print(nombre,"\n", "hola", n , "h") #---> sale el nombre
                #print(nombre, "\n", n, m, xini, yini, xfin, yfin) #--- sale n,m,xinicial, y inicial, xfinal, y final
        
            for posiciones in nodo.iter("posicion"):
                a = int(posiciones.text) #---> gas
                b = int(posiciones.attrib["x"]) #----> eje x 
                c = int(posiciones.attrib["y"]) #---> eje y
                #print(b, "pos x", c, "pos y", a, "combustible")
            terreno = terrenos = self.LsT.insertarTerreno(nombre, n, m, xini, yini, xfin, yfin)
            pos = terrenos.listaPosiciones.insertar(b, c, a)
            print(pos.gas, terreno.listaPosiciones.iterar, "combustible", terreno.nombre)
            
    
    def getListaTerreno(self, nombre):
        terreno = self.LsT.getTerreno(nombre)
        listaDoblePosicion = terreno.listaPosiciones.getList()
        
        


    def listArchivos():
        ejemplo_dir =  'C:/Users/SM/Documents/GitHub/P1/IPC2_Proyecto1_201602404'
        with os.scandir(ejemplo_dir) as ficheros:
            ficheros = [fichero.name for fichero in ficheros
            if fichero.is_file() and fichero.name.endswith('.xml')]
            print('\n', ficheros, '\n')


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


class Menu():
    
    def Menu():
        p = Principal()
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
                p.listArchivos
                #listArchivos()
            elif num == "1":
                ruta = input("Nombre del archivo: ")
                p.CargarArch(ruta)
                #CargarArch()
            #asd = ListaSimple.imprimir('fjalkñd')
        #elif num == "2":

       # elif num == "3":

            elif num == "4":
                print('Los datos del estudiante son: \n')
                p.ImprimirDtEst()
        #elif num == "5":

            elif num == "6":
                return False
    Menu()



    