# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

class Player:   # Part 1.1
    
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy
        if (0.0 < speed < 1.0) and (0.0 < endurance < 1.0) and (0.0 < accuracy < 1.0):   # Part 1.2
            pass
        else:
            raise ValueError("ValueError exception thrown")
   
    def introduce(self):
        return f'Hello everyone, my name is {self.name}.'   # Part 1.3

    def strength(self):     # Part 1.4
        attNames = ['speed', 'endurance', 'accuracy']
        attValues = [self.speed, self.endurance, self.accuracy]
        maximum = max(attValues)
        pointer = attValues.index(maximum)
        return (attNames[pointer], maximum)  


class Commentator:      # Part 2.1

    def __init__(self, name):          
        self.name = name  # Part 2.2
        
    def sum_player(self, player):   # Part 2.3
        return getattr(player, 'speed') + getattr(player, 'endurance') + getattr(player, 'accuracy')

    def compare_players(self, player1, player2, attribute):    # Part 2.4
        if getattr(player1, attribute) > getattr(player2, attribute): return getattr(player1, 'name')
        if getattr(player1, attribute) < getattr(player2, attribute): return getattr(player2, 'name')
        
        if player1.strength()[1] > player2.strength()[1]: return getattr(player1, 'name')
        if player1.strength()[1] < player2.strength()[1]: return getattr(player2, 'name')

        if self.sum_player(player1) > self.sum_player(player2): return getattr(player1, 'name')
        if self.sum_player(player1) < self.sum_player(player2): return getattr(player2, 'name')

        return 'These two players might as well be twins!'

# Test part 1.1 + 1.2
Jan = Player('Jan',0.2,0.5,0.5)

# Test part 1.3
print(Jan.introduce())

# Test part 1.4
print(Jan.strength())

# Test part 2.1 + 2.2
ray = Commentator('Ray Hudson')
print(ray.name)

# Test part 2.3
print(ray.sum_player(Jan))

# Test part 2.4
alice = Player('Alice', 0.8, 0.2, 0.6)
bob = Player('Bob', 0.9, 0.2, 0.6)
print(ray.compare(alice, bob, 'speed'))