def Menu():
        opcion = 1
        while opcion != 2:
            print('----- Menu Principal -----')
            print('1. Cargar archivo.')
            print('2. Procesar archivo')
            print('3. Escribir archivo de salida')
            print('4. Mostrar datos del estudiante')
            print('5. Generar gráfica')     
            print('6. Salir')
            break
        opcion = input()
        ruta = ''
        if opcion == 1:
            print('* Kevin Estuardo Secaida Molina')
            print('* 201602404')
            print('* Introducción a la programación y computación 2 sección "D"')
            print('* Ingenieria en Ciencias y Sistemas')
            print('* 4to. Semestre')         
        else:
            opcion = 2
Menu()