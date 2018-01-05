import os
import moviepy.editor as mv
import numpy as np

class Video():
    
    def __init__(self, path):
        self.path = path
        self.Name = os.path.split(self.path)
        self.myclip = mv.VideoFileClip(self.path)
        self.Duration = self.myclip.duration
    
    def makeFrames(self, Start=0, End=None, n=100):
        if End == None:
            End = self.Duration
        else: pass
    
        Intv = (End - Start)/n
        t = Start
        try:
            os.makedirs(os.path.join(self.Name[0], self.Name[1][:-4]))
        except: pass
    
        newpath = os.path.join(self.Name[0], self.Name[1][:-4])
        while t <= End:
            
#            minuten = t//60
#            sekunden = int(t-minuten*60)
#            milisec = t-minuten*60-sekunden           
#            zeit = ('%.2d:%.2d:%.2d' % (minuten, sekunden, milisec))
            self.myclip.save_frame(os.path.join(newpath, "%7.2f.png" % t), t=t)     
            t += Intv
        return newpath
#%% Tests
if __name__ == '__main__':
    cwd = (r'Z:\2_Projekt__Permeabilitätsbeeinflussung\02_Löslichkeitsuntersuchungen\HS Microscope\Experiments\Vidoes\RIMR_MS-300\rimh_ms-300_55Celsius')  
    smal = os.path.join(cwd , 'vlc-record-2017-01-13-03h55m29s-dshow___-.avi')
    vid = Video(smal)
    name = vid.Name[1][:-4]    
    print(name)
    print(vid.Duration)
#%%
    p = vid.makeFrames(Start=43, n=200)
    print(p)
