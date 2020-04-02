people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7}
]

def get_age(name):
    for person in people:
        if(person['name'] == name):
            return person['age']

    return 'nothing'

print(get_age('bob'))
