import os
import changeFrame as cf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg


def split(image):
    b = mpimg.imread(image)[:,:,2]  
    return b

def change(b, faktor=0.5):
    new_b = np.zeros(b.shape)
    for i in np.arange(b.shape[0]):
        for j in np.arange(b.shape[1]):
            if b[i][j] <= faktor:
                new_b[i][j] = 0
            else: new_b[i][j] = 1
    return new_b

class countPixel2():
    
    def __init__(self, pathfolder):
        self.Path = pathfolder
        self.lfiles = os.listdir(self.Path)
        self.limage = [i for i in self.lfiles if i[-4:]=='.png']
        self.limage.sort()
        self.data = np.zeros((2, len(self.limage)), dtype=float)
    
    def splitandchange(self,savepath, nameDatafile='data', faktor=0.5):
        n = 0
        for i in self.limage:
            b = split(os.path.join(self.Path,i))
            new_img = change(b,faktor)
            mpimg.imsave(os.path.join(self.Path,i), new_img)
            j = 0
            for x in range(new_img.shape[0]):
                for y in range(new_img.shape[1]):
                    if b[x][y] == 1:
                        j += 1
                    else: pass
            self.data[0][n] = float(i[:-4])
            self.data[1][n] = j
            n += 1
        np.save(os.path.join(savepath, nameDatafile), self.data)


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




if __name__ == '__main__':

    pathimages = (r'Z:\2_Projekt__Permeabilitätsbeeinflussung\02_Löslichkeitsuntersuchungen\HS Microscope\Experiments\Vidoes\RIMR_MS-300\rimh_ms-300_55Celsius\vlc-record-2017-01-13-03h55m29s-dshow___-')

    imageslist = [i for i in os.listdir(pathimages) if i[-4:] == '.png']
    imageslist.sort()    
    r,g,b = split(os.path.join(pathimages,imageslist[15]))    
    new_b = change(b, 0.5)
    mpimg.imsave('test1.png', new_b)
    plt.imshow(new_b)
    plt.colorbar()
    j = 0
    for i in new_b:
        j += 1
    print(j)































