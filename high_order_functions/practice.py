li = [1,2,3,4,5,6,7,8,9]
def func(x):
    return x**x

empty_list = []

for x in li:
    empty_list.append(func(x))

print(empty_list)

# using MAP

li = [1,2,3,4,5,6,7,8,9]
def func(x):
    return x**x

total = list(map(func,li))
print(total)

#list comprehension
li = [1,2,3,4,5,6,7,8,9]
def func(x):
    return x**x

listaa = [func(x) for x in li if x]
print(listaa)


#filter

def add7(x):
    return x +7

def isOdd(x):
    return x%2 !=0

li = [1,2,3,4,5,6,7,8,9]

total = list(map(add7,filter(isOdd,li)))
print(total)
