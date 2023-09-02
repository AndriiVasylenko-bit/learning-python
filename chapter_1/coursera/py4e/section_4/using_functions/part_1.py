# user functions
def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()



# main functions
big = max('Hello world')
print(big)

tiny = min('Hello world') #маленький
print(tiny)



# Type Conversions
print(float(99) / 100)

i = 42
print(type(i))
f = float(i)
print(f)
print(type(f))
print(1 + 2 * float(3) / 4 - 5)



# Type Conversions 2
sval = '123'
print(type(sval))
try:
    print(sval + 1)
except:
    print('TypeError: can only concatenate str (not "int") to str')

ival = int(sval)
print(type(ival))
print(ival + 1)

nsv = 'hello bob'
niv = int(nsv)



