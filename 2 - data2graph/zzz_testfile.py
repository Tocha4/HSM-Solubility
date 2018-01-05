from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pylab as pl
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.image as mpimg

img = Image.open('309.14.png')#[:,:,2]#.convert('L')
img = mpimg.imread('309.14.png')[:,:,2]
z   = np.asarray(img)*100
zz = z#[280:,450:650]
mydata = zz[::1,::1]
x,y = np.mgrid[:mydata.shape[0],:mydata.shape[1]]
#%%
#fig = pl.figure(facecolor='w')
#ax1 = fig.add_subplot(1,2,1)
#im = ax1.imshow(mydata,interpolation='nearest',cmap=pl.cm.jet)
#ax1.set_title('2D')
#
##%%
#
#ax2 = fig.add_subplot(1,2,2,projection='3d')

#ax2.plot_surface(x,y,mydata,cmap=pl.cm.jet,rstride=1,cstride=1,linewidth=0.,antialiased=False)
#ax2.set_title('3D')
#ax2.set_zlim3d(0,100)
#pl.show()

#fig = plt.figure()
#ax = fig.gca(projection='3d')
#surf = ax.plot_surface(x,y,zz, cmap=cm.cool,)
#fig.colorbar(surf, shrink=0.5, aspect=5)
#plt.show()
gd = np.array([])
j = 4
for i in range(len(z[:,0])-10):
    summe = sum(z[j-4:j+6,200])/10
    gd = np.append(gd,summe)
    j += 1
print(len(gd))


fig2 = plt.figure()
print(len(z[4:474,200]))
plt.plot(z[4:474,200])
plt.plot(gd, 'r')
