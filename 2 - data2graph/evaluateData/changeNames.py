import Anton as aen
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.stats import linregress


def changeCelsius(path):
    files = aen.searchfiles(path, '.npy')
    files.sort()
    for i in files:
        fname,name = os.path.split(i)
        if 'Celsius' in name:
            nm = name.split('Celsius')
            nm = nm[0]+nm[1]
            os.rename(os.path.join(fname,name), os.path.join(fname,nm))
    return print('geaender')
        
def change2under(path):
    files = aen.searchfiles(path, '.npy')
    files.sort()
    j = 0
    for i in files:
        j += 1
        fname, name = os.path.split(i)
        try:
            nm = name.replace('KE60','KE_60')
            os.rename(os.path.join(fname,name), os.path.join(fname,nm))
            print(nm)
        except: pass
    return print('%s Files vorhanden'% str(j))
    
    



if __name__ == '__main__':
    
    path = r'Z:\2_Projekt__Permeabilitätsbeeinflussung\02_Löslichkeitsuntersuchungen\HS Microscope\Experiments\Final_results\data'
    change2under(path)
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    