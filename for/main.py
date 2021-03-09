from helpers import get_countries
countries = get_countries()


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


""" Write your functions here. """

# Part 1 list with shortest named countries

def shortest_names(country_names):
  shortest_len = 255			# define variables

  for country in country_names:		# get shortest len
    if len(country) < shortest_len:
      shortest_len = len(country)  
  shortest_name=[]

  for country in country_names:		# generate namelist
    if len(country) == shortest_len:
      shortest_name.append(country)

  return shortest_name

# Part 2 top three most vowels

def most_vowels(country_names):

  max_vowels = []

  for country in country_names:		# get shortest len
    tot_vowels = 0
    for letter in country.lower():
      if letter in 'aeiou':
        tot_vowels += 1
    max_vowels.append(tot_vowels)
    
  # Bubble sort
  for i in range(len(max_vowels)):
    # We want the last pair of adjacent elements to be (n-2, n-1)
    for j in range(len(max_vowels) - 1):
      if max_vowels[j] < max_vowels[j+1]:
        # Swap
        max_vowels[j], max_vowels[j+1] = max_vowels[j+1], max_vowels[j] 
        country_names[j], country_names[j+1] = country_names[j+1], country_names[j]
  
  return country_names[0:3]

# Part 3 Alphabeth from country letters

def alphabet_set(countries):

  alphabet = []                                     # Declare variables
  country_list = []

  for ptr in range(0 , len(countries) , 2):            # Loop trough country list
    country_add_flag = False                        # Reset add country to list flag
    for letter in countries[ptr].lower():           # Check letters in country name
      if not letter in alphabet:                    # If letter not in alphabet list
        if letter in 'abcdefghijklmnopqrstuvwxyz':  # Check for legal letter
          country_add_flag = True                   # If ok, add country to list
          alphabet.append(letter)                   # Add letter to alphabet list
          if len(alphabet) == 26:                   # Check if alphabet list complete
            print ('The list contains ' + str(len(country_list)) + ' entries')
            return (country_list)              # If so, return number of countries in list
    if country_add_flag == True:                    # Check if country must be added to country list
      country_list.append(countries[ptr])           # Add country to list
  return False                                      # If alphabet not in country list, return false

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()

    """ Write the calls to your functions here. """

# Test part 1
print ('--------------------------------------------------')
print ('Test 1, display list with shortest name countries')
print ('--------------------------------------------------')
print (shortest_names(countries))

# Test part 2
print ('\n----------------------------------------------------------')
print ('Test 2, display list with 3 countries with most vowels')
print ('----------------------------------------------------------')
print (most_vowels(countries))

# Test part 3
print ('\n-------------------------------------------------------------------------')
print ('Test 3, display list with countries containing all letters in alphabet')
print ('-------------------------------------------------------------------------')
print (alphabet_set(countries))
