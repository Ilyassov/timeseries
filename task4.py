from math import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Чтение исходных данных
Data = pd.read_csv('usd_kzt.csv', encoding = 'UTF-8', delimiter = ',')
Data = Data.drop(['USD_quant'], axis = 1)

# Формирование последовательностей данных
date_series = Data['Date'].values
usd_series = Data['USD'].values

# Определение числа задержек
N = len(usd_series)
tau = (N + 1) // 4
n = N - tau

# 1. Преобразование одномерного ряда в многомерный
X = [usd_series[i: N - tau + i] for i in range(tau)]
X = np.array(X)

# 2. Построение для матрицы X соответствующей ковариационной матрицы
C = X.dot(X.T) / n

# 3. Определение собственных значений и собственных векторов матрицы C
Lambda, V = np.linalg.eig(C)

# 4. Переход к главным компонентам
Y = V.T.dot(X)

# 5. SSA–сглаживание
r = 20
V_r = V[:,:r]
Y_r = V.T.dot(X)[:r,]
new_X = V_r.dot(Y_r)
def new_series(s):
    ans = 0
    if (1 <= s <= tau):
        for i in range(1, s+1):
            ans += new_X[i-1][s-i]
        return ans / s
    elif (tau <= s <= n):
        for i in range(1, tau+1):
            ans += new_X[i-1][s-i]
        return ans / (tau+1)
    elif (n <= s <= N):
        for i in range(1, N-s+2):
            ans += new_X[i+s-n-2][n-i]
        return ans / (N-s+1)

smooth_usd_series = [new_series(i) for i in range(1, N+1)]

# Отрисовка начальной последовательности и сглаженной
def Draw(series, color, xlabel, ylabel):
    plt.plot(series, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

Draw(usd_series, 'r', 'Days', 'KZT')
Draw(smooth_usd_series, 'b', 'Days', 'KZT')

# Прогноз методом SSA
# 6. Прогнозирование исходной временной последовательности
V_tau = V[-1, :r]
V_ast = V[:tau-1, :r]
Q = X[-tau+1 :]

denom = V_tau @ V_ast.T
delim = 1 - V_tau @ V_tau.T
predict_series = (denom.dot(Q)) / delim

predict_series = np.append(usd_series[:N-n], predict_series)

plt.plot(usd_series, 'b')
plt.plot(predict_series, 'r')
plt.xlabel('Days')
plt.ylabel('KZT')
plt.show()
# Draw(usd_series, 'r', 'Days', 'KZT')
# Draw(predict_series, 'b', 'Days', 'KZT')
