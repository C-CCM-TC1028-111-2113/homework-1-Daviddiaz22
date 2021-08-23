def main():
    #escribe tu código abajo de esta línea
    import math
    palabras = int(input('Dame el número de palabras: '))

    hojas = math.ceil((palabras / 475))
    costo = hojas * 60
    costo = costo - (costo * .1)

    print('El costo de la publicación es: ' + str(costo))


if __name__ == '__main__':
    main()
