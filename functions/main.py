# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

# Exercise 1

def greet(text):
	greet = 'Hello, ' + text + '!'
	return greet

print(greet ('Bob'))

# Exercise 2

def add(a,b,c):
	add = a + b + c
	return add

print (add(5,3,2))

# Exercise 3

def positive(number):
	positive = number > 0
	return positive

print (positive(50))
print (positive(-50))
print (positive(0))

# Exercise 4

def negative(number):
	negative = number < 0
	return negative

print (negative(50))
print (negative(-50))
print (negative(0))
