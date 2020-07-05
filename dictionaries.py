# Chapter 6: Dictionaries

alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])

# adding more key-value pairs
print(alien_0)
alien_0['X'] = 0
alien_0['Y'] = 25
print(alien_0)

# Empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying values
alien_0 = {'color' : 'green'}
print(alien_0)
print("The alien is " + alien_0['color'])
alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color'])

alien_0 = {'X' : 0, 'Y' : 25, 'speed' : 'medium'}
print("Original X position: " + str(alien_0['X']))

# Move alien to the right
if alien_0['speed'] == 'slow':
    incrementX = 1
elif alien_0['speed'] == 'medium':
    incrementX = 2
else:
    incrementX = 3
# New alien position
alien_0['X'] = alien_0['X'] + incrementX
print("New X position: " + str(alien_0['X']))

# Removing key-value pairs
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)

del alien_0['points']
print(alien_0)
del(alien_0['color'])
print(alien_0)

# breakdown dicts and other statements to multiple lines

favLang = {
    'A' : 'python',
    'B' : 'C',
    'C' : 'Perl',
    'D' : 'Perl',
    'E' : 'Julia', # It's recommended to add a comma for the last one too
}
print("E's favorite language is " +
    favLang['A'].title())

# Exercise
candidate1 = {
    'firstName' : 'barack',
    'lastName' : 'obama',
    'city' : 'chicago',
}
print("Candidate one's first name: " + candidate1['firstName'].title())
print("Candidate one's last name: " + candidate1['lastName'].title())
print("Candidate one's city of residence: " + candidate1['city'].title())

glossary = {
    'immutable' : 'unchanging over time or unable to be changed.',
    'function' : 'a unit of code that is defined by its role within a code structure',
    'dictionary' : 'a book that lists the words of a language',
    'interpreter' : 'a program that simplifies a high-level code into a simpler code',
    'nested' : 'a unit of code that is fully contained',
}

print("\nWord:\t\t\tMeaning:")
print("-"*90)
print("Immutable:\t\t" + glossary['immutable'].capitalize())
print("Function:\t\t" + glossary['function'].capitalize())
print("Dictionary:\t\t" + glossary['dictionary'].capitalize())
print("Interpreter:\t\t" + glossary['interpreter'].capitalize())
print("Nested:\t\t\t" + glossary['nested'].capitalize())


# Looping through dictionary

user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


favLang = {
    'A' : 'python',
    'B' : 'c',
    'C' : 'perl',
    'D' : 'perl',
    'E' : 'julia',
}

for name, lang in favLang.items():
    print("\nName: " + name)
    print("Language: " +lang.title())

for name, lang in favLang.items():
    print(name.title() + "'s favorite language is " +
    lang.title())

# loop through just the keys

for name in favLang.keys():
    print("Name: " + name)

# above two lines are equivalent to the following two lines

for name in favLang:
    print("Name: " + name)

for name in favLang:
    print(name.title() + "'s favorite language is " +
    favLang[name].title())

# keys in sorted order

favLang = {
    'p' : 'python',
    'd' : 'c',
    'q' : 'perl',
    'm' : 'perl',
    's' : 'julia',
}

for name in sorted(favLang):
    print(name.title() + "'s favorite language is " +
    favLang[name].title())

print(sorted(favLang))
print(favLang)

# looping through values in a dict
print(sorted(favLang.values()))

for lang in favLang.values():
    print("One of the favorites: " + lang.title())

# set is a 'list' of unique items and we can use sets to weed out duplicates
# from a list of values

print(favLang)
print()
# Set of favorite languages
for lang in set(favLang.values()):
    print(lang.title())
print()
# Sorted set of favorite languages
for lang in sorted(set(favLang.values())):
    print(lang.title())

# Exercise

glossary = {
    'immutable' : 'unchanging over time or unable to be changed.',
    'function' : 'a unit of code that is defined by its role within a code structure',
    'dictionary' : 'a book that lists the words of a language',
    'interpreter' : 'a program that simplifies a high-level code into a simpler code',
    'nested' : 'a unit of code that is fully contained',
}

print("Word:\t\t\tand it's Meaning:")
print("-"*90)
for word, meaning in glossary.items():
    print(word.title() + ":\t\t" + meaning.capitalize())


# List of Dictionaries

alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# fleet of aliens

aliens = []
for alien in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

aliens = []

for alien in range(15):
    aliens.append({'color' : 'green', 'points' : 5, 'speed' : 'slow'})
    aliens.append({'color' : 'yellow', 'points' : 10, 'speed' : 'medium'})
    aliens.append({'color' : 'red', 'points' : 15, 'speed' : 'fast'})

print(aliens)

for alien in aliens:
    print(alien)

print("Total # of aliens: " + str(len(aliens)))

slow = 0
medium = 0
fast = 0
for alien in aliens:
    if alien['speed'] == 'slow':
        slow += 1
    elif alien['speed'] == 'medium':
        medium += 1
    elif alien['speed'] == 'fast':
        fast += 1

print("# of slow aliens: " + str(slow))
print("# of medium aliens: " + str(medium))
print("# of fast aliens: " + str(fast))

count = {'slowAliens' : 0, 'mediumAliens': 0, 'fastAliens' : 0}
for alien in aliens:
    if alien['speed'] == 'slow':
        count['slowAliens'] += 1
    elif alien['speed'] == 'medium':
        count['mediumAliens'] += 1
    elif alien['speed'] == 'fast':
        count['fastAliens'] += 1

print("# of slow aliens: " + str(count['slowAliens']))
print("# of medium aliens: " + str(count['mediumAliens']))
print("# of fast aliens: " + str(count['fastAliens']))


# list in a dictionary

pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'cheese'],
}

print("You ordered a " + pizza['crust'] +
    "-crust pizza with following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


favLangs = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
    'jay' : ['ruby', 'python', 'julia'],
}
for name, langs in favLangs.items():
    print(name.title() + "'s favorite languages: ")
    for lang in langs:
        print("\t" + lang.title())

# avoid nesting beyond the above mentioned example

# nest dictionaries in a dictionary
users = {
    'emusk' : {
        'first' : 'elon',
        'last' : 'musk',
        'location' : 'hawthorne',
    },
    'bgates' : {
        'first' : 'bill',
        'last' : 'gates',
        'location' : 'seattle'
    }
}

for uname, info in users.items():
    print("\n Username: " + uname)
    print("\tFull Name: " + info['first'].title() + " " + info['last'].title())
    print("\tLocation: " + info['location'].title())
