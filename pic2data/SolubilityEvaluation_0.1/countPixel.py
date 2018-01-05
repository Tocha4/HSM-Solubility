from PIL import Image, ImageMath
import matplotlib.pyplot as plt
import matplotlib.figure as pltfig
import numpy as np
import os
from changeFrame import frames 

class countPixel():
    
    def __init__(self, path):
        self.Path = path
        self.lfiles = os.listdir(self.Path)
        self.limage = frames(self.lfiles)
        self.data = np.zeros((2, len(self.limage)), dtype=float)
                
    def cPixel(self, nameDataFile='data', sumgb=10):       
        j = 0
        for i in self.limage:            
            self.data[0][j] = float(i[:-4])
            image = Image.open(os.path.join(self.Path, i))
            n = 0
            for x in range(0, image.size[0]):
                for y in range(0, image.size[1]):
                    pixel = (x,y)
                    rgb = image.getpixel(pixel)
                    if rgb[1] + rgb[2] >= sumgb:
                        n += 1
                    else: pass
            self.data[1][j] = n
            j += 1
        np.save(os.path.join(self.Path, nameDataFile), self.data)
                        
    def dataPlot(self, nr=1, title='Auflösungsreaktion'):
        plt.hold(True)
        plt.figure(nr)
        plt.plot(self.data[0], self.data[1]/self.data[1][0], 'bs')
        plt.title(title)
#        plt.xlim(-0.25,11)
#        plt.ylim(0.15, 1.025)
        plt.ylabel('Flächenkonzentration [ A/A0 ]')
        plt.xlabel('Zeit [ Sekunden ]')
        plt.show()
        plt.savefig(os.path.join(self.Path, 'SR.jpeg'))
        plt.savefig(os.path.join(self.Path, 'SR.pdf'))
        
#%%

if __name__ == '__main__':
    cwd = ('Z:\%s_Projekt__Permeabilitätsbeeinflussung\%s_Löslichkeitsuntersuchungen\HS Microscope\Experiments\Vidoes' % ('2', '02'))  
    path = os.path.join(cwd , 'komisch', 'overwritten')
    
    folder = countPixel(path)
    folder.cPixel()
    folder.dataPlot()
    print(np.load(os.path.join(path, 'data.npy'))[1])

#    print(folder.data)    
    
    
    
    
    
    
    
    
    
    
