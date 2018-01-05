from Anton import searchfiles
import numpy as np
import matplotlib.pyplot as plt
import os

a = (r'Z:\2_Projekt__Permeabilitätsbeeinflussung\AP 4 - 90%\02_Löslichkeitsuntersuchungen\HS Microscope\Experiments\Final_results\data\2 - RIMR+MS300')
p = searchfiles(a, '.npy')
p.sort()
#
#for i in p:
#    print(os.path.split(i)[1])

#%%
def calcslopes(p):
    mslopes = np.zeros([2,len(p)]) # slopes, Temperature, name
    name = []
    for i in range(len(p)):
        data = np.load(p[i])        
        mslopes[0][i] = np.sqrt((np.sum(data)/len(data))**2)
        try:
            mslopes[1][i] = int(os.path.split(p[i])[1][-6:-4])
        except: mslopes[1][i] = float(os.path.split(p[i])[1][-8:-4])
        name.append(os.path.split(p[i])[1][:-4])
    return mslopes,name

def moment(path):
    data = np.load(path)
    KE = np.sqrt(((data[0]+data[1])/2)**2)
    MS = data[2]
    K = data[3]
    return KE, MS, K



#%%
if __name__ == '__main__':
    
    data,name = calcslopes(p)
    color = ['b', 'g', 'r', 'c', 'm', 'y', 'k']#['r','r', 'g', 'g', 'g','m','m','m','b','b','b','b'] #
    marker=['D','o','d','v',',','.','>','8','+','_','x','*','<']
    j = 0
    n = 0
    for i in range(len(name)):
        
        plt.plot(data[1][i],data[0][i],marker=marker[j], label=name[i], c=color[n], markersize=20)
        n += 1
        print(n,j)
        if n > 6:
            n = 0
            j += 1
            if j > 12:
                j=0

    
#    KE,MS,K = moment(searchfiles(a,'Momentum.npy')[0])
#    plt.plot(27,KE, marker='h', label='Momentum_KE-60',c='k', markersize=20)
#    plt.plot(27,K, marker='8', label='Momentum_MS-300',c='y', markersize=20)
#    plt.plot(27,MS, marker='*', label='Momentum_K-85',c='c', markersize=20)

    plt.legend()
    plt.title('Auflösungsgeschwindigkeiten in Abhängigkeit der Temperatur', size=30)
#    plt.xlim(25,90)
#    plt.ylim(-0.0025,0.025)
    plt.ylabel('Auflösungsgeschwindigkeit (Steigung) \n [normierte Fläche/Sekunde]', size=25)
    plt.xlabel('Temperatur [°C]', size=25)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()