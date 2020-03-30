from math import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X = pd.read_csv('usd_kzt.csv', encoding = 'UTF-8', delimiter = ',')
X = X.drop(['USD_quant'], axis = 1)
Date = X['Date'].values
USD = X['USD'].values

N = len(USD)
tau = 46
r = 10

full = [USD[i: N - tau + i] for i in range(tau)]
full = np.array(full)
cov_matr = np.cov(full)

L, V = np.linalg.eig(cov_matr)
V = V[:r]
Y = V.transpose()
Y = Y.dot(full[:r])

new_X = V.dot(Y)
real = np.hstack((full[0][:tau], full[tau - 1]))
prediction = np.hstack((new_X[0][:tau], new_X[r - 1]))

plt.plot(Date, real, 'b')
plt.plot(Date, prediction, 'r' )
plt.xlabel('Date')
plt.ylabel('KZT')
plt.show()