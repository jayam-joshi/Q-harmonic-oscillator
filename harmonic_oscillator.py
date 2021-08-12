import matplotlib.pyplot as plt
import numpy as np
from math import *

h = 6.62607015e-34
h_bar = h/(2*pi) 
w = 10
E_0 = h_bar*w/2
m = 1
hermite = []
n = int(input("Energy Level \n"))

j=n
while True:
    if j==n:
        x = pow(2,n)
        hermite.append(x)
        j = j-2
        continue
    if j<0:
        break
    x = -1*(j+1)*(j+2)*x/(2*(n-j))    #Real analysis
    hermite.append(x)
    j = j-2
print(hermite)

t = -10
zeta = []
psi = []
A = pow(m*w/(pi*h_bar),0.25)

while t<10:
    zeta.append(t)
    i = A*exp(-t*t/2)/sqrt(pow(2,n)*factorial(n))
    j=n
    k=0
    hermitian = 0
    
    while j>=0:
        hermitian = hermitian + hermite[k]*pow(t,j)
        j = j-2
        k = k+1
    psi.append(i*hermitian)
    t = t+0.01

plt.style.use('dark_background')
plt.xlabel('x')
plt.ylabel('ψ')
plt.plot(zeta,psi)
plt.show()




    





    
    
    





