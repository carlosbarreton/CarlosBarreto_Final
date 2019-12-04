import numpy as np
import matplotlib.pyplot as plt

def dft(yk,N):
    Yn = np.zeros(N,dtype=complex)
    Z = np.exp(-2*np.pi*1j/N)
    for n in range(N):
        suma = 0j
        for k in range(N):
            suma += Z**(n*k)*yk[k]
        Yn[n] = suma
    return Yn

manchas = np.loadtxt("monthrg.dat")
tiempo = manchas[:,0] + manchas[:,1]/12
numero = manchas[:,3]
numero = numero[tiempo>1900]
tiempo = tiempo[tiempo>1900]

plt.figure()
N = len(numero)
fourier = dft(numero,N)
plt.figure()
plt.scatter(np.arange(N),abs(fourier))
plt.xlabel("k")
plt.ylabel("$|S_k|$")
plt.savefig("solar.png")