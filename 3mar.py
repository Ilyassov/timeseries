from math import *
import matplotlib.pyplot as plt

t = 1.384
N = 10000
a, b = 1, 1

v = [(a * cos(i*t), b * sin(i*t)) for i in range(N+1)]

def euc_dist(n1, n2):
    return sqrt((n1[0]-n2[0])*(n1[0]-n2[0]) + (n1[1]-n2[1])*(n1[1]-n2[1]))

def make_slice(v, start, m):
    return v[start:start+m]

def dist(v1, v2, m):
    ans = 0
    for p in range(m):
        ans += euc_dist(v1[p], v2[p])
    return sqrt(ans / m)

dic = {}
for m in range(1, 20):
    false_neig = 0
    for i in range(N+1-m):
        v_i = make_slice(v, i, m)
        min_dists = [dist(v_i, make_slice(v, j, m), m) for j in range(i+1, N+1-m)]
        if min_dists == []:
            continue
        nearest = min(min_dists)
        min_dist_index = i + 1 + min_dists.index(nearest)
        v_j = make_slice(v, min_dist_index, m)
        cur_dist = dist(v_i, v_j, m)
        v_i_next = make_slice(v, i, m+1)
        v_j_next = make_slice(v, min_dist_index, m+1)
        next_dist = dist(v_i_next, v_j_next, m+1)
        false_neig += 1 if (next_dist / cur_dist) > (m/(m+1) * nearest) else 0
    dic[m] = false_neig
    print(false_neig)

G = list(dic.items())
x, y = zip(*G)
plt.plot(x, y)
plt.show()