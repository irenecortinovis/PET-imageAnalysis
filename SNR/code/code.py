#!/usr/bin/env python

#--------------------------------------------------------------------------------------#
#                                                                                      #
#  Simple script to analyse the data from the simple PET demonstrator                  #
#                                                                                      #
#--------------------------------------------------------------------------------------#

import sys, time, glob, struct, subprocess, os, shutil

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


print("Starting the code")


numero_step=1


numero_output= 7
for x in range(0, numero_step):
    for y in range(1, 7):
        if x < 10:
            linecode ="list_ROI_values test_output_cylinder_between/output%isignal%i outputgz_00%i.hv ../ROI_parameter_cylinder_between/ROI_uniform_cylinder_s%i.par" %(y,numero_output,numero_output,y)
        else:
            linecode ="list_ROI_values test_output_cylinder_between/output%isignal%i outputgz_0%i.hv ../ROI_parameter_cylinder_between/ROI_uniform_cylinder_s%i.par" %(y,numero_output,numero_output,y)
        p = subprocess.call(linecode,shell=True)
    numero_output=numero_output+1

numero_output= 7
for x in range(0, numero_step):
    for y in range(1, 7):
        if x < 10:
            linecode ="list_ROI_values test_output_cylinder_between/output%ibkg%i outputgz_00%i.hv ../ROI_parameter_cylinder_between/ROI_uniform_cylinder_b%i.par" %(y,numero_output,numero_output,y)
        else:
            linecode ="list_ROI_values test_output_cylinder_between/output%ibkg%i outputgz_0%i.hv ../ROI_parameter_cylinder_between/ROI_uniform_cylinder_b%i.par" %(y,numero_output,numero_output,y)
        p = subprocess.call(linecode,shell=True)
    numero_output=numero_output+1
