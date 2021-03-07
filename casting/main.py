# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# Part 1

leek_price = 2
price = 'Leek is ' + str(leek_price) + ' euro per kilo.'
print (price)

# Part 2

order = 'leek 4'
x=order.find(' ')+1
leek_number=order[x:]

leek_number=int(leek_number)
sum_total = leek_number * leek_price
print (sum_total)

# Part 3

broccoli_price = 2.34
order = 'broccoli 1.6'
x = order.find(' ')+1
broccoli_number = order[x:]

broccoli_number = float(broccoli_number)
total_price = broccoli_number * broccoli_price
print (str(broccoli_number) + 'kg broccoli costs ' + str(round(total_price,2)) + 'e')
