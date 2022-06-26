import math

def f(n):
    return n/math.factorial(n)**(1/n)

acc = 0.001
i = 2
while f(i) - f(i-1) > acc:
    i = i + 1
print(f(i))