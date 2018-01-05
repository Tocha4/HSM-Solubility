from vid2frame import *
from changeFrame import *
from imageanalyse import *
from countPixel import *
from Anton import *


#    Z:\2_Projekt__Permeabilitätsbeeinflussung\02_Löslichkeitsuntersuchungen\HS Microscope\Experiments\Vidoes\RIMR_MS-300\rimh_ms-300_55Celsius\vlc-record-2017-01-13-03h55m29s-dshow___-.avi
a = input('Path to the videos, pleas: \n>>> ')
n = input('Number of frames: >>> ')
faktor = input('Enhance factor: >>> ')
faktor2 = input('Was ist Blau in Prozent: >>> ')

if a[-4:] == ('.avi'):
    p = []
    p.append(a)
    a = os.path.split(a)[0]
else:
    p = searchfiles(a, '.avi')

#%%

g = 1
for m in p:
    Vid = Video(os.path.join(a,m))
    dataname = ('%2d_'% g + os.path.split(os.path.split(Vid.path)[0])[1] )
    
#%%
    newpath = Vid.makeFrames(Start=0, n=int(n))
    
#%%
    Frames =changeFrames(newpath)
    Frames.cuterandnewfolder()
    Frames.cEnhance(Faktor=float(faktor))
    
#%%
    pathfilesnew = Frames.newfolder
    data = countPixel2(pathfilesnew)
    data.splitandchange(savepath=a,nameDatafile = dataname, faktor=float(faktor2)/100)
#    data.dataPlot()
    g += 1


