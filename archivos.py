def read():
    numbers = []# encoding ="utf-8" es como lo de html esto es para que lea cualquier tipo de caracter y eso ej: ñ ´ etc
    with open("./archivos/numebers.txt", "r", encoding="utf-8") as f: #cuando algo tieen : es un bloque de codigo abajo
        for line in f:# con for podemos leer cada linea del archivo(f)
            numbers.append(int(line))# porque lee str entonces lo pasamos a int
    print(numbers)

def write():
    names = ["Facundo", "Miguels", "Pepe", "Christian"]# crear un archivo que contenga en cada linea estos nombrs
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:#hciimos esto dle url/names.txt y lo llamamos en la console sin tener el archivo, y al hacer esto me creo el archivo /// SI CAMBIO "w" por "a" esto lo que hace es que me agrega el name por el qeu cambie, con w no me lo agrega me lo reescribe entonces el el name viejo se pierde
        for name in names:
            f.write(name)# write all the names
            f.write("\n")# then un salto de linea
    # print(names)# aun no hemos print entonces si le cambiamos el name a miguel por otro se sobreescribe el archivo en el momento de que lo llame por consola


def run():
    write()# aca es donde llamamos entonces si quiero llamar read() se lo cambio aca


if __name__ == '__main__':
    run()