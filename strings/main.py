# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1

example_0 = 'Ruud Gullit'
example_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = example_0 + ' ' + str(goal_0 ) + ', ' + example_1 + ' ' +  str(goal_1 )
 
report = f'{example_0 } scored in the {goal_0}nd minute\n{example_1} scored in the {goal_1}th minute'

# Part 2

player = 'Arnold Muhren'
x1 = player.find(' ') 
first_name = player[:x1]
last_name = player[x1+1:]

name_short = player[0] + ". " + last_name

chant_text = first_name + '! '
chant_times = len(first_name)
chant = chant_text * chant_times
chant = chant[:-1]

good_chant = chant[-1] != ' '

