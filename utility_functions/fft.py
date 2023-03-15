
import numpy as np

def dft(x):
    x = np.asarray(x, dtype=float)
    print (x)
    N = x.shape[0]
    print (N)
    n = np.arange(N)
    print (n)
    k = n.reshape((N, 1))
    print (k)
    M = np.exp(-2j * np.pi * k * n / N)
    #print (M[0])
    print (M[1])
    return np.dot(M, x)

x = np.random.random(10)


result = dft(x)

#print (np.fft.fft(x))