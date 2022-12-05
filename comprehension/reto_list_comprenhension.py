def run():
    list_comprenhension = [i for i in range(1,10000) if i % 4 == 0 and i % 6 == 0 and  i % 9 == 0]# no lo pude hacer porque no sabia como hacer el metodo matematico
    print(list_comprenhension)# tambien podemos escribir if i % 36 == 0, porque este es multiplo de 4,6,9 y asi me ahorro este codigo


if __name__ == '__main__':
    run()