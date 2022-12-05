def run():
    pass
    # squares = []# lista normal!!!!!!!!!!!!!!!!!
    # for i in range(1,101):
    #     if i % 3 != 0:# si es 0 si es divisible por 3, pero en este caso queremos lo que no sean divisibles
    #         squares.append(i**2)#squared(al cuadrado)
    #     print(squares)


# list comprenhension
    squares = [i**2 for i in range(1,101) if i %3 != 0]
    # para cada i en el rango qeu va de 1-101 voy a guardar esa i **2 solo si esa i %3 es distinta a 0
    print(squares)

if __name__ == '__main__':
    run()