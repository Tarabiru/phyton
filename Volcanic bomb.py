# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 20:16:04 2018

@author: taram
"""

from numpy import *
import matplotlib.pyplot as plt

def dxdt(v_x):
    return v_x
def dydt(v_y):
    return v_y
def dvdt_v(a_y):
    return a_y

x0 = 0;         y0 = 0
v_x0 = 45.8;    v_y0 = 79.4
a_x = 0;        g = 9.81

t0 = 0; t1 = 16
n = 200
dt = float(t1 - t0)/n

x = zeros(n+1)
x[0] = x0
v_x = v_x0

y = zeros(n+1)
y[0] = y0
v_y = zeros(n+1)
v_y[0] = v_y0

for i in range(0, n, 1):
    # Horinzontally
    x[i+1] = x[i] + dt*dxdt(v_x)
    # Vertically 
    y[i+1] = y[i] + dt*dydt(v_y[i])
    v_y[i+1] = v_y[i] - dt*dvdt_y(g)
    
    if i == 0 or i == 1:
        print x[i+1]
        print y[i+1]
        print v_y[i+1]
        
time = linspace(t0, t1, n+1)
x_simple = v_x*time
y_simple = v_y0*time - 0.5*g*time**2

plt.plot(x, y, 'b-', x_simple, y_simple, 'r--')
plt.title('Volcanic bomb motion')
plt.xlabel('Horizontal position')
plt-ylabel('Vertical position')
plt.show()










    


