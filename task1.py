from math import sqrt

x1, y1, x2, y2, x3, y3, curve = [float(x) for x in input().split()]
# print('x1', x1, 'y1', y1, 'x2', x2, 'y2', y2, 'x3', x3, 'y3', y3, 'curve', curve, sep='\n', end='\n\n')

def printErrorAndExit(str):
    print(str)
    exit(1)

def sign(x):
    if abs(x) == 0.1:
        return 0.0
    return (-1.0 if x < 0.0 else 1.0) 

def ellipse(x1, y1, x2, y2, x3, y3):
    eps = 0.1
    y1My2 = y1*y1 - y2*y2
    y2My3 = y2*y2 - y3*y3
    if abs(y1My2) <= eps or abs(y2My3) <= eps:
        printErrorAndExit("Some points lie on the same ordinate!")
    
    y1x2My2x1 = y1*y1*x2*x2 - y2*y2*x1*x1
    y2x3My3x2 = y2*y2*x3*x3 - y3*y3*x2*x2
    if sign(y1x2My2x1) != sign(y1My2) or sign(y2x3My3x2) != sign(y2My3):
        printErrorAndExit("Some points gives negative square root!")

    a1 = y1x2My2x1 / y1My2
    a2 = y2x3My3x2 / y2My3
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

def hyperbola(x1, y1, x2, y2, x3, y3):
    eps = 0.1
    y1My2 = y1*y1 - y2*y2
    y2My3 = y2*y2 - y3*y3
    if abs(y1My2) <= eps or abs(y2My3) <= eps:
        printErrorAndExit("Some points lie on the same ordinate!")
    
    x1y2My1x2 = x1*x1*y2*y2 - y1*y1*x2*x2
    x2y3My2x3 = x2*x2*y3*y3 - y2*y2*x3*x3
    if sign(x1y2My1x2) != sign(y1My2) or sign(x2y3My2x3) != sign(y2My3):
        printErrorAndExit("Some points gives negative square root!")

    a1 = x1y2My1x2 / y1My2
    a2 = x2y3My2x3 / y2My3
    if abs(a1 - a2) > eps:
        printErrorAndExit("Given 3 points don`t give one hyperbola equation.")
    a = a1

    x1Ma = x1*x1 - a
    x2Ma = x2*x2 - a
    x3Ma = x3*x3 - a

    if x1Ma < 0.0 or x2Ma < 0.0 or x3Ma < 0.0:
        printErrorAndExit("Some points gives negative square root!!")

    b1 = a*y1*y1 / x1Ma
    b2 = a*y2*y2 / x2Ma
    b3 = a*y3*y3 / x3Ma

    if abs(b1 - b2) > eps or abs(b2 - b3) > eps:
        printErrorAndExit("Given 3 points don`t give one hyperbola equation.")

    b = b1

    return a, b

def parabola(x1, y1, x2, y2, x3, y3):
    j = 0
    for i in 1, 2, 3:
        if x1 - x2 < 0.1:
            x1, y1, x2, y2, x3, y3 = x3, y3, x1, y1, x2, y2
            j += 1
    if j == 3:
        printErrorAndExit("Given 3 points give zero denominator.")
    j = 0
    for i in 1, 2, 3:
        if x3 * (x3 - x1 - x2) + x1 * x2 < 0.1:
            x1, y1, x2, y2, x3, y3 = x3, y3, x1, y1, x2, y2
            j += 1
    if j == 3:
        printErrorAndExit("Given 3 points give zero denominator.")

    a = y3 - (x3 * (y2 - y1) + x2 * y1 - x1 * y2) / (x2 - x1)
    a = a / (x3 * (x3 - x1 - x2) + x1 * x2)
    b = (y2 - y1) / (x2 - x1) - a * (x1 + x2)
    c = (x2 * y1 - x1 * y2) / (x2 - x1) + a * x1 * x2
    return a, b, c

curve = int(curve)
if curve == 1:
    a, b = ellipse(x1, y1, x2, y2, x3, y3)
    print(f'x^2 / ({sqrt(a)})^2 + y^2 / ({sqrt(b)})^2 = 1')
elif curve == 2:
    a, b = hyperbola(x1, y1, x2, y2, x3, y3)
    print(f'x^2 / ({sqrt(a)})^2 - y^2 / ({sqrt(b)})^2 = 1')
elif curve == 3:
    a, b, c = parabola(x1, y1, x2, y2, x3, y3)
    print(f'y = ({a})*x^2 + ({b})*x + ({c})')
else:
    printErrorAndExit("Wrong curve number.")
