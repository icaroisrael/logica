z = 10
def soma(a, b, c):
    if(c == 1):
        return a * b
    elif(c == 2):
        return a / b
    elif(c == 3):
        return a + b
    elif(c == 4):
        return a - b
    else: 
        return "Coloque um valor de 1 a 4"
z = soma(2,3,1)
print(z)