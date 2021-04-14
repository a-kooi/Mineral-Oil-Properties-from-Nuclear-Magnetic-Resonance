import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import scipy.optimize
import scipy.stats as stat
from scipy.signal import find_peaks

#meiboom gill with delay time at .5ms
datafilename = 'MG.5delay.txt'
t,y = np.loadtxt(datafilename,unpack=1)

#y = y - 2.27375e-3

peaks, _ = find_peaks(y, height=.022)
time = t[peaks][2:]
height = y[peaks][2:]
time1 = time*1
height1 = height*1
error = np.full_like(height,.00078)
plt.errorbar(time,height,yerr=error,ls='none',fmt='.') 

def f(x, A, B, C):
    return A*np.exp(-x/B)+C
guess = np.array([.1,.02,0])

parms, covariance = scipy.optimize.curve_fit(f,time,height,sigma=error,p0=guess,absolute_sigma=1)
A, B, C = parms
print (parms)
for i in range(0,len(parms)):
    print('param ',i,' = ',parms[i], '+/-', np.sqrt(covariance[i,i]))


xx = np.linspace(0,0.038,1001)
ff = f(xx, *parms)
plt.plot ( xx,ff,'r-')
plt.grid()

fit = f(time, *parms)
dof = len(time) - len(parms)
chisq = sum( (height-fit)**2 / error**2 )
redchisq= chisq/float(dof)

print ('Chi Square Value', chisq)
print ('Degrees of Freedom', dof)
print ('Reduced Chi Square Value', redchisq)
print('With what confidence can we reject this model? ',stat.chi2.cdf(chisq,dof))

plot_xlabel = 'time (s)'
plot_ylabel = 'voltage (v)'


plt.title('MG Spin Echo Amplitude Decay')
plt.xlabel(plot_xlabel)
plt.ylabel(plot_ylabel)
plt.savefig('MG.5delay01.jpg', dpi=1000)



plt.show()
