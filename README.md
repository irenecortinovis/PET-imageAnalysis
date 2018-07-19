# CODE

### SPATIAL RESOLUTION

``line.py``
plot profiles

``fitfwhm.m``
fit one file of in 0.5mm with gaussians, output files with filename, fwhm, errorfwhm

``FWHMline.py``
plot fwhm using output files created with matlab or root

``fitFWHMline.cpp``
fit gaussians with ROOT but fits are not good

``fitfwhm.sh``
script for running cpp on all files and then python

### RESOLVING POWER

``scriptfiji.py``
save profiles of groups of sources

``cross.py``
plot profiles and calculate resolving power


### SNR
- ``code.py``

Calculates the mean and stdev of the activity in each ROI defined in ROI_parameter_cylinder_between, using stir.
The index runs on the number of iterations of the images.

Need to set: origin (in mm):={n of planes in axial direction / 2,-17.3,20}

Go in the directory where the reconstructed images are, create a new directory called "test_output_cylinder_between" where the .txt output will be written.

e.g. ``list_ROI_values test_output_cylinder_between/text_tof10ps_%isignal%i reco_norm_tof10ps_0%i.hv ../ROI_parameter_cylinder_between/ROI_uniform_cylinder_s%i.par``

- ``complete_evaluation.py``
Calculate SNR from the output files created with ``code.py``.

Hardcoded things to set in code:
``for x1 in range(100, 113):``
these are the lines in the .txt that you want to consider.


# WORKFLOW for spatial resolution and resolving power

Start from ``images.hv`` and ``images.v`` with different methods (no compton, efficiencies, average, maxenergy)

Open each image with Fiji and use scriptfiji.py to choose ROIs and save the profiles of each ROI.

### Case spatial resolution:

Filenames for spatial resolution, line of sources at centre of scanner in axial direction: ``eff06.txt, eff07.txt, eff08.txt, eff09.txt, eff1.txt, max.txt, nocompt.txt``.

Add "a" before .txt for filenames for line of sources at perifery of scanner in axial direction: eg. ``eff06a.txt, eff07a.txt``, ...

Plot profiles with ``line.py``
Need to set directories inside the code, can choose 0.5mm, 1mm and 2mm pixels.
(Offsets and number of pixels hardcoded to convert from Fiji coordinates to coordinates from centre of scanner. These must correspond to the scriptfiji ROIs offsets and number of pixels in .hv / 2.)

Fit each .txt file with gaussians.
``fitfwhm.m`` is for 0.5mm pixels.
(Offsets and number of pixels hardcoded to convert from Fiji coordinates to coordinates from centre of scanner. These must correspond to the scriptfiji ROIs offsets and number of pixels in .hv / 2.)
Fits each source with a gaussian and outputs a file with 3 columns: filename, fwhm, errorfwhm.

Plot results from MATLAB output with ``FWHMline.py``.

(TODO: script that runs MATLAB script on all files in directory, then plots results with python)



### Case resolving power:

Filenames for resolving power, cross of sources:

``distance (10,15,20,25) + clo/far + _ + method (eff06, ...) (+a if perifery axial direction) + .txt``
eg. ``15clo_nocompta.txt``

Plot profiles and calculate resolving power with ``cross.py``
(Offsets and number of pixels hardcoded, must correspond to the scriptfiji ROIs offsets and number of pixels in .hv / 2).

Set in code position of sources, names of files (divided in x and y oriented ROIs), and directory where files to analyse are.
