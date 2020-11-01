from matplotlib import pyplot as plt
import numpy as np
from scipy import special as sp

M = 1000
sigma = 800

timeStep = 10
T = np.arange(0, 3000, timeStep)
U = (T - M) / sigma


def F(v):
    return 0.5 * (1 + sp.erf(v / 2**0.5))


def f(v):
    return 1 / ((2*np.pi)**0.5 * sigma) * np.exp(-v**2 / 2)


def F_inv(v):
    return M + sigma * sp.erfinv((1-v)/0.5 - 1)


density = f(U)
reliability = 1 - F(U)
intensity = density / reliability

test = sp.erf(0)

T_medium = M + 2*sigma / ((2*np.pi)**0.5 * (1 - F(-M/sigma))) * np.exp(-M**2/(2*sigma**2))

T_090 = F_inv(0.90)
T_095 = F_inv(0.95)
T_099 = F_inv(0.99)

for t in range(500, 2501, 500):
    print("Для t = {:d}:\n".format(t))
    print("\tПлотность = {:.6f}\n".format(density[t // timeStep]))
    print("\tНадежность = {:.6f}\n".format(reliability[t // timeStep]))
    print("\tИнтенсивность = {:.6}\n\n".format(intensity[t // timeStep]))

print("Среднее время наработки на отказ: {:.4f}\n\n".format(T_medium))

print("Гамма-процентный ресурс:\n")
print("\tПри P = 0.90: {0:.4f}\n".format(T_090))
print("\tПри P = 0.95: {0:.4f}\n".format(T_095))
print("\tПри P = 0.99: {0:.4f}\n".format(T_099))

num_cols = 2
num_rows = 2
pad_value = 5

plt.figure(figsize=(num_cols * 7, num_rows * 4.5))

plt.subplot(num_rows, num_cols, 1)
plt.xlabel("t")
plt.ylabel("Плотность")
plt.grid(True)
plt.tight_layout(pad=pad_value)
plt.plot(T, density)

plt.subplot(num_rows, num_cols, 2)
plt.xlabel("t")
plt.ylabel("Надежность")
plt.grid(True)
plt.tight_layout(pad=pad_value)
plt.plot(T, reliability)

plt.subplot(num_rows, num_cols, 3)
plt.xlabel("t")
plt.ylabel("Интенсивность")
plt.grid(True)
plt.tight_layout(pad = pad_value)
plt.plot(T, intensity)

plt.subplot(num_rows, num_cols, 4)
plt.xlabel("t")
plt.ylabel("All")
plt.grid(True)
plt.tight_layout(pad=pad_value)
plt.plot(T, intensity, label="Интенсивность")
plt.plot(T, reliability, label="Надежность")
plt.plot(T, density, label="Плотность")
plt.ylim([-0.5, 5])
plt.legend()

plt.show()
