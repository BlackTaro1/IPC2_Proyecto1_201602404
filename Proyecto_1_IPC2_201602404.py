import xml.etree.ElementTree as ET
from io import open 

def ImprimirDtEst():
    print('* Kevin Estuardo Secaida Molina')
    print('* 201602404')
    print('* Introducción a la programación y computación 2 sección "D"')
    print('* Ingenieria en Ciencias y Sistemas')
    print('* 4to. Semestre \n')  

def CargarArch():
    archivo_xml=open("Taro.xml", "w")
    print(archivo_xml)

    tree = ET.parse("Taro.xml")
    raiz = tree.getroot()
    print(raiz)
  
 

def Menu():
          opcion = 0
          while opcion != 6:
            print('----- Menu Principal -----')
            print('1. Cargar archivo.')
            #print('2. Procesar archivo')
            #print('3. Escribir archivo de salida')
            print('4. Mostrar datos del estudiante')
            #print('5. Generar gráfica')     
            print('6. Salir')
            opcion = input()
            ruta = ''
            if opcion == '1':
                print('El archivo a cargar es: ')
                CargarArch()
            elif opcion == '4':
                print('Los datos del estudiante son: \n')
                ImprimirDtEst()

            else:
                opcion = 6
Menu()