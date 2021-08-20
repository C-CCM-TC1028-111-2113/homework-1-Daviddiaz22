def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    mensajes = int(input('Dame el número de mensajes: '))
    megas = float(input('Dame el número de megas: '))
    minutos = int(input('Dame el número de minutos: '))

    total = (mensajes * 0.8) + (megas * 0.8) + (minutos * 0.8)

    print('El costo mensual es: ' + str(total))

if __name__ == '__main__':
    main()
