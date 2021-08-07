from xml.etree.ElementTree import TreeBuilder


def ImprimirDtEst():
    print('* Kevin Estuardo Secaida Molina')
    print('* 201602404')
    print('* Introducción a la programación y computación 2 sección "D"')
    print('* Ingenieria en Ciencias y Sistemas')
    print('* 4to. Semestre \n')  

def CargarArch(ruta):
    import xml.etree.ElementTree as ET
    tree = ET.parse(ruta)
    raiz = tree.getroot()
    print('* Kevin Estuardo Secaida Molina', raiz)   

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
                print('El archivo a cargar es: ', ruta)
                ruta = input()
                CargarArch()
            elif opcion == '4':
                print('Los datos del estudiante son: \n')
                ImprimirDtEst()

            else:
                opcion = 6
Menu()