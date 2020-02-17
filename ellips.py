x1, y1, x2, y2, x3, y3, curve = [float(x) for x in input().split()]
print('x1', x1, 'y1', y1, 'x2', x2, 'y2', y2, 'x3', x3, 'y3', y3, 'curve', curve, sep='\n', end='\n\n')

def printErrorAndExit(str):
    print(str)
    exit(1)

def sign(x):
    if abs(x) == 0.1:
        return 0.0
    return (-1.0 if x < 0.0 else 1.0) 

def check(x1, y1, x2, y2, x3, y3):
    eps = 0.1
    y1My2 = y1*y1 - y2*y2
    y2My3 = y2*y2 - y3*y3
    if abs(y1My2) <= eps or abs(y2My3) <= eps:
        print(y1My2)
        print(y2My3)
        printErrorAndExit("Some points lie on the same ordinate!")
    
    y1x2My2x1 = y1*y1*x2*x2 - y2*y2*x1*x1
    y2x3My3x2 = y2*y2*x3*x3 - y3*y3*x2*x2
    print(y1x2My2x1)
    print(y2x3My3x2)
    if sign(y1x2My2x1) != sign(y1My2) or sign(y2x3My3x2) != sign(y2My3):
        printErrorAndExit("Some points gives negative square root!")

    a1 = y1x2My2x1 / y1My2
    a2 = y2x3My3x2 / y2My3
    print(f'a1 {a1}\na2 {a2}')
    if abs(a1 - a2) > eps:
        printErrorAndExit("Given 3 points don`t give one ellipse equation.")
    a = a1

    aMx1 = a - x1*x1
    aMx2 = a - x2*x2
    aMx3 = a - x3*x3

    if aMx1 < 0.0 or aMx2 < 0.0 or aMx3 < 0.0:
        printErrorAndExit("Some points gives negative square root!!")

    b1 = a*y1*y1 / aMx1
    b2 = a*y2*y2 / aMx2
    b3 = a*y3*y3 / aMx3

    if abs(b1 - b2) > eps or abs(b2 - b3) > eps:
        printErrorAndExit("Given 3 points don`t give one ellipse equation.")

    b = b1

    return a, b


a, b = check(x1, y1, x2, y2, x3, y3)
print(f'a*a = {a}, b*b = {b}')