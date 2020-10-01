from matplotlib import pyplot as plt
import numpy as np
from scipy import special as sp

M = 1000
sigma = 800

timeStep = 10
T = np.arange(0, 3000, timeStep)
U = (T - M) / sigma

density = 1.41 * 10**(-2) * np.exp(U**2 / 2)
reliability = 1 - (0.5 * (1 + sp.erf(U / 2**0.5)))
intensity = density / reliability

for t in range(500, 2501, 500):
    print("Для t = {:d}:\n".format(t))
    print("\tПлотность = {:.4f}\n".format(density[t // timeStep]))
    print("\tНадежность = {:.4f}\n".format(reliability[t // timeStep]))
    print("\tИнтенсивность = {:.4}\n\n".format(intensity[t // timeStep]))


num_cols = 2
num_rows = 2
pad_value = 5

plt.figure(figsize=(num_cols * 7, num_rows * 4.5))

plt.subplot(num_rows, num_cols, 1)
plt.xlabel("t")
plt.ylabel("Плотность")
plt.grid(True)
plt.tight_layout(pad = pad_value)
plt.plot(T, density)

plt.subplot(num_rows, num_cols, 2)
plt.xlabel("t")
plt.ylabel("Надежность")
plt.grid(True)
plt.tight_layout(pad = pad_value)
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
plt.tight_layout(pad = pad_value)
plt.plot(T, intensity, label = "Интенсивность")
plt.plot(T, reliability, label = "Надежность")
plt.plot(T, density, label = "Плотность")
plt.ylim([-0.5, 5])
plt.legend()

plt.show()