def main():
    #escribe tu código abajo de esta línea
    jNuevos = int(input('Dame la cantidad de juegos nuevos: '))
    jUsados = int(input('Dame la cantidad de juegos usados: '))

    total = (jNuevos * 1000) + (350 * jUsados)

    print('El total de la compra es: ' + str(total))



if __name__ == '__main__':
    main()
