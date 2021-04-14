import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import scipy.optimize
import scipy.stats as stat
from scipy.signal import find_peaks

#carpool shell with delay time at .8ms
datafilename = 'CP0_8delay.txt'
t,y = np.loadtxt(datafilename,unpack=True)

#y = y - 2.14875e-3
y = (y + 0.0004)*10e2
t= t

print(y,t)
plt.grid()


pkidx,_ = find_peaks(y, height= 140)

print(y[pkidx])
print(y[pkidx][2:])
time =t[pkidx]
time = time[2:]
height = y[pkidx]
height = height[2:]
error= np.full_like(height, 0.78)
plt.errorbar(time, height, yerr=error,ls='none',fmt='.') 





def f(x, A, B, C):
    return A*np.exp(-x/B)+C


parms, covariance = scipy.optimize.curve_fit(f,time,height,[700,0.20,0],sigma=error,absolute_sigma=1)

A, B, C = parms
print (parms)
for i in range(0,len(parms)):
    print('param ',i,' = ',parms[i], '+/-', np.sqrt(covariance[i,i]))


xx = np.linspace(0,0.040,30)
ff = f(xx, *parms)

#chi square

fit = f(time, *parms)
dof = len(time) - len(parms)
chisq = sum( (height-fit)**2 / error**2 )
redchisq= chisq/float(dof)

print ('Chi Square Value', chisq)
print ('Degrees of Freedom', dof)
print ('Reduced Chi Square Value', redchisq)
print('With what confidence can we reject this model? ',stat.chi2.cdf(chisq,dof))

plot_xlabel = 'time (s) '
plot_ylabel = 'voltage (mV)'

plt.plot ( xx,ff,'r-')
plt.title('Transverse Magnetization ')
plt.xlabel(plot_xlabel)
plt.ylabel(plot_ylabel)
plt.savefig('CPdelay0.8.jpg', dpi=1000)

plt.show()


# In[ ]:




