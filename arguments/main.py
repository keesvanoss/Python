# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#------------------------------------------------------------------------
# Part 1, replace part of default template argument
#------------------------------------------------------------------------

def greet(name, template = 'Hello, <name>!'):
    template = template[:template.find('<name>')] + name + template[template.find('!'):]
    return template

#------------------------------------------------------------------------
# Part 2, calculate gravityforce
#------------------------------------------------------------------------

def force( mass = 0, body = 'earth'):
    planets = {
        'sun'     : 274.0,
        'jupiter' : 24.9,
        'neptune' : 11.2,
        'saturn'  : 10.4,
        'earth'   : 9.8,
        'uranus'  : 8.9,
        'venus'   : 8.9,
        'mars'    : 3.7,
        'mercury' : 3.7,
        'moon'    : 1.6,
        'pluto'   : 0.6
    } 
    gravity = planets.get(body)
    return mass * gravity

#------------------------------------------------------------------------
# Part 3, calculate pullforce
#------------------------------------------------------------------------

def pull(m1, m2, d):
    G = 6.674 * 10**-11
    pull = G * ((m1 * m2) / d**2)
    return pull

#------------------------------------------------------------------------

# Test part 1
print(greet('Kees'))

# Test part 2
print(force(mass = 10, body ='moon'))

# Test part 3
print(pull(800, 1500, 3))