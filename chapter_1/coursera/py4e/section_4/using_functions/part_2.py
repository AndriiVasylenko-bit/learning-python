# dysfunctional code
x = 5
print('Hello')

def print_lyrics():
    print("I'm a Andrii, and I'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')
x = x + 2
print(x)



# functional code
x = 5
print('Hello')

def print_lyrics():
    print("I'm a Andrii, and I'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')
print_lyrics()
x = x + 2
print(x)



# Argument.
big = max('Hello world!')
print(big)



# Prarmaters.
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')
greet('es')
greet('fr')



# Return Valuse
def greet():
    return "Hello"

print(greet(), 'Glenn')
print(greet(), 'Sofia')



# Return value 2
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')
