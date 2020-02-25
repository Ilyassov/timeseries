from math import *

t = 100 #10, 100, 1000
N = 1000
a, b = 1, 1

x = [cos(j/t) for j in range(N*t+1)]
y = [sin(j/t) for j in range(N*t+1)]
# x = [a * cos(j/t) for j in range(N*t+1)]
# y = [b * sin(j/t) for j in range(N*t+1)]

def func_x(a, t):
    return a * cos(t)
def func_y(b, t):
    return b * sin(t)
def teta(z):
    return (0 if z < 0 else 1)
def euc_dist(x1, y1, x2, y2):
    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def dist(k, n1, n2):
    ans = 0.0
    for i in range(1, k+1):
        index1 = n1 - k - i
        index2 = n2 - k - i
        if index1 < 0 or index2 < 0:
            break
        cur_euc_dist = euc_dist(x[index1], y[index1], x[index2], y[index2])
        ans += cur_euc_dist * cur_euc_dist
    return sqrt(ans)

def c_k_l(k, l):
    ans = 0.0
    for i in range(1, N+1):
        for j in range(1, N+1):
            ans += teta(l - dist(k, i, j))
    return ans / (N*N)

k = 10
prev = log(c_k_l(k, 0.5)) / log(0.5)
print(prev)
cur = log(c_k_l(k, 0.25)) / log(0.25)
print(cur)
step = 8
while step > 0.001 and abs(prev-cur) > 0.05:
    prev = cur
    l = 1.0 / step
    cur = log(c_k_l(k, l)) / log(l)
    print(cur)
    step *= 2