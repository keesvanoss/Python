# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

# statement 1

switzerland_language_spoken = 'Swiss German' 
spain_language_spoken = 'Castilian Spanish'
print(switzerland_language_spoken == spain_language_spoken)

# statement 2

switzerland_most_prevalent_religion = 'Roman Catholic'
spain_most_prevalent_religion = 'Roman Catholic'
print(switzerland_most_prevalent_religion == spain_most_prevalent_religion)

# statement 3

switzerland_namelen_capital = len('Bern')
spain_namelen_capital = len('Madrid')
print(spain_namelen_capital != switzerland_namelen_capital)

# statement 4

switzerland_GDP = 580 * 10**9
spain_GDP = 1778 * 10**12
print(switzerland_GDP > spain_GDP)

# statement 5

switzerland_population_growth = 0.66
spain_population_growth = 0.67
print((switzerland_population_growth < 1) and (spain_population_growth < 1))

# statement 6

switzerland_population_count = 8.4 * 10**6
spain_population_count = 50 * 10**6
count = [switzerland_population_count > 10**6,spain_population_count > 10**6]
print(any(count))

# statement 7

print ((switzerland_population_count > 10 * 10**6) != (spain_population_count > 10 * 10**6))
 
