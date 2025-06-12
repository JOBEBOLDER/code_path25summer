'''
Problem 1: Most Endangered Species
Imagine you are working on a wildlife conservation database. 
Write a function named most_endangered() that returns the species with the 
highest conservation priority based on its population.

The function should take in a list of dictionaries named species_list as a parameter. Each dictionary represents data associated with a species, including its name, habitat, and wild population. The function should return the name of the species with the lowest population.

If there are multiple species with the lowest population, return the species with the lowest index.

def most_endangered(species_list):
    pass
Example Usage:

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))
Example Output:

Vaquita

'''

# Function to find the most endangered species based on population
def most_endangered(species_list):
    #base case
    if not species_list:
        return None
    min_value = float('inf')
    endangered_species = None
    #to access the value in the dictionary, and compare each value, to find the min value
    for species in species_list:
        if species['population'] < min_value:
            min_value = species['population']
            endangered_species = species['name']
        else:
            return None
    return endangered_species
    
        
species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))

#problem2:

def count_endangered_species(endangered_species, observed_species):
    #base case:
    if endangered_species is None or observed_species is None:
        return None
    
    count = 0
    set1 = set(endangered_species)

    for species in observed_species:
        if species in set1:
            count += 1

    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  