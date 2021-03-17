# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

# Part 1, print the Zen of Python
import this, time, math, sys, greet
from datetime import datetime

# Part 2, wait <second> sec.
def wait(seconds):
    time.sleep(seconds)
    return 

# Part 3, return sine
def my_sin(SineValue):
    return(math.sin(SineValue))

# Part 4, return date in ISO format
def iso_now():
    my_date = datetime.now()
    return(my_date.isoformat()[:16])

# Part 5, return platform
def platform():
    return(sys.platform)

# Part 6, return string from greet.py
def supergreeting_wrapper(name):
    return(greet.supergreeting(name))

# Test part 2
wait(2)

# Test part 3
print(my_sin(math.pi/2))

# Test part 4
print(iso_now())

# Test part 5
print(platform())

# Test part 6
print(supergreeting_wrapper('Kees'))