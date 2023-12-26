# homework - calculator
# in python
def addition(x : float, y : float):
    result = x + y
    
    return(result) 


def subtraction(x : float, y : float):
    result = x - y
    
    return(result)


def multiplication(x : float, y : float):
    result = x * y
    
    return(result)


def division(x : float, y : float): 
    if y != 0: 
        result = x / y
        return(result)
    else: raise ValueError('This operation is not supported for given input parameters')


def modulo(x : float, y : float):
    if x >= y and y > 0:
        result = x % y
        return(result)
    else: raise ValueError('This operation is not supported for given input parameters')    



def secondPower(x : float):
    result = x**2
    
    return(result)



def power(x : float, y : float):
    if y >= 0:    
        result = x ** y
        return(float(result))
    else: raise ValueError('This operation is not supported for given input parameters')



def secondRadix(x : int):
    if x > 0:
        result = x ** (1/2)
        return(result)
    else: raise ValueError('This operation is not supported for given input parameters')


def magic(x : float, y : float, z : float, k : float):
    l = x + k
    m = y + z
    if m !=0:
        n = ((l / m) + 1)
        return(n)
    else: raise ValueError('This operation is not supported for given input parameters')



def control(a : str, x : float, y : float, z : float, k : float):
    if   a == "ADDITION":
        return addition(x,y)
    elif a == "SUBTRACTION":
        return subtraction(x,y)
    elif a == "MULTIPLICATION":
        return multiplication(x,y)
    elif a == "DIVISION":
        return division(x,y)
    elif a == "MOD":
        return modulo(x,y)
    elif a == "POWER":
        return power(x,y)
    elif a == "SECONDRADIX":
        return secondRadix(x)
    elif a == "MAGIC":
        return magic(x,y,z,k)
    else: raise ValueError('This operation is not supported for given input parameters')


    



