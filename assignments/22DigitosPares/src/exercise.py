def main():
    #escribe tu código abajo de esta línea
    numero = input('Dame un número: ')

    lista = [int(numero[0]), int(numero[1]), int(numero[2]), int(numero[3])]
  
    val = 0
  
    for num in lista:
      

        if num % 2 == 0:
            val += 1
  
        else:
            val += 0
          
    print("El número de dígitos pares es: " + str(val))


if __name__ == '__main__':
    main()
