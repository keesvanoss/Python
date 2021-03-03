# Do not modify these lines
__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'
__human_name__ = 'comments'

# Add your code after this line

conversion_factor = 0.83                # 1 dollar = 0,83 Euro
dollar_count = 300			# Amount of dollars

"""The conversion starts here
and calculates the value of Dollars in Euros """

value_in_euros = dollar_count * conversion_factor

""" Print routine
After conversion the result is printed """

print (round( value_in_euros,2))
