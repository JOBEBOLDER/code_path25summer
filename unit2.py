'''
input: dict
out: string

edges:
1. same value ->
2. empty dict
3.
implementation:
#basecase
min_value = max
minvalue_name = 

time: On
space: On
'''

def most_endangered(species_list):
    #base case:
    if not species_list:
        return None
    
    min_value = float('inf')
    minvalue_name = ""

    #do the for loop 
    for species in species_list:
        if species["population"] < min_value:
            min_value = species['population']
            minvalue_name = species['name']
    return minvalue_name

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 10
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))

#problem 4:
'''
input: 2 lists: unique
output: list->result=[]

implementation:
-1. create result to store the result
2.use the COunter calculate all the species
3. we can priority the species in  Counter.items base on the priority_species
4.extend the species to the 
'''