import math
import os
import sys
import matplotlib as mpl
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show

directory = '/home/irene/Documents/CERN/programs/recoGATE/imageAnalysis/SpatialRes/CylindricalPET/0.5mm/line/'

filenames = []
filenamesa = []

for filename in os.listdir(directory):
    if (filename.endswith('.txt') and filename.find('outm') != -1):
        if(filename.endswith('a.txt')):
            filenamesa.append(filename)
        else:
            filenames.append(filename)
filenames.sort()
filenamesa.sort()
filenames_list = filenames + filenamesa

for filename in filenames_list:
    x = []
    y = []
    yerr = []
    with open(directory+filename) as f:
        data = f.read()
    data = data.split('\n')
    for row in data:
        if len(row) != 0:
            x.append(float (row.split('\t')[0]))
            y.append(float (row.split('\t')[1]))
            yerr.append(float (row.split('\t')[2]))

    if not filename.endswith('a.txt'):
        plt.subplot(121)
        plt.errorbar(x, y, xerr=0.5/math.sqrt(12), yerr=yerr, fmt='.-', label=filename[4:-4])
        #plt.plot(x, y, marker='.', markersize=5, label=filename[4:-4])
        plt.title('FWHM, z=0, 0.5mm pixels')
        plt.xlabel('radial distance from centre (mm)')
        plt.ylabel('FWHM (mm)')
        plt.legend(loc='best')

    elif filename.endswith("a.txt"):
        plt.subplot(122)
        plt.errorbar(x, y, xerr=0.5/math.sqrt(12), yerr=yerr, fmt='.-', label=filename[4:-5])
        #plt.plot(x, y, marker='.', markersize=5, label=filename[4:-5])
        plt.title('FWHM, z=45.5, 0.5mm pixels')
        plt.xlabel('radial distance from centre (mm)')
        plt.ylabel('FWHM (mm)')
        plt.legend(loc='best')


plt.show()
input()
