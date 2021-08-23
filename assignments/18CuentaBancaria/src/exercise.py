def main():
    #escribe tu código abajo de esta línea
    saldoAnterior = float(input('Dame el saldo del mes anterior: '))
    ingresos = float(input('Dame los ingresos: '))
    egresos = float(input('Dame los egresos: '))
    cheques = int(input('Dame el número de cheques: '))

    total = saldoAnterior + ingresos - egresos - (cheques * 13)

    total = total - (total * 0.075)

    print('El saldo final de la cuenta es: ' + str(total))

if __name__ == '__main__':
    main()
