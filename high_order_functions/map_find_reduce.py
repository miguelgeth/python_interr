li = [1,2,3,4,5,6,7,8,9]
def func(x):
    return x**x

lista = []
for x in li:
    lista.append(func(x))
print(lista)

# now using map
li = [1,2,3,4,5,6,7,8,9]
def func(x):
    return x**x
# use map to pass a function to a list or element list
easy = list(map(func,li))
print(easy)

# with list comprehension
li = [1,2,3,4,5,6,7,8,9]
def func(x):
    return x**x
easy = list(func(x) for x in li if x % 2 == 0)# intente poner una lambda en vez de func(x) pero no me funciona Y ACA SOLO ME PRINT LOS PARES SI QUIERO TODOS PONGO SOLO /// if x listo
print(easy)


#filter()

def add7(x):
    return x + 7

def isOdd(x):
    return x%2 !=0# x divido 2 y los distinto a 0 los pritn
a = [1,2,3,4,5,6,7,8,9]

b =list(filter(isOdd,a))# filter me sirve si quiero ver un ciclo y mirar cuales estan mal
#LEER LA LINEA DE ABAJO
# c = list(map(add7,b))#le pasamos b que tiene un filter y me vota los numeros impares, y con add7 le vamos a agregar 7 numbers a cada numero del filter
#todo USAR ESTA LINEA DE ABAJO ME AHORRO CODIGO
c = list(map(add7,filter(isOdd,a)))# aca nos ahorramos codigo

print(c)