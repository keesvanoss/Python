
from helpers import get_countries

""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


# Part 1 Return list with shortest named countries

def shortest_names(country_names):
    shortest_len = 255                     # Init value
    shortest_name = []                     # Clear shortest name list

    for country in country_names:          # Loop through country list
        if len(country) < shortest_len:    # Check if country name has short name
            shortest_len = len(country)    # If so, remember shortest number

    for country in country_names:          # Loop through country list
        if len(country) == shortest_len:   # Check if country name is shortest
            shortest_name.append(country)  # If so, append to list

    return shortest_name                   # Return list with shortest country names


# Part 2 top three most vowels

def most_vowels(country_names):

    max_vowels = []                        # Clear nr of vowels list

    for country in country_names:          # Loop through country list
        tot_vowels = 0                     # Reset vowel counter
        for letter in country.lower():     # Check every letter in countryname
            if letter in 'aeiou':          # Check if vowel
                tot_vowels += 1            # If so, increment vowel counter
        max_vowels.append(tot_vowels)      # Add nr of vowels to list

    # Bubble sort, sort nr of vowels list and corresponding country list
    for i in range(len(max_vowels)):
        for j in range(len(max_vowels) - 1):
            if max_vowels[j] < max_vowels[j+1]:
                max_vowels[j], max_vowels[j+1] = max_vowels[j+1], max_vowels[j] 
                country_names[j], country_names[j+1] = country_names[j+1], country_names[j]

    return country_names[0:3]              # Return first 3 country names with most vowels


# Part 3 Alphabeth from country letters

def alphabet_set(countries):

    alphabet = []                                           # Declare variables
    country_list = []

    for ptr in range(0, len(countries), 2):                 # Loop trough country list
        country_add_flag = False                            # Reset add country to list flag
        for letter in countries[ptr].lower():               # Check letters in country name
            if letter not in alphabet:                      # If letter not in alphabet list
                if letter in 'abcdefghijklmnopqrstuvwxyz':  # Check for legal letter
                    country_add_flag = True                 # If ok, add country to list
                    alphabet.append(letter)                 # Add letter to alphabet list
        if country_add_flag is True:                        # Check if country must be added to country list
            country_list.append(countries[ptr])             # Add country to list
        if len(alphabet) == 26:                             # Check if alphabet list complete
            return (country_list)                           # If so, return number of countries in list
    return country_list                                     # If alphabet not in country list, return false

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`


if __name__ == '__main__':
    countries = get_countries()

# Test part 1
    print('--------------------------------------------------')
    print('Test 1, display list with shortest name countries')
    print('--------------------------------------------------')
    print(shortest_names(countries))

# Test part 2
    print('\n----------------------------------------------------------')
    print('Test 2, display list with 3 countries with most vowels')
    print('----------------------------------------------------------')
    print(most_vowels(countries))

# Test part 3
    print('\n-------------------------------------------------------------------------')
    print('Test 3, display list with countries containing all letters in alphabet')
    print('-------------------------------------------------------------------------')
    result = alphabet_set(countries)
    print(result)
    print('The list contains ' + str(len(result)) + ' entries')            