import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("pde.dat")

x = np.linspace(0,2,len(data))
plt.plot(x,data, label="Condicion inicial")
plt.xlabel("x")
plt.ylabel("u")
plt.legend()
plt.savefig("resultado.png")