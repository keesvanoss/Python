from helpers import get_countries 

__winc_id__ = '25a8041d2d5e4e3ab61ab1be43bfb863'
__human_name__ = 'dictionaries'

# Part 1, create dict passport

def create_passport(name,date_birth,place_birth,height,nationality):
    passport = {
        'name' : name,
        'date_of_birth': date_birth,
        'place_of_birth': place_birth,
        'height' : height,
        'nationality' : nationality
    }
    return passport

# Part 2, add stamp with visited country to passport

def add_stamp(passport, country):
    home_country = passport.get('nationality')
    visited_countries = passport.get('stamps')

    if visited_countries == None: visited_countries = []
    if country.lower != home_country.lower:
        if country not in visited_countries:
            visited_countries.append(country)
    if visited_countries != []: passport['stamps'] = visited_countries
    return passport

# Part 3, check if person is allowed in country

def check_passport(passport, country, allowed_countries, forbidden_countries):
    if 'stamps' in passport: 
        countries_been = passport.get('stamps')
    else:
        countries_been = []
    allowed = allowed_countries.get(country)
    not_allowed = forbidden_countries.get(country)
    if not_allowed != None:
        for country in not_allowed:
            if country in countries_been:
                return False
    add_stamp(passport,country)
    return passport



# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == '__main__':
    countries = get_countries()

# Test part 1
    new_passport = create_passport('Kees', '1962-05-23', 'Veghel', 1.87, countries[0])

# Test part 2
    print(add_stamp(new_passport,countries[0]))
    print(add_stamp(new_passport,countries[12]))
    print(add_stamp(new_passport,countries[12]))
    print(add_stamp(new_passport,countries[30]))

# Test part 3
    hank = check_passport(new_passport,
               'Netherlands',
               {'Belgium': ['Netherlands']},
               {'Netherlands': ['North Korea']})

    hank = add_stamp(hank, 'North Korea')
    print(check_passport(hank,
               'Netherlands',
               {'Belgium': ['Netherlands']},
               {'Netherlands': ['North Korea']}))