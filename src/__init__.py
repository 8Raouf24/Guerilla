
import random

war_characters = [
    "Alexander",
    "Napoleon",
    "Hannibal",
    "Caesar",
    "Saladin",
    "Patton",
    "Joan",
    "Genghis",
    "Churchill",
    "Rommel"
]



def return_random_name(list_names):
    rand_index =  random.randint(0,len(list_names)-1)
    name = list_names[rand_index]
    list_names.pop(rand_index)

    

    return name

