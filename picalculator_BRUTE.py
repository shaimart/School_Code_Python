import math
def newtonPi(init:float)->float:
    

    x_k = init
    while True:
        a = math.sin(x_k)
        b = math.cos(x_k)
        c = a / b
        x_k_1 = x_k - c
        if x_k_1 == x_k:
            return(x_k_1)
        x_k = x_k_1


print(newtonPi(3.0))
print(newtonPi(3))
# print(newtonPi("a"))
print(newtonPi(-3.0))

def leibnizPi(iterations: int)->float:
    sum = 0
    for i in range (iterations):
        sum += (4 * (-1) ** i) / (2 * i + 1)
    return sum


def nilakanthaPi(iterations: int)->float:
    sum = 3
    for i in range (1,iterations):
        sum += (4 * (-1) ** (i + 1) / (2 * i * (2*i + 1) * (2*i + 2)))
    return sum 

   
