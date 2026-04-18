#create class
class parrot:

    # class attribute
    species = "bird"
    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the parrot class
blu = parrot("blu", 10)
woo = parrot("woo", 15)

# access the class attributes
print("Blu is a ",blu.species)
print("woo is also a {}, and it is beautiful".format(woo.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))