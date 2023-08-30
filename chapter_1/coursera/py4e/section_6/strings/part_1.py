# String Data Type
str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)
str3 = '123'
try:
    str3 = str3 + 1
except:
    print('TypeError: can only concatenate str (not "int") to str')
x = int(str3) + 1
print(x)



# Reading and Converting
name = input('Enter: ')
print(name)
apple = input('Enter: ')
try:
    x = apple - 10
except:
    print("TypeError: unsupported operand type(s) for -: 'str' and 'int'")
x = int(apple) - 10
print(x)



#Looking Inside Strings/Внутренний взгляд на струны
fruit = 'banana'
letter = fruit[1]
print(letter)
x = 3
w = fruit[x - 1]
print(w)

