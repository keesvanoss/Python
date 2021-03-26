__winc_id__ = '9920545368b24a06babf1b57cee44171'
__human_name__ = 'refactoring'

# Define parent- and child classes

specialist_list = {}

class specialist():
  def __init__(self, name, profession):
    self.name = name
    self.profession = profession
    if profession in specialist_list.keys():
      specialist_list[profession].append(name)
    else:
      specialist_list[profession] = [name]

class electrician(specialist):
  pass

class painter(specialist):
  pass

class plumber(specialist):
  pass

class homeowner():
  def __init__(self, name, address, needs):
    self.name = name 
    self.address = address
    self.needs = needs
    
  def contracts(self):
      newlist = []
      for item in self.needs:
        newlist += specialist_list[item]
      return newlist

  def add_needs(self, specialist):
    self.needs.append(specialist)

# Define specialists

alice = specialist('Alice Aliceville', 'electrician')
bob = specialist('Bob Bobsville', 'painter')
craig = specialist('Craig Craigsville', 'plumber')

# Define homeowners

alfred = homeowner('Alfred Alfredson', 'Alfredslane 123', ['painter', 'plumber'])
bert = homeowner('Bert Bertson', 'Bertslane 231', ['plumber'])
candice = homeowner('Candice Candicedottir', 'Candicelane 312', ['electrician', 'painter'])

# Print homeowners contracts

print(f"Alfred's contracts: {alfred.contracts()}")
print(f"Bert's contracts: {bert.contracts()}")
print(f"Candice's contracts: {candice.contracts()}")
