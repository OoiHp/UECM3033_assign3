import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(y,t,a,b):
    y0, y1 = y
    dy = [a*(y0-y0*y1), b*(-y1+y0*y1)]
    return dy
    
a=1.0
b=0.2
y1=1.0
yrs=5
t = np.linspace(0, yrs, yrs+1) #5 years

y0=0.1       
yin = [y0,y1]
y=odeint(f, yin, t, args=(a,b))    

plt.plot(t, y[:,0],'r', label='$y_0$')
plt.plot(t, y[:,1],'b', label='$y_1$')
plt.legend(loc='best')
plt.xlabel('$t(year)$')
plt.ylabel('$y$')
plt.title('$y_0$=%r\n$y_0$ and $y_1$ against $t$'%(y0))
plt.grid()
plt.show()

plt.plot(y[:,0], y[:,1],'g')
plt.xlabel('$y_1$')
plt.ylabel('$y_0$')
plt.title('$y_1$ against $y_0$')
plt.grid()
plt.show()
    
y0=0.11
yin = [y0,y1]
y=odeint(f, yin, t, args=(a,b))    

plt.plot(t, y[:,0],'r', label='$y_0$')
plt.plot(t, y[:,1],'b', label='$y_1$')
plt.legend(loc='best')
plt.xlabel('$t(year)$')
plt.ylabel('$y$')
plt.title('$y_0$=%r\n$y_0$ and $y_1$ against $t$'%(y0))
plt.grid()
plt.show()

plt.plot(y[:,0], y[:,1],'g')
plt.xlabel('$y_1$')
plt.ylabel('$y_0$')
plt.title('$y_1$ against $y_0$')
plt.grid()
plt.show()