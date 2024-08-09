import json
from random import choice

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def gen_person():
    name = ''
    tel = ''

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(num)

    person = {
        'name': name,
        'tel': tel
    }
    return person


def write_json(person_dict):
    try:
        data = json.load(open('people.json'))
    except FileNotFoundError:
        data = dict()

    key = ''
    while len(key) != 10:
        key += choice(num)
    data.update({key: person_dict})

    with open('people.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())
