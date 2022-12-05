def run():
    # diccionary = {} diccionary normal
    # for i in range(1,101):
    #     if i % 3 != 0:# que no sean divisible por 3
    #         diccionary[i] = i**3# lo guardamos en i y depues para que se eleve al cubo
    #     print(diccionary)
    diccionary_comprehension = {i: i**3 for i in range(1,101) if i %3 != 0}# para cada element en un iterable(i) voy a colocar una key y un value solamente si se cumple una condition
    print(diccionary_comprehension)

if __name__ == '__main__':
    run()