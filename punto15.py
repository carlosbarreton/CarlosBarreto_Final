import numpy as np
import matplotlib.pyplot as plt

x_k = np.loadtxt("valores.txt")
def likelihood(sigma, x_k):
    return (1/np.sqrt(2*np.pi*sigma**2))*np.exp(-0.5*x_k**2/sigma**2)

def p_sigma(A=10):
    return A

def L(sigma, x):
    prob = (1/9)*sigma/sigma
    for x_k in x:
        prob *= likelihood(sigma, x_k)
    return prob

x = [float(number) for number in x_k]
sigma = np.linspace(1,10,100)
l = L(sigma,x)

plt.figure()
plt.plot(sigma,l)
plt.title("prob($\sigma$|{$x_k$})")
plt.xlabel("$\sigma$")
plt.savefig("sigma.png")

def metropolis(sigma, N=100000, delta=1.0):
    lista = [np.random.random()]

    for i in range(1,N):
        propuesta  = lista[i-1] + (np.random.random()-0.5)*delta
        r = min(1, L(sigma, propuesta)/L(sigma, lista[i-1]))
        alpha = np.random.random()
        if(alpha<r):
            lista.append(propuesta)
        else:
            lista.append(lista[i-1])
    return np.array(lista)