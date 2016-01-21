"""
Prints out all the melons in our inventory
"""

#imports attribute-specific dictionaries from melons.py
from melons_edited import melons

def print_melon_info():
    for melon in melons.keys():
        if melons[melon]['Seedless'] == True:
            seedless = 'Yes'
        else:
            seedless = 'No'
        print ("{}: Costs ${:.2f}. Weighs {}. Seedless: {}." 
            "Color inside is typically {}; rind is typically {}.".format(
                    melon, 
                    melons[melon]["Price"], 
                    melons[melon]["Average Weight"], 
                    seedless,                   
                    melons[melon]["Flesh Color"], 
                    melons[melon]["Rind Color"]
                    ))


print_melon_info()
