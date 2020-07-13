# Create a tuple named zoo that contains 10 of your favorite animals.

zoo = ("tiger", "giraffe", "orangutan", "gorilla", "spider monkey",
       "puma", "rhinoceros", "chicken", "squirrel", "rabbit")

print(zoo.index("puma"))
print(zoo.index("squirrel"))

animal_i_want = "chipmunk"
if animal_i_want in zoo:
    print("{animal_i_want} is here!")

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal,
 sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo
print(first_animal)
print(second_animal)
print(third_animal)
print(fourth_animal)

zoo = list(tuple(zoo))
new_animals = ["chipmunk", "porcupine", "pigeon"]
zoo.extend(new_animals)
zoo = tuple(list(zoo))
print(zoo)
