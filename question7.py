'''
question7_.py


TOTAL POINTS AVAILABLE: 50 (10 per method) 


Code Functionality (7)
7 points - all tests pass and code uses if/else, for structures in a 
Pythonic manner without relying on elements like pass or break or 
range() unnecessarily

5-6 points - all tests pass, but code could be significantly 
improved to be more Pythonic

3-4 points - at least one test fails, but code would work with small
changes

1-2 points - no test passes and effort has been made to answer question 
but would need significant changes/additions to function correctly

0 points - no effort made to answer question



Code Readability (3)
3 points - Well commented, clear code where PyLint returns no or 
few errors/warnings

2 points - Missing either docstring or comments

1 point - Comments or documentation missing and variable names
could be improved 

0 points - multiple and repeated significant style issues, code very 
difficult to understand

'''



# Create a class called Farm which takes two inputs: name (a string) and
# starting_animals (a list of strings). The input starting_animals is optional
# with a default value of None.
#
# Give it a single class attribute called animal_capacity which is a dictionary
# containing the key-value pairs:
#   'cows':3,
#   'chickens':20,
#   'sheep':15,
#   'horses':5
#
# Within the constructor, initialise an instance attribute called name with
# the input parameter called name. Also create an instance attribute called
# animal_collection which is initially set to be an empty dictionary.
#
# Go through the starting_animals list and check if each item is a key in the
# animal_capacity class attribute. If an animal in starting_animals is not in
# the animal_capacity dictionary, raise a ValueError. If it is included, add
# it to the animal_collection dictionary as a key with a value of 1.

# Create a method called calculate_remaining_capacity which takes a string
# containing an animal name as an input. If the animal name does not exist
# as a key in the animal_capacity dictionary, then a ValueError is raised.
# If it does, then difference between the value for that animal in
# animal_capacity and animal_collection is returned.

# Overload the string method so that the string with the following format is
# returned with the name of the farm, the total number of animals, and the types
# of animals listed in alphabetical order:
# 'Imperial Farm contains 35 animals in total, including cows, horses, sheep.'
# If there are no animals, the returned string should be:
# 'Imperial Farm contains no animals.'

# Create a class called CityFarm which extends the Farm class. Set its class
# attribute animal_capacity to the following:
#   'chickens':10,
#   'sheep':5,
#   'horses':2
#
# Have the constructor accept the same inputs as for Farm, but make the starting_animals
# be a required input. Follow the same set up steps as Farm but check that the input
# animals are in the more restricted animal_capacity. For maximum marks, do not copy code
# from Farm and instead call it directly where appropriate.



class Farm:

    # Class attribute for animal capacity
    animal_capacity = {
        'cows': 3,
        'chickens': 20,
        'sheep': 15,
        'horses': 5
    }

    def __init__(self, name, starting_animals=None):

        self.name = name
        self.animal_collection = {}

        # Process starting animals
        if starting_animals:
            for animal in starting_animals:
                if animal not in Farm.animal_capacity:
                    raise ValueError(f"Animal '{animal}' is not allowed on this farm.")
                self.animal_collection[animal] = self.animal_collection.get(animal, 0) + 1

    # Calculatemthe rmaining capacity for each animal
    def calculate_remaining_capacity(self, animal):

        if animal not in Farm.animal_capacity:
            raise ValueError(f"Animal '{animal}' is not allowed on this farm.")

        current_count = self.animal_collection.get(animal, 0)

        return Farm.animal_capacity[animal] - current_count

    # Returns a string r4prssenttion of the farm
    def __str__(self):

        if not self.animal_collection:
            return f"{self.name} contains no animals."

        total_animals = sum(self.animal_collection.values())
        animal_list = ', '.join(sorted(self.animal_collection.keys()))

        return f"{self.name} contains {total_animals} animals in total, including {animal_list}."

class CityFarm(Farm):

    # Class attribute for animal capacity (overrides Farm's animal_capacity)
    animal_capacity = {
        'chickens': 10,
        'sheep': 5,
        'horses': 2
    }

    def __init__(self, name, starting_animals):

        # Temporarily replace the parent class's animal_capacity with CityFarm's
        original_animal_capacity = Farm.animal_capacity
        Farm.animal_capacity = CityFarm.animal_capacity

        # Call the Farm constructor to handle initialisation
        super().__init__(name, starting_animals)

        # Restore the original animal_capacity of the Farm class
        Farm.animal_capacity = original_animal_capacity



# Trial of Farm
my_farm = Farm("Imperial Farm", ["cows", "chickens", "sheep", "cows", "horses"])
print(my_farm)

# To print remaining capacities per animal for Farm
for animal in Farm.animal_capacity:
    print(f"Remaining capacity for {animal}: {my_farm.calculate_remaining_capacity(animal)}")

# Trial with no animals for Farm
empty_farm = Farm("UCL Farm")
print(empty_farm)

# Trial of CityFarm
city_farm = CityFarm("Urban Farm", ["chickens", "sheep", "chickens"])
print(city_farm)
