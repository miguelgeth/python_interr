DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():# leer reto_filtrar
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]# worker es como poner i le ponemos el nombre que quede mas acorde
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]# pendiente con las mayus
    adults = list(filter(lambda worker: worker["age"] >18 ,DATA))
    adults = list(map(lambda worker: worker["name"] ,adults))# porque ahora DATA esta en adults// y con este map ya me sale solo los nombres
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))# |(pipe) es nuevo solo funcion en python3.9 lo que hace es unir un diccionario con una nuevo "old" seria el nombre del diccionario, pero se hace con diccionarios, con LISTAS ES +
    #  y al momento de print me sale la nueva key "old":True or False, si es mayour de 70 da true

    for worker in adults:# aca solo se le cambia esta parte y listo y si solo dejamos adults y este for me imprime lo que le dije pero me trae todo como un diccionario, para evitar eso le hacemos un map
        print(worker)

    # for worker in all_python_devs:
    #     print(worker)


if __name__ == '__main__':
    run()