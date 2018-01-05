import Anton as aen
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
#import seaborn as sns; sns.set()

path = r'Z:\2_Projekt__Permeabilitätsbeeinflussung\AP 4 - 90%\02_Löslichkeitsuntersuchungen\HS Microscope\Experiments\Final_results\data'
files = [i for i in os.listdir(path) if i[-4:] == '.npy']
files.sort()
#%%
f = [[],[],[],[]]
for i in files:
    if 'BÜFA_KE_60' in i:
        f[0].append(i)
    elif 'BÜFA_MS_300' in i:
        f[1].append(i)
    elif 'RIMR_MS_300' in i:
        f[3].append(i)
    else:
        f[2].append(i)

#%%
factor = [0.73, 0.8]
fmt = ['--or', '--ob', '--ok', '--og']
n = 0
for m in f:
    data = np.zeros([len(m),3])
    name = ('%s %s%s'% (m[0].split('_')[0],m[0].split('_')[1],m[0].split('_')[2]))
    j = 0
    for i in m:       
        x = float(os.path.split(i)[1].split('_')[3])   
        if 'MS300' in name: fac = factor[0]
        else: fac = factor[1]
        d = np.load(os.path.join(path,i))#/510.551613316      #*fac*10**(-6)# 
        y = 0.5/abs((np.sum(d))/(len(d)))             
        yerr = 0.25/(abs(d.max()-abs(d.min())))
        print(yerr)
        data[j,:] = x,y,yerr
        j += 1 
#    print(np.max(data[:,1]))
    plt.errorbar(data[:,0],data[:,1], data[:,2], fmt=fmt[n], label=name, ms=15, elinewidth=3, capsize=6) #,fmt='--or'
    plt.legend(loc=1)
    plt.ylabel('Half life [Seconds]', size=25)
    plt.xlabel('Temperature [ °C ]', size=25)
    plt.xlim(37.5,87.5)
    plt.yscale('log')
#    plt.ylim(0, 900)
    plt.xticks(size=25)
    plt.yticks(size=25)
#    plt.title('Vergleich der Auflösungsgeschwindigkeiten in Abhängigkeit der Temperatur', size=22)
    n+=1



#title = 'Auflösungsgeschwindigkeit'
#figure = plt.gcf()
#plt.subplots_adjust(left=0.15)
#plt.grid()
#figure.set_size_inches(25,17)
#fig = plt.get_current_fig_manager()
#fig.window.showMaximized()
#plt.savefig(('%s.png'% title), dpi=200)
#path = os.path.join(r'Z:\2_Projekt__Permeabilitätsbeeinflussung\AP 4 90%',('%s.png'% title))
#plt.savefig(path, dpi=300)

