#go to directory
cd /home/irene/Documents/CERN/programs/recoGATE/imageAnalysis/SpatialRes/CylindricalPET/0.5mm/line
#compile c++
g++ /home/irene/Documents/CERN/programs/recoGATE/imageAnalysis/SpatialRes/code/fitFWHMline.cpp -o fitFWHMline `root-config --cflags --glibs`

#execute c++ on all txt files that do not start with out
for file in *.txt
  do
    if [[ ${file:0:3} != "out" ]]
    then
    echo $file
    ./fitFWHMline $file
  fi
  done

#matlab??


#call python to analyse output of c++
python /home/irene/Documents/CERN/programs/recoGATE/imageAnalysis/SpatialRes/code/FWHMline.py
