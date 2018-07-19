from ij import IJ  
import ij.Prefs;

imp1 = IJ.getImage()
imp2 = IJ.getImage()


#from left to right
ij.Prefs.verticalProfile = 0

#10far
imp1.setRoi(141,248,14,6)
IJ.run(imp1, "Plot Profile", "");

#10clo
imp1.setRoi(239,248,11,6)
IJ.run(imp1, "Plot Profile", "");

#15clo
imp1.setRoi(252,248,14,6)
IJ.run(imp1, "Plot Profile", "");

#15far
imp1.setRoi(347,248,17,6)
IJ.run(imp1, "Plot Profile", "");


#from top to bottom
ij.Prefs.verticalProfile = 1

#20far
imp2.setRoi(248,134,6,21)
IJ.run(imp2, "Plot Profile", "")

#20clo
imp2.setRoi(248,230,6,19)
IJ.run(imp2, "Plot Profile", "")

#25clo
imp2.setRoi(248,253,6,22)
IJ.run(imp2, "Plot Profile", "")

#25far
imp2.setRoi(248,347,6,18)
IJ.run(imp2, "Plot Profile", "")

#ij.Prefs.verticalProfile = 0

