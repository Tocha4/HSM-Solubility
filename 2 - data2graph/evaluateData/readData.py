import Anton as aen
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.stats import linregress as lin

def gcfunction(files, temp): # liefert nur die files mit einer bestimmten Temperatur
    gc = []
    for i in files:
        fname,name = os.path.split(i)
        gcn = name.split('_')[-1:]
        gcn = gcn[0][:-4]
        gcn = float(gcn)
        if gcn == temp:
            gc.append(i)
    return gc 
    
def entry():
    evaluatin = input('>>> ')
    evi = evaluatin.split(';')
    times = [(i) for i in evi]
    times = [i.split(',') for i in times]
    times = [[float(j) for j in i] for i in times]
    return times
   
def seerawdata(files,temp):
    forty = gcfunction(files,temp)
    j = 1
    for i in forty:
        _,title = os.path.split(i)
        data = np.load(i)
        plt.subplot(4,3,j)
        plt.plot(data[0,:],data[1,:], '-ob')
        plt.grid()
        plt.title(title)
        j += 1
    figure = plt.gcf()
    figure.set_size_inches(20,17)
    plt.savefig(('%s.png'% title), dpi=200)
    plt.close(figure)
    return forty

def createSlopes(tempfiles, times):
    slopes = np.array([])
    j = 0
    for i in tempfiles:
        if times[j][0] != times[j][1]:
            path,title = os.path.split(i)
            data = np.load(i)
            start = np.where(data[0] >= times[j][0])[0][0]
            ende = np.where(data[0] <= times[j][1])[0][-1]
            x = data[0,start:ende]
#            print(np.max(data[1,start]))
            y = data[1,start:ende]/data[1,start]       
            slope, intercept, r_value, p_value, slope_std_error = lin(x, y)
            print(slope)
            fx = intercept+ slope*x       
            lab = ('%s %s - %s'% (title, str(data[0][start]),str(data[0][ende])))
            plt.plot(x,fx, label=lab)
            plt.legend()
            j += 1
            slopes = np.append(slopes,slope)
        else: j += 1
    name = os.path.split(tempfiles[0])[1].split('_')
    temp = ( '%.1f' % float(name[-1].split('.npy')[0])) 
    name = ('%s_%s_%s_%s_Celsius' %(name[1],name[2],name[3],temp))
    file = os.path.join(os.path.split(os.path.split(tempfiles[0])[0])[0],name)
    plt.title('%s'% times)
    plt.show()
    np.save(file, slopes)
    return slopes
    
#%%
path = r'Z:\2_Projekt__Permeabilitätsbeeinflussung\02_Löslichkeitsuntersuchungen\HS Microscope\Experiments\Final_results\data\1 - RIMR+KE60'

files = aen.searchfiles(path, '.npy')
files.sort()
#data = np.load(files[0])
temp = 42.5

tempfiles = seerawdata(files, temp)
times = entry()

slopes = createSlopes(tempfiles,times)
























