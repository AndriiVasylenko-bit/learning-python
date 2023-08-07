x = 2
x = x + 2
print(x)

# region Badly.
x1q3z9ocd = 35.0
x1q3z9afd = 12.50
xlq3p9afd = x1q3z9ocd * x1q3z9afd
print(xlq3p9afd)
# endregion

# region Good.
a = 35.0
b = 12.50
c = a * b
print(c)
# endregion

# region Mnemonic.
hours = 35.0
rate = 12
pay = hour * rate
print(pay)
# endregion

# region incriment.
x = 0.6
x = 3.9 * x * (1-x)
print(x)
# endregion

xx = 2
xx = xx + 2
print(xx)

yy = 440 * 12
print(yy)

zz = yy / 1000
print(zz)

jj = 23
kk = jj % 5 # Remainder.
print(kk)
print(4 ** 3) # Power.

# Order of evaluation.
x = 1 + (2*3)-(4/(5**6))

# What does "Type" Mean?
ddd = 1+4
print(ddd)
eee = 'hello ' + 'there'
print(eee)
# eee = eee + 1 # Python losst.
print(type(eee))
print(type('hello'))
print(type(1))
xx = 1
print(type(xx))
temp = 98.6
print(type(temp))
print(type(1))
print(type(1.0))

# Type Conversions.
print(float(99)+100)
i = 42
print(type(i))
f = float(i)
print(f)
print(type(f))
sval = '123'
print(type(sval))
# # print(sval + 1) # Python losst.
ival = int(sval)
print(ival + 1)

nsv = 'hello bob'
niv = int(nsv) # Python losst.

# Division was different.
print(10/2)
print(9/2)
print(99/100)
print(10.0/2.0)
print(99.0/100.0)

# User Input.
nam = input('Who are you?')
print('Welcome', nam)