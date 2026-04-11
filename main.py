import numpy as np
import matplotlib.pyplot as plt 
import math as mt 
from scipy.integrate import odeint

#We have 3 differential equations, with 2 constants :
#The K01 absorption rate constant : 0.33 min^-1
#The K02 elimination rate constant : 0.33 hour^-1 -> 19.8 min^-1 

K01 = 0.33
K02 = 19.8
QConso = 160 #Quantity in mg

def model(x,t):
    #Parameters
    A0=x[0]
    A1=x[1]
    A2=x[2]
    #The kinetics equations 
    dA0=-K01*A0
    dA1=K01*A0 + K02*A2
    dA2=-K02*A2
    return [dA0,dA1,dA2]

x0 = [QConso, 0, 0]
t=np.linspace(0, 10, 101)
x = odeint(model, x0, t)

plt.plot(x,t)
plt.show()