# def divisor(num):
#     divisors = [i for i in range(1,num + 1) if num % i == 0 ]
#     return divisors


# def run():# 
#     num = (input("ingresa un numero: "))
#     assert num.isnumeric() and int(num) <= 0,"ingresa un numero positivo"
#     print(divisor(int(num)))
#     print("end")


# if __name__ == '__main__':
#     run()












def divisor(num):
    divisors = [i for i in range(1,num+1) if num%i == 0]
    return divisors

def run():
    num = input('Enter a number: ')
    assert num.isnumeric() and int(num)>0, 'Ingresa solo numeros positivos'# como es una afirmacion num>0 porque num tiene qeu ser mayor
    print(divisor(int(num)))
    print('Finish')


if __name__ == '__main__':
    run()