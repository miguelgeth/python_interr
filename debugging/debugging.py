def divisor(num):
    divisors = [i for i in range(1,num + 1) if num % i == 0 ]#esto esta hecho mal a proposito para usar DEBUGGING y el error es qeu si un numero para ser divisor de otro tiene qeu dar 0 no 1
    # divisors.append(i) esto se le agrega si lo hacemos de la manera normal, porque divisors es un lista vacia entonces le agregamos el append (i) para que le pase la info e itere
    return divisors

    #todo lo vamos a usar con lambda para probar: uso de lambda la uso si quiero hacer algo que es sencillo de una maner mas rapida y CUANDO TENEMOS HIGH-ORDER-FUNCTION OSEA QUE LE PASAMOS COMO ARGUMENTO UNA FUNCION A OTRA, EN ESTE CASO SI SIRVE LAMBDA
# divisors = lambda num:[i for i in range(1,num +1) if num % i == 0] quitamos el def porque lambda es una funcion anonima
    
def run():
    num = int(input("ingresa un numero"))
    # print(divisors(num))lambda
    print(divisor(num))
    print("end")


if __name__ == '__main__':
    run()