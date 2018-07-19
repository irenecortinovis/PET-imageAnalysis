import math
import os
import sys
import matplotlib as mpl
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
from scipy.odr import *


pos_sources = (0.25, 5.25, 10.25, 15.25, 25.25, 50.25, 75.25, 99.25)

def gauss_sources_func(p, x):
    a1, sigma1, a2, sigma2, a3, sigma3, a4, sigma4, a5, sigma5, a6, sigma6, a7, sigma7, a8, sigma8 = p
    return (a1*np.exp(-(x-0)**2/(2*sigma1**2)) + a2*np.exp(-(x-5)**2/(2*sigma2**2)) + a3*np.exp(-(x-10)**2/(2*sigma3**2))
                + a4*np.exp(-(x-15)**2/(2*sigma4**2)) + a5*np.exp(-(x-25)**2/(2*sigma5**2)) + a6*np.exp(-(x-50)**2/(2*sigma6**2))
                + a7*np.exp(-(x-75)**2/(2*sigma7**2)) + a8*np.exp(-(x-99)**2/(2*sigma8**2)))


#directories = ['../CylindricalPET/0.5mm/','../CylindricalPET/1mm/','../CylindricalPET/2mm/']
directories = ['../CylindricalPET/0.5mm/line/','../CylindricalPET/1mm/']

filenames = []
filenamesa = []

for directory in directories:
    #print(directory)
    for filename in os.listdir(directory):
        if (filename.endswith('.txt') and not filename[0:3] == 'out'):
            if(filename.endswith('a.txt')):
                filenamesa.append(filename)
            else:
                filenames.append(filename)
    filenames.sort()
    filenamesa.sort()
    filenames_list = filenames + filenamesa
    #print(filenames_list)

    for filename in filenames_list:
        x = []
        y = []
        with open(directory+filename) as f:
            data = f.read()
        data = data.split('\n')
        for row in data:
            if len(row) != 0:
                if(directory.find('0.5mm') != -1):
                    x.append(-((float (row.split('\t')[0]))-251+42)*0.5)
                    y.append(float (row.split('\t')[1]))
                    #fig = plt.figure(0)

                if(directory.find('1mm') != -1):
                    x.append(-((float (row.split('\t')[0]))-126+20))
                    y.append(float (row.split('\t')[1]))
                    #fig = plt.figure(1)

                if(directory.find('2mm') != -1):
                    x.append(-((float (row.split('\t')[0]))-64+10)*2)
                    y.append(float (row.split('\t')[1]))
                    #fig = plt.figure(2)



        if not filename.endswith('a.txt'):
            #plt.subplot(121)
            if(directory.find('0.5mm') != -1):
                fig = plt.figure(0)
                plt.ylabel('mean on 10 pixels')
                plt.title('z=0, pixels 0.5mm')
            elif(directory.find('1mm') != -1):
                fig = plt.figure(1)
                plt.ylabel('mean on 6 pixels')
                plt.title('z=0, pixels 1mm')
            elif(directory.find('2mm') != -1):
                fig = plt.figure(2)
                plt.ylabel('mean on 4 pixels')
                plt.title('z=0, pixels 2mm')
            plt.plot(x,y, marker='.', linewidth=1, markersize=1, label=filename[:-4])
            plt.xlabel('mm from centre')
            plt.legend(loc='best')


            '''#per trovare normalizzazione prendo il valore di y alle sorgenti
            norm0 = y[x.index(math.floor(pos_sources[0]))]
            norm1 = y[x.index(math.floor(pos_sources[1]))]
            norm2 = y[x.index(math.floor(pos_sources[2]))]
            norm3 = y[x.index(math.floor(pos_sources[3]))]
            norm4 = y[x.index(math.floor(pos_sources[4]))]
            norm5 = y[x.index(math.floor(pos_sources[5]))]
            norm6 = y[x.index(math.floor(pos_sources[6]))]
            norm7 = y[x.index(math.floor(pos_sources[7]))]
            gaussians_model = Model(gauss_sources_func)
            data = RealData(x,y)
            p = [norm0, 0.6, norm1, 0.7, norm2, 0.8, norm3, 0.8, norm4, 0.9, norm5, 0.9, norm6, 0.9, norm7, 0.1]
            odr = ODR(data, gaussians_model, beta0=p, maxit=10000)
            out = odr.run()
            #out.pprint()

            FWHM = out.beta[1::2]*2.355
            FWHM_error = out.sd_beta[1::2]*2.355
            if(directory.find('0.5mm') != -1):
                pixel = 'pixels 0.5mm'
                fig = plt.figure(6)
                label = pixel + ", " + filename[:-4]
                #plt.errorbar(pos_sources, FWHM, yerr=FWHM_error, fmt='.', label=label)
                plt.plot(pos_sources, FWHM, marker='.', markersize=5, label=label)
                plt.title('FWHM, z=0')
                plt.xlabel('positions of sources')
                plt.ylabel('sigma')
                plt.legend(loc='best')'''




        elif filename.endswith("a.txt"):
            #plt.subplot(122)

            if(directory.find('0.5mm') != -1):
                fig = plt.figure(3)
                plt.ylabel('mean on 10 pixels')
                plt.title('z=45.5, pixels 0.5mm')
            elif(directory.find('1mm') != -1):
                fig = plt.figure(4)
                plt.ylabel('mean on 6 pixels')
                plt.title('z=45.5, pixels 1mm')
            elif(directory.find('2mm') != -1):
                fig = plt.figure(5)
                plt.ylabel('mean on 4 pixels')
                plt.title('z=45.5, pixels 2mm')
            plt.plot(x,y, marker='.', linewidth=1, markersize=1, label=filename[:-5])
            plt.xlabel('mm from centre')
            plt.legend(loc='best')


            '''#per trovare normalizzazione prendo il valore di y alle sorgenti
            norm0 = y[x.index(math.floor(pos_sources[0]))]
            norm1 = y[x.index(math.floor(pos_sources[1]))]
            norm2 = y[x.index(math.floor(pos_sources[2]))]
            norm3 = y[x.index(math.floor(pos_sources[3]))]
            norm4 = y[x.index(math.floor(pos_sources[4]))]
            norm5 = y[x.index(math.floor(pos_sources[5]))]
            norm6 = y[x.index(math.floor(pos_sources[6]))]
            norm7 = y[x.index(math.floor(pos_sources[7]))]
            gaussians_model = Model(gauss_sources_func)
            data = RealData(x,y)
            p = [norm0, 0.6, norm1, 0.7, norm2, 0.7, norm3, 0.8, norm4, 0.8, norm5, 0.9, norm6, 1.1, norm7, 1.1]
            odr = ODR(data, gaussians_model, beta0=p, maxit=10000)
            out = odr.run()
            #out.pprint()

            FWHM = out.beta[1::2]*2.355
            FWHM_error = out.sd_beta[1::2]*2.355
            if(directory.find('0.5mm') != -1):
                pixel = 'pixels 0.5mm'
                fig = plt.figure(7)
                label = pixel + ", " + filename[:-5]
                #plt.errorbar(pos_sources, FWHM, yerr=FWHM_error, fmt='.', label=label)
                plt.plot(pos_sources, FWHM, marker='.', markersize=5, label=label)
                plt.title('FWHM, z=45.5')
                plt.xlabel('positions of sources')
                plt.ylabel('sigma')
                plt.legend(loc='best')'''
    filenames = []
    filenamesa = []
    filenames_list = []

plt.show()
input()
