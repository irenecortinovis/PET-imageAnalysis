import math
import os
import sys
import matplotlib as mpl
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
from scipy.odr import *
import pandas as pd


pos_sourcesx_temp = ([-54.5,-53,-51.5,-50], [-6,-4.5,-3,-1.5], [2,3], [50,51,52,53])
pos_sourcesy_temp = ([-55,-52.5,-50], [-10,-7.5,-5,-2.5], [2,4,6,8], [50,52,54,56])

pos_sourcesx = []
pos_sourcesy = []

#order sources in different way
for sources in pos_sourcesx_temp:
    for source in sources:
        sources[sources.index(source)] = -source
    sources.sort()
pos_sourcesx = list(reversed(pos_sourcesx_temp))

for sources in pos_sourcesy_temp:
    for source in sources:
        sources[sources.index(source)] = -source
    sources.sort()
pos_sourcesy = list(reversed(pos_sourcesy_temp))

#print(pos_sourcesx)
#print(pos_sourcesy)
#[[-53, -52, -51, -50], [-4, -3, -2, -1], [1.5, 3, 4.5, 6], [50, 51.5, 53, 54.5]]
#[[-56, -54, -52, -50], [-8, -6, -4, -2], [2.5, 5, 7.5, 10], [50, 52.5, 55]]



namex = ('10far', '10clo', '15clo', '15far') #from left to right
namey = ('20far', '20clo', '25clo', '25far') #from top to bottom

offsetx = (141, 239, 252, 347) #from left to right
offsety = (134, 230, 253, 347) #from top to bottom
halfx = 251
halfy = 251

SNR_data = []

filenames = []
filenamesa = []
directory = '/home/irene/Documents/CERN/programs/recoGATE/imageAnalysis/SpatialRes/CylindricalPET/0.5mm/cross/'
for filename in os.listdir(directory):
    if (filename.endswith('.txt') and filename[0:3] != 'out') :
        if(filename.endswith('a.txt')):
            filenamesa.append(filename)
        else:
            filenames.append(filename)
filenames.sort()
filenamesa.sort()
filenames_list = filenames + filenamesa

for filename in filenames_list:
    if (filename.endswith('.txt') and filename[0:3] != 'out') :
        x = []
        y = []
        with open(directory+filename) as f:
            data = f.read()
        data = data.split('\n')
        for row in data:
            if (len(row) != 0 and row.split('\t')[0] != 'X'):
                for name in namex:
                    if filename.find(name) != -1:
                        x.append(((float (row.split('\t')[0]))-halfx+offsetx[namex.index(name)])*0.5)
                        title = name
                        fileid = namex.index(name)

                for name in namey:
                    if filename.find(name) != -1:
                        x.append(((float (row.split('\t')[0]))-halfx+offsety[namey.index(name)])*0.5)
                        title = name
                        fileid = namey.index(name) + len(namex)


                plt.xlabel('mm from centre')
                plt.ylabel('mean on 6 pixels')
                y.append(float (row.split('\t')[1]))


        sources_sets = []

        if int(fileid / 4) == 0:
            sources_sets = pos_sourcesx
        elif int(fileid / 4) == 1:
            sources_sets = pos_sourcesy


        if len(sources_sets) != 0:
            maxs = []
            mins = []
            counter = 0;
            for source in sources_sets[fileid%4]:
                #print('find max in: \t', y[x.index(source)-1:x.index(source)+2])
                maxs.append(max(y[x.index(source)-1:x.index(source)+2]))
                if counter < len(sources_sets[fileid%4])-1:
                    #print('find min in: \t', y[x.index(source):x.index((sources_sets[fileid%4])[counter+1])])
                    mins.append(min(y[x.index(source):x.index((sources_sets[fileid%4])[counter+1])]))
                counter = counter +1

            #print('printing mins, max: ', mins, maxs)

            #SNR
            meanmax = sum(maxs)/len(maxs)
            meanmin = sum(mins)/len(mins)

            SNR = meanmax / meanmin
            errSNR = SNR*(1/math.sqrt(meanmax) + 1/math.sqrt(meanmin)) #they are poissonian

            #centre
            centre = 1  #the sources are at the centre of ring
            if(filename.find('far') != -1):
                centre = 0  #sources are at edges of ring

            #z0 and method
            z0 = 1 #z is == 0
            method = filename[6:-4]
            if(filename.endswith('a.txt')):
                z0 = 0  #z is at the edge of detector for the axial coordinate
                method = filename[6:-5]

            #distance
            distance = 0
            if(filename.find('10') != -1):
                distance = 1.0  #mm
            elif(filename.find('15') != -1):
                distance = 1.5  #mm
            elif(filename.find('20') != -1):
                distance = 2.0  #mm
            elif(filename.find('25') != -1):
                distance = 2.5  #mm


            SNR_dict = {"centre" : centre,
                        "z0" : z0,
                        "method" : method,
                        "distance" : distance,
                        "SNR" : SNR,
                        "errSNR" : errSNR}

            SNR_data.append(SNR_dict)


        if not filename.endswith('a.txt'):
            '''if fileid == 4:
                plt.figure(2)
            else:
                plt.figure(0)
                plt.subplot(2,4,fileid+1)'''
            plt.figure(0)
            plt.subplot(2,4,fileid+1)
            title = title + ', z=0'
            plt.title(title)
            plt.plot(x,y, marker='.', linewidth=1, markersize=1, label=filename[6:-4])
            plt.legend(loc='best')


        elif filename.endswith("a.txt"):
            plt.figure(1)
            plt.subplot(2,4,fileid+1)
            title = title + ', z=84'
            plt.title(title)
            plt.plot(x,y, marker='.', linewidth=1, markersize=1, label=filename[6:-5])
            plt.legend(loc='best')


df = pd.DataFrame(SNR_data)

for iz, group in df.groupby('z0'):
    plt.figure(1+iz)
    figs, axs = plt.subplots(2,4)
    for ix, methodgroup in group.groupby(['centre', 'method']):
        centre, method = ix
        for distance, distancegroup in methodgroup.groupby('distance'):
            if(iz==0):
                title = "d=" + str(distance) + "mm, z=84mm"
            else:
                title = "d=" + str(distance) + "mm, z=0"
            if(centre==0):
                title += ", centre FOV"
            else:
                title += ", edge FOV"
            index = int(distance/0.5-2)
            x_array = []
            for snr in distancegroup['SNR']:
                x_array.append(method)
            axs[centre,index].set_title(title, fontsize=11)
            axs[centre,index].errorbar(x_array,distancegroup['SNR'], yerr=distancegroup['errSNR'], fmt='.', color="black")
            axs[centre,index].set_xlabel('method', fontsize=10)
            axs[centre,index].set_ylabel('SNR', fontsize=10)
            #print(title, x_array, distancegroup['SNR'])
            for tick in axs[centre,index].xaxis.get_major_ticks():
                tick.label.set_fontsize(8)
            for tick in axs[centre,index].yaxis.get_major_ticks():
                tick.label.set_fontsize(8)
            plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)

'''
for iz, group in df.groupby(['z0', 'centre']):
    z0, centre = iz
    plt.figure(1+z0*2+centre)
    figs, axs = plt.subplots(2,2)
    for method, methodgroup in group.groupby('method'):
        if (method == 'amax'):
            method = 'max'
        for distance, distancegroup in methodgroup.groupby('distance'):
            if(z0==0):
                title = "d=" + str(distance) + " mm"
            else:/media/usb-disk/irene/Compton/simulations/cylindricalPET/reconstructions
                title = "d=" + str(distance) + " mm"
            index = int(distance/0.5-2)
            x_array = []
            for snr in distancegroup['SNR']:
                x_array.append(method)
            axs[int(index/2), index%2].set_title(title, fontsize=11)
            axs[int(index/2), index%2].errorbar(x_array,distancegroup['SNR'], yerr=distancegroup['errSNR'], fmt='.', color="black")
            axs[int(index/2), index%2].set_xlabel('method', fontsize=10)
            axs[int(index/2), index%2].set_ylabel('Resolving power', fontsize=10)
            for tick in axs[int(index/2), index%2].xaxis.get_major_ticks():
                tick.label.set_fontsize(8)
            for tick in axs[int(index/2), index%2].yaxis.get_major_ticks():
                tick.label.set_fontsize(8)
            plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
'''
plt.show()
input()
