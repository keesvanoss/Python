from helpers import random_koala_fact

__winc_id__ = 'c0dc6e00dfac46aab88296601c32669f'
__human_name__ = 'while'

# Part 1, create list with unique facts

def unique_koala_facts(nr_of_facts):

  facts_list = []                             # Unique facts list
  old_nr = 255                                # Remember nr of facts of facts for iteration check
  iterations = 200                            # Stop after repeating 200 times the same nr of facts
  
  while nr_of_facts > 0:
    fact = random_koala_fact()                # Get random fact
    if fact not in facts_list:                # Check if fact in unique list
      facts_list.append(fact)                 # If not, append to unique list
      nr_of_facts -= 1                        # Decrement nr of facts
    if old_nr == nr_of_facts:                 # Check for the same nr of facts
      iterations -= 1                         # Check for 200 times
      if iterations == 0: nr_of_facts = 0     # After 200 times, stop reading facts -> exit
    else:                                     # If new fact
      old_nr = nr_of_facts                    # Save nr of facts
      iterations = 200                        # Reset iterations
  return facts_list                           # Return unique list

# Part 2, count 'joey' in facts after 1 is 10 times repeated

def num_joey_facts():
  facts_list = []                             # Unique facts list
  fact_counters = [0] * 10                    # Counters how many times fact is read
  
  while True:                                 # Endless loop
    fact = random_koala_fact()                # Get random fact
    if 'joey' in fact.lower():                # Check if 'joey in fact
      if fact not in facts_list:              # If so, check if fact in unique list
        facts_list.append(fact)               # If not, append to unique list
      ptr = facts_list.index(fact)            # Get index to fact
      fact_counters[ptr] += 1                 # Increment facts counter
      if 10 in fact_counters:                 # If a fact repeated 10 times
        return len(facts_list)                # Exit and return number of unique facts with 'joey'

# Part 3, find weight koala in kg in facts

def koala_weight():
  while True:                                 # Endless loop
    fact = random_koala_fact()                # Get fact
    if ('weigh' in fact.lower()) and \
       ('kg' in fact.lower()):                # Check if 'weigh' ad 'kg' in fact 
      ptr1 = fact.lower().find('kg')          # Get index to 'kg'
      ptr2 = ptr1                             # Set start index number
      while fact[ptr2-1] != ' ':              # Point back until space
        ptr2 -= 1
      return int(fact[ptr2:ptr1])             # Return weight in kg as integer

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == '__main__':
    print(random_koala_fact())

# Test part 1
    print ('\n-------------------------------------------------------------------------------------')
    result = unique_koala_facts(50)
    print (result)
    print (len(result))

# Test part 2
    print ('\n-------------------------------------------------------------------------------------')
    print(num_joey_facts())

# Test part 3
    print ('\n-------------------------------------------------------------------------------------')
    print(koala_weight())