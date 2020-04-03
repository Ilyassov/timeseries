from math import sqrt
from math import sin
from math import cos
from math import log

t = 100
N = 1000
l = 0.5
k = 30
ck = 1e+9
a, b = 1, 1

x = [cos(j/t) for j in range(N+1)]
y = [sin(j/t) for j in range(N+1)]

def euc_dist(x1, y1, x2, y2):
    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def dist(x1, y1, x2, y2, k):
    ans = 0.0
    for i in range(k):
        ans += euc_dist(x1[i], y1[i], x2[i], y2[i])
    return ans

def c_k_l(k, l):
    sqr_l = l*l
    ans = 0.0
    for i in range(N-k):
        for j in range(N-k):
            ans += 2*(sqr_l >= dist(x[i:i+k], y[i:i+k], x[j:j+k], y[j:j+k], k))
    return ans / (N*N)

for cur_k in range(1, k):
    ckl = c_k_l(cur_k, l)
    dc = log(ckl) / log(l)
    print('ckl\t', ckl)
    if abs(ck - dc) <= 0.05:
        print('Answer:\t', ckl, dc, cur_k)
        exit()
    else:
        ck = dc
