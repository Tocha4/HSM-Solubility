import numpy as np
import os
from Anton import *



path = r'Z:\2_Projekt__Permeabilitätsbeeinflussung\02_Löslichkeitsuntersuchungen\HS Microscope\Experiments\Final_results\Vidoes\Momentum'
file = [i for i in os.listdir(path) if i[-4:]=='.npy'][1]

data = np.load(os.path.join(path, file))