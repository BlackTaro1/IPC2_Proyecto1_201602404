import xml.etree.ElementTree as ET

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
    
    print('\nCoordenadas de todos los terrenos.')
    for elemento in raiz: 
        #for subelemento in elemento: 
            print(elemento.attrib)
 

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
        num = input("Elija la opción: ")
        if num == "1":
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
            

        #   opcion = 0
        #   while opcion != 6:
        #     print('----- Menu Principal -----')
        #     print('1. Cargar archivo.')
        #     print('2. Procesar archivo')
        #     print('3. Escribir archivo de salida')
        #     print('4. Mostrar datos del estudiante')
        #     print('5. Generar gráfica')     
        #     print('6. Salir')
        #     opcion = input()
        #     ruta = ''
        #     if opcion == '1':
        #         print('El archivo a cargar es: ')
        #         ruta = input()
        #         CargarArch(ruta)
        #     elif opcion == '4':
        #         print('Los datos del estudiante son: \n')
        #         ImprimirDtEst()

        #     else:
        #         opcion = 6
Menu()