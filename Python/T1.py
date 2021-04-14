import numpy as np
import matplotlib.pyplot as plt

datay = np.array([84, 81.6, 78.4, 76.8, 74.4, 69.6, 66.4, 62.4, 56.8, 52, 44.8, 37.6, 29.6, 20, 12, 11.2, 12, 12, 12.8, 13.6, 14.4, 15.2, 16.8, 17.6, 19.2, 20.8, 22.4, 24.8, 26.4, 28, 30.4 ])
datat = np.array([88, 85, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 9.9, 9.8, 9.3, 9.1, 8.5, 8, 7.5, 7, 6.5, 6, 5.5, 5, 4.5, 4, 3.5])

error = 0.64105
t = np.linspace(0,100,1000)


y1 = -92 + 38.8*np.log(t)
y2 = 51.1*np.exp(-0.149*t)

plt.plot(t,y1,t,y2,)
plt.errorbar(datat,datay,error,marker='o',linestyle='')

plt.axis([0,100,0,100])

plt.title(' T1 and Zero Crossing ')
plt.xlabel( 'Delay Time (mS)' )
plt.ylabel( 'Voltage (V)' )
plt.savefig('T1 plot.jpg',dpi=1000)
plt.grid()

plt.show()

