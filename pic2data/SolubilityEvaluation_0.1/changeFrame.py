import os
from PIL import Image, ImageEnhance, ImageFilter

def frames(lf):
    lframes = [i for i in lf if i[-4:]=='.png']
    lframes.sort()
    return lframes

class changeFrames():
    
    def __init__(self, Path, cropbox=None): 
        self.Path = Path
        self.lfiles = [i for i in os.listdir(self.Path) if i[-4:] == '.png']
        self.lframes = frames(self.lfiles)
        self.newfolder = os.path.join(self.Path,'overwritten')
        self.imagesize = Image.open(os.path.join(self.Path, self.lfiles[0])).size
        if cropbox == None:
            self.cropbox = (0,0,self.imagesize[0],self.imagesize[1])
        else: self.cropbox = cropbox   
        self.newimagesize = None           
        
    def cuterandnewfolder(self):
        try:
            os.makedirs(os.path.join(self.newfolder))
        except: pass
        for i in self.lframes:   
            image = Image.open(os.path.join(self.Path, i))
            image = image.crop(self.cropbox)
            image.save(os.path.join(self.newfolder,i))
        self.newimagesize = Image.open(os.path.join(self.newfolder,self.lframes[0])).size
            
    def cGaus(self):
        for i in self.lframes:
            image = Image.open(os.path.join(self.newfolder, i))
            image = image.filter(ImageFilter.GaussianBlur)
            image.save(os.path.join(self.newfolder, i))
 
    def cEnhance(self, Faktor=4):
        for i in self.lframes:
            image = Image.open(os.path.join(self.newfolder, i))
            image = ImageEnhance.Contrast(image)
            image.enhance(Faktor).save(os.path.join(self.newfolder, i)) 

    def cGrey(self, Faktor=0):
        for i in self.lframes:
            image = Image.open(os.path.join(self.newfolder, i))
            image = ImageEnhance.Color(image)
            image.enhance(Faktor).save(os.path.join(self.newfolder, i)) 
            
    
        
    def cContrast(self):
        for i in self.lframes:
            image = Image.open(os.path.join(self.newfolder, i))
            source = image.split()
            g = source[2].point(lambda i: i > 100 and 255)
            gn = source[2].point(lambda i: i + 200)
            source[2].paste(gn, None, g)
            image = Image.merge(image.mode, source)
            source = image.split()
            g = source[1].point(lambda i: i > 100 and 255)
            gn = source[1].point(lambda i: i + 200)
            source[1].paste(gn, None, g)
            image = Image.merge(image.mode, source)
            image.save(os.path.join(self.newfolder, i))

#%% Ort
if __name__ == '__main__':

    cwd = ('Z:\%s_Projekt__Permeabilitätsbeeinflussung\%s_Löslichkeitsuntersuchungen\HS Microscope\Experiments\Vidoes' % ('2', '02'))  
    smal = os.path.join(cwd , 'komisch')
    Frames = changeFrames(smal, (15, 5, 750, 475))
    print('Imagesize: ', Frames.imagesize)
    Frames.cuterandnewfolder()
    Frames.cGaus()
    Frames.cEnhance(4.5)
    Frames.cContrast()    
    print('Newimagesize: ', Frames.newimagesize)    
    print('\nDas Program ist jetzt zuende!')
