import math

def solver(a, b, c):
    if a == 0:
        return
    else:
        print(f"\nEquation is: {a}x^2 + ({b}x) + ({c}) = 0")
        Discriminant = b**2 - 4 * a * c
        if Discriminant < 0 :
            print('There are 0 roots')
            pass
        else:
            discriminant = math.sqrt(Discriminant)
            result1 = (-b + discriminant) / 2 * a
            result2 = (-b - discriminant) / 2 * a
            if result1 == result2:
                print("There are 1 roots\nx = {}".format(result1))
                return result1
            else:
                print("There are 2 roots\nx1 = {},\nx2 = {}".format(result1,result2))
                return result1 ,result2




while True:
    try:
        a = float(input('Enter a: '))  
        b = float(input('Enter b: '))  
        c = float(input('Enter c: '))  
        solver(a,b,c)
        break
    except ValueError:
        print("Error. Expected a valid real number, got {} instead".format("unfixed bag :("))



