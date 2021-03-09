from helpers import random_koala_fact

__winc_id__ = 'c0dc6e00dfac46aab88296601c32669f'
__human_name__ = 'while'

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == '__main__':
    print(random_koala_fact())

# Part 1, create list with unique facts

def unique_koala_facts(nr_of_facts):

  facts_list = []                             # Declare variables
  old_nr = 255

  iterations = 20                             # Stop after repeating 20 times the same nr_of facts
  while nr_of_facts > 0:
    fact = random_koala_fact()                # Get random fact
    if not fact in facts_list:                # Check if fact in unique list
      facts_list.append(fact)                 # If not, append to unique list
      nr_of_facts -= 1                        # Decrement nr of facts
    if old_nr == nr_of_facts:                 # Check for the same nr_of facts
      iterations -= 1                         # Check for 20 times
      if iterations == 0: nr_of_facts = 0     # After 20 times, stop reading facts -> exit
    else:                                     # If new fact
      old_nr = nr_of_facts                    # Save nr of facts
      iterations = 20                         # Reset iterations
  return facts_list                           # Return unique list

# Part 2, count 'joey' in facts after 1 is 10 times repeated

def num_joey_facts():
  fact_list = []
  fact_counters = [0] * 100
  joey_count = 0
  
  while True:
    fact = random_koala_fact()
    if 'joey' in fact.lower():
      joey_count += 1
    if not fact in fact_list:
      fact_list.append(fact)
    ptr = fact_list.index(fact)
    fact_counters[ptr] += 1
    if 10 in fact_counters:
      return joey_count  
    
def koala_weight():
  a = True
  return a

# Test part 1
print(unique_koala_facts(50))

# Test part 2
print(num_joey_facts())
