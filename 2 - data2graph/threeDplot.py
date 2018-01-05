import os
import sys
sys.path.append(r'Z:\2_Projekt__Permeabilitätsbeeinflussung\02_Löslichkeitsuntersuchungen\HS Microscope\HSM Recording development\Auswertung\Auswertung_all')
import changeFrame as cf
from PIL import Image, ImageEnhance, ImageFilter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg


def rgbshow(image):

    image = Image.open(image)
    r,g,b = image.split()
    w = image.size[0]
    h = image.size[1]
    npimgG = np.zeros((w,h))
    
    for x in range(w):
        for y in range(h):
            pixel = (x,y)
            rgb = image.getpixel(pixel)
            npimgG[x][y] = rgb[1]    
    return w,h,npimgG, image

#%%
if __name__ == '__main__':
    
    pathimages = (r'Z:\2_Projekt__Permeabilitätsbeeinflussung\02_Löslichkeitsuntersuchungen\HS Microscope\HSM Recording development\Auswertung\pic2data\testpics')
    imageslist = [i for i in os.listdir(pathimages) if i[-4:] == '.png']
    imageslist.sort()
    a = cf.changeFrames(pathimages)
    print(a.imagesize)
    w,h,npimgG, image = rgbshow(os.path.join(pathimages, imageslist[5]))
    
#%%
    img = mpimg.imread(os.path.join(pathimages,imageslist[5]))
#    imgplot = plt.imshow(img)
    r_img = img[:,:,2]
    
    new_img = np.zeros(r_img.shape)
    for i in np.arange(r_img.shape[0]):
        for j in np.arange(r_img.shape[1]):
            if r_img[i][j] <= 0.5:
                new_img[i][j] = 0
            else: new_img[i][j] = 1
    
    fig = plt.figure()
    im1 = fig.add_subplot(1,2,1)
    im1.imshow(img)
    im2 = fig.add_subplot(1,2,2)
    im2.imshow(new_img)
    fig.savefig('test.png', dpi=500)
#    plt.colorbar()
#    hist = r_img.ravel()
#    plt.hist(hist, bins=256)
    


#    fig = plt.figure()
#    ax = Axes3D(fig)
#    X = np.linspace(0,w-1,w,dtype=int)
#    Y = np.linspace(0,h-1,h,dtype=int)
#    X, Y = np.meshgrid(X, Y)
#    print(X,Y)
#    ax.plot_surface(X, Y, npimgG[X][Y])
#    plt.show()
    
    
    
    





