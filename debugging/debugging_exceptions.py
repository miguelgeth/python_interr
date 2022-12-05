def divisor(num):
    divisors = [i for i in range(1,num + 1) if num % i == 0 ]
    return divisors


def run():# donde falla el programa ponemos try
    try:
        num = int(input("ingresa un numero: "))
        print(divisor(num))
        print("end")
    except ValueError:
        print("debes ingresar un numero")


if __name__ == '__main__':
    run()