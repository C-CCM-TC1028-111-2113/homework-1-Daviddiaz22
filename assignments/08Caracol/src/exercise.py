def main():
    #escribe tu código abajo de esta línea
    minutos = float(input('Dame los minutos: '))

    recorrido = (minutos * ((5.7 * 60 )/10))

    number = round(recorrido,1)

    print('Centímentros recorridos: ' + str(number))

if __name__ == '__main__':
    main()
