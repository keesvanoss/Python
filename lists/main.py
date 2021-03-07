# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# Part 1 bubblesort list

def alphabetical_order(film_names):
  # We go through the list as many times as there are elements
  for i in range(len(film_names)):
    # We want the last pair of adjacent elements to be (n-2, n-1)
    for j in range(len(film_names) - 1):
      if film_names[j] > film_names[j+1]:
        # Swap
        film_names[j], film_names[j+1] = film_names[j+1], film_names[j] 
  return film_names

# Part 2 check if film has won Golden Globe

def won_golden_globe(film_name):
  awards_won = ['Jaws','Star Wars: Episode IV – A New Hope', \
                'E.T. the Extra-Terrestrial','Memoirs of a Geisha']
  awards_won = [x.lower() for x in awards_won]
  film_name_lower = film_name.lower()
  Check_won = film_name_lower in awards_won  
  return Check_won

# Part 3 remove Toto album names from mixed Filn names/Toto albums list

def remove_toto_albums(mixed_strings):
  toto_albums = ['Fahrenheit','The Seventh One','Toto XX','Falling in Between', \
                 '35th Anniversary','Toto XIV','Old Is New', \
                 '40 Tours Around the Sun - Live in Holland']
  for album_name in toto_albums:
    if album_name in mixed_strings:
      mixed_strings.remove(album_name) 
  return mixed_strings

# Test part 1
test = ['Jaws','35th Anniversary','Star Wars: Episode IV – A New Hope', \
        'E.T. the Extra-Terrestrial','Old Is New','Memoirs of a Geisha']
print (alphabetical_order(test))

# Test part 2
test = ['Jaws','35th Anniversary','Star Wars: Episode IV – A New Hope', \
        'E.T. the Extra-Terrestrial','Old Is New','Memoirs of a Geisha']
print (won_golden_globe('jaws'))

# Test part 3
test = ['Jaws','35th Anniversary','Star Wars: Episode IV – A New Hope', \
        'E.T. the Extra-Terrestrial','Old Is New','Memoirs of a Geisha']
print (remove_toto_albums(test))