while True:
    try:
        numero_1 = int( input('Ingresar primer numero: ') )
        numero_2 = int( input('Ingresar segundo numero: ') )

        print('CALCULADORA')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicacion')
        print('4. Division')
        opcion = int( input('Ingresar opcion: ') )

        resultado = 0
        texto = ''
        if opcion == 1:
            resultado = numero_1 + numero_2
            texto = 'de la suma'
        elif opcion == 2:
            resultado = numero_1 - numero_2
            texto = 'de la resta'
        elif opcion == 3:
            resultado = numero_1 * numero_2
            texto = 'de la multiplicacion'
        elif opcion == 4:
            resultado = numero_1 / numero_2
            texto = 'de la resta'

        print('El resultado {} es: {}'.format(texto, resultado))
        break
    except ValueError as error:
        print('Debe ingresar solo numeros.')
    except ZeroDivisionError as error:
        print('No se puede dividir para cero')
