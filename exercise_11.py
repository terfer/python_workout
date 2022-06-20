PEOPLE = [{'first':'Reuven', 'last':'Lerner',
    'email':'reuven@lerner.co.il'},
 {'first':'Donald', 'last':'Trump',
    'email':'president@whitehouse.gov'},
 {'first':'Vladimir', 'last':'Putin',
    'email':'president@kremvax.ru'}
 ]

def key_first(contacts : dict) -> str:
    return contacts['last'], contacts['first']

def alphabetize_names(list_contacts : list) -> list:
    return sorted(list_contacts, key = key_first)

print(alphabetize_names(PEOPLE))