import os
import numpy as np




def searchfiles(pathfolders, datatype):
    lenth = len(datatype)
    file = [[],[]]
    for root,dirs,files in os.walk(pathfolders):
        file[0].append(root)
        file[1].append(files)
    
    fi = []
    
    for x in file[1]:
        index = file[1].index(x)
        for y in x:
            if y[-lenth:] == datatype:
                fi.append(os.path.join(file[0][index],y))
    return fi




if __name__ == '__main__':
    pathfolders = (r'Z:\2_Projekt__Permeabilitätsbeeinflussung\02_Löslichkeitsuntersuchungen\HS Microscope\Experiments\Final_results\data')
    files = searchfiles(pathfolders, '.npy')
    print(len(files))
