import numpy as np
import matplotlib.pyplot as plt 
import math as mt 
from scipy.integrate import odeint
#We have 3 differential equations, with 2 constants :
#The K01 absorption rate constant : 0.33 min^-1
#The K02 elimination rate constant : 0.33 hour^-1 -> 19.8 min^-1 

def calculation(K01, K2, t0, h, n, a0, a1, a2):
    A0 = [a0]
    A1 = [a1]
    A2 = [a2]
    t = [t0]
    for k in range(n):
        t.append(t[k] +1)
        y.append(y[k] + h*f(y[k]))
    return t, y