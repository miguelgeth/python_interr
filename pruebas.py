def run():

    
#     lista = [ # solo puedo guardar dicc dentro de list si quiero poner objetos dentro de list toca de la forma normal como un array y tendremos qeu llamarlo como un dicc 
#         {'firstname': 'Miguel', 'lastname': 'Garcia'},
# ]


#     for item in lista:
#         # print(item)# asi me print todo el text si quiero solo los valores lo hacemos asi
#         print(item["firstname"], "-" ,item["lastname"])# asi

#     dicc = {
#         "college_names": ['miguel','juan','andres','jose']
#     }

#     for key,value in dicc.items():
#         print(f'{key} - {value}')

    # square =[i for i in range(1,101) if i % 2 != 0]
    # print(square)

    # lista = [1,2,3,4]
    # for i in lista:
    #     if i % 2 != 0:
    #         print(i)

    # squared = [i**2 for i in squared ]
    # print(squared)

    # squared = [1,2,3,4,5]
    # for i in squared:
    #     print(i**2)

    diccio = {i: i**0.5 for i in range(1,101)}
    print(diccio)



if __name__ == '__main__':
    run()