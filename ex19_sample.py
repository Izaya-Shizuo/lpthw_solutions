def factorial(x):
        if x == 0:
                return 1
        else:
                return x*factorial(x-1)

print factorial(3)
y = 3
print factorial(y)
print factorial(2+1)
print factorial(3*1)
print factorial(3/1)
print factorial(y*1)
print factorial(y+2)
print factorial(y/1)
z = 2
print factorial(y+z)
print factorial(y*z)
