import xml.etree.ElementTree as ET
import os

def ImprimirDtEst():
    print('* Kevin Estuardo Secaida Molina')
    print('* 201602404')
    print('* Introducción a la programación y computación 2 sección "D"')
    print('* Ingenieria en Ciencias y Sistemas')
    print('* 4to. Semestre \n')  

def CargarArch(ruta):
    #tree = ET.parse("test.xml")
    tree = ET.parse(ruta)
    raiz = tree.getroot()
    print(raiz)
    # for elemento in raiz:
    #     print('Estudiante',elemento.attrib['x'],'ha sido insertado.')
    #     estudiantes.crearEstudiante(elemento.attrib['carnet'], elemento.attrib['nombre']) # inserta estudiante
    #     for subelemento in elemento.iter('curso'):
    #         estudiante = estudiantes.getEstudiante(elemento.attrib['carnet'])#se busca estudiante
    #         estudiante.lista_cursos.insertar(subelemento.attrib['codigo'], subelemento.attrib['nombre'], subelemento.text) # se asigna curso
    #         print('Se asigno el curso', subelemento.attrib['nombre'],'al estudiante',estudiante.nombre)

    print('\nCoordenadas de todos los terrenos.')
    for elemento in raiz: 
        #for subelemento in elemento: 
            print(elemento.attrib)

def listArchivos():
    ejemplo_dir =  'C:/Users/SM/Documents/GitHub/P1/IPC2_Proyecto1_201602404'
    with os.scandir(ejemplo_dir) as ficheros:
        ficheros = [fichero.name for fichero in ficheros
        if fichero.is_file() and fichero.name.endswith('.xml')]
        print('\n', ficheros, '\n')
 

def Menu():
    while(True):
        print("-----Menu-----\n"+
            "0.- Enlistar los archivos (.xml) \n"+
            "1.- Agregar \n"+
            "2.- Listar \n" +
            "3.- Buscar \n" +
            "4.- Busqueda Binaria \n" +
            "5.- Tamaño \n" +
            "6.- Salir \n" )
        num = input("Elija la opción: \n")
        if num == "0":
            listArchivos()
        elif num == "1":
            ruta = input("Nombre del archivo: ")
            CargarArch(ruta)
        #elif num == "2":
         
       # elif num == "3":
           
        elif num == "4":
            print('Los datos del estudiante son: \n')
            ImprimirDtEst()
        #elif num == "5":

        elif num == "6":
            return False
Menu()