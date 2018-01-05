import numpy as np
import Anton as aen
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def zeile(z,average, total, factor):
    gd = np.array([])
    for i in range(len(z)-average):
        summe = sum(z[i:i+average])/average
        if summe >= total:
           summe = summe*factor
        elif summe <= 12:
            summe = summe*factor
        gd = np.append(gd,summe)
    return gd

def zeile2(z,average=10, total=10, factor=2):
    gd = np.array([])
    for i in range(len(z)-average):
        summe = sum(z[i:i+average])/average
        slope = (max(z[i:i+average]) - min(z[i:i+average]))/2
        if summe >= total:
           summe = summe*factor
        elif summe <= 12:
            summe = summe*factor
        gd = np.append(gd,slope)
    return gd

def row(z,rows=11,factor=2, average=30):
    gd = np.array([])
    for i in range(len(z)-rows):
        avg = sum(z[i:i+rows])
        gd = np.append(gd,avg)
    return gd

def pic(img,average=10,total=20, factor=10):
    newpic = np.zeros([480-average,768])
    for i in range(len(img[0,:])):
        newpic[:,i] = zeile(img[:,i],average, total, factor)
    return newpic


def pic2(img,rowandcolumns=3,factor=2, average=30 ):
    newpic = np.zeros([480-rowandcolumns,768-rowandcolumns])
    for i in range(len(img[0,:])):
        Trows = np.zeros([len(newpic[:,0]),rowandcolumns])
        for j in range(rowandcolumns):
            Trows[:,j] = row(img[:,i+j], rows=rowandcolumns)
        print(Trows)
        for x in range(len(newpic[:,0])):
            newpic[x,i] = sum(Trows[x,:])/rowandcolumns**2
        
        
    return newpic

#def gdnewpic(pics, average):
#    for i in pics:
#        img = mpimg.imread(i)[:,:,2]
#        z   = np.asarray(img)*100
#        newpic = np.array([])
#        for j in range(len(img[0,:])):
# 


#%%

if __name__ == '__main__':
    
    path = (r'Z:\2_Projekt__Permeabilitätsbeeinflussung\02_Löslichkeitsuntersuchungen\HS Microscope\HSM Recording development\Auswertung\pic2data\Pictures\meansqrt')
    
    pics = os.listdir(path)
    pics = [i for i in pics if i[-4:] == '.png']
    pics.sort()
    img = np.asarray(mpimg.imread(os.path.join(path,pics[42]))[:,:,2])*100
    
#
#    newpic = pic(img, average=5, total=25, factor=3)/100
#    plt.figure()
#    plt.imshow(newpic)
#    plt.title('average %s' % str(5))
    
    average = 15
    newpic = pic2(img)
    plt.figure()
    plt.imshow(newpic)
#    plt.title('average %s' % str(average))
#    
#    plt.figure()
#    plt.imshow(img)  
#    plt.title('blau')
#    
#    plt.figure()
#    plt.imshow(mpimg.imread(os.path.join(path,pics[42])))  
#    plt.title('original')
#%%
#    newimg = zeile2(img[:,450],average=18, total=10, factor=2)
#    plt.figure()
#    plt.plot(img[7:,450])
#    plt.plot(newpic[:,450], 'r')
    


