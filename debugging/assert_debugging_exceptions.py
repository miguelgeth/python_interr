def divisor(num):
    divisors = [i for i in range(1,num + 1) if num % i == 0 ]
    return divisors


def run():# assert es una alternativa de try, except
    num = input("ingresa un numero: ")# le quitamos el int porque el isnumeric mira sollo strings
    assert num.isnumeric(), "debes ingresar un numero"#isnumeric devuelve si ese num es true or false y afirma qeu tieen qeu ser un numeroString (despues lo pasamos a int) pero si es un string normal me vota el false y me print ese texto
    print(divisor(int(num)))# lo pasamos a int
    print("end")


if __name__ == '__main__':
    run()