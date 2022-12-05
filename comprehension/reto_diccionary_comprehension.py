def run():
    # diccionary_comprehension = {i: i*i for i in range(1,1001) if i % i == 0}
    # print(diccionary_comprehension)# asi lo hice pero qudo al reves 7:49 y tiene que qeudar 49:7 pero lo resolvi mal, lo correcta es la de abajo
    diccionary_comprehension = {i: round(i**0.5,2) for i in range(1,1001)}#en vez de 0.5 le coloco 2 pero me queda al contrario, tipo 3:9
    # ! EN DICCIONARY EL IF ES OPTIONAL
    print(diccionary_comprehension)# asi lo hice pero qudo al reves 7:49 y tiene que qeudar 49:7


if __name__ == '__main__':
    run()