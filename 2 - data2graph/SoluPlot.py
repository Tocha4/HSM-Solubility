from Anton import searchfiles
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.stats import linregress
from itertools import cycle
import seaborn as sns; sns.set()

def get_files():
    a = (r'Z:\2_Projekt__Permeabilitätsbeeinflussung\AP 4 - 90%\02_Löslichkeitsuntersuchungen\HS Microscope\Experiments\Final_results\data\2 - RIMR+MS300')
    p = searchfiles(a, '.npy')
    p.sort()
    
    files = dict()
    for i in p:
        path,name = os.path.split(i)
        if name[-6:-4] in files:
            files[name[-6:-4]].append(i)
        else:
            files[name[-6:-4]] = [i]
    return files


def solureaction(g, files, number='all', ende=None, start=None,marker='o', cr='k'):

    p = files[g]
    
    if number == 'all':
        number = [os.path.split(i)[1][:-19] for i in p]
    else:
        number = number#['10','30','3','5']
    
    slopes = np.array([])
    inters = np.array([])
    colors = cycle(i for i in ['b', 'g', 'r', 'c', 'm', 'y', 'k'])
    j = 0
    for i in range(len(p)):
        check = os.path.split(p[i])[1][:-19]
        
        if check in number:
            
            data = np.load(p[i])
            _,label = os.path.split(p[i])
            if start == None:
                start = 0#np.where(data[0] > 100)[0][0]#starttimes[j])[0][0]
            else: start = start
            if ende == None:
                x = data[0]#data[0][-2] #stoptimes[j]
                y = data[1]
            else:
                ende = ende
                try:
                    index = np.where(data[0] > ende)[0][0]
                    x = data[0][start:index]-data[0][start]
                    y = data[1][start:index]
                except:
                    x = data[0][start:]-data[0][start]
                    y = data[1][start:]
            color = colors.__next__()
            plt.plot(x, y/np.max(y),marker,  markersize=8 , c=color, alpha=0.7)  
            
            slope, intercept, r_value, p_value, slope_std_error = linregress(x, y/np.max(y))
            slopes = np.append(slopes,slope)
            inters = np.append(inters, intercept)
            j += 1
    m = np.mean(slopes)
    fx = np.mean(inters) + m*x
    plt.plot(x,fx, '-', label=('RIMR with MS-300 at {}°C'.format( g)), linewidth=10, c=cr)




if __name__=='__main__':
    
    files = get_files()

    solureaction('55',files,['10','30','3','5'], ende=850, start=20, marker='o',cr='m')
    solureaction('65',files, ['6','7','8'], ende=550, start=25, marker='D',cr='k')
    solureaction('75', files, ['10','11','29','30'], ende=300, start=20, marker='v', cr='g')
    solureaction('85', files, ['13','15','16'], ende=100, start=5, marker='X', cr='b')
    
    plt.legend(fontsize=20)
    plt.show()
    plt.ylabel('Area concentration [ A/A0 ]', size=25)
    plt.xlabel('Time [ Seconds ]', size=25)
    plt.xlim(0,750)
    plt.ylim(0,1.05)
    plt.xticks(size=25)
    plt.yticks(size=25)
    


