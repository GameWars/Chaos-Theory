"""
Boloutare Doubeni
Math 532H - Non Linear Dynamics and Chaos with Applications
September 22, 2014

Strogatz Exercise 2.8.2
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


#args for linspace
xmin = 0.
xmax = 10.
xn = 32

tmin = xmin
tmax = xmax

#limits = [0, xmax, xmin, xmax]
x = np.linspace(xmin, xmax,xn) #the x-axis
t = np.linspace(0, 2*xmax,xn) #the t-axis
XX, YY = np.meshgrid(t, x) 

    
def f(x,t): return x #f(x)=x

x0 = [0.,.1,.5,1.,1.5] #The initial conditions
F = integrate.odeint(f,x0, t) #The solution of f(x)
dx = x #x'=x
dt = np.ones(32) 
r = (dx**2 + dt**2)**0.5; #use to normalize the vectors
pt = dt/r
px = dx/r

def main(): 
    
    #plot the solution
    plt.plot(dx, F)
    
    #plot the vector field
    plt.quiver(XX, YY, pt, px)
    
    #plot labels
    plt.xlabel('$t$')
    plt.ylabel('$x$')
    plt.title('The direction field of $f(x)=x$ and its solution')
    
    #plot limits
    plt.xlim([tmin, tmax])
    plt.ylim([tmin, tmax])
   
    #save the figure as a pdf file
    plt.savefig('Sec2_8.pdf')

main()


