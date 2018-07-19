/*
compile with:

g++ fitFWHMline.cpp -o fitFWHMline `root-config --cflags --glibs`
*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <TCanvas.h>
#include <TGraphErrors.h>
#include <TF1.h>
#include <TApplication.h>
#include <TFitResultPtr.h>
#include <TFitResult.h>



int main(int argc, char** argv){

  std::string inputfilename ;
  inputfilename = argv[1] ;

  //TApplication* Grafica = new TApplication("Grafica", 0, NULL);

  std::ifstream infile;
  infile.open(inputfilename.c_str(), std::ios::in);

  //check if it is good
  if(infile.good()==0)
  {
    std::cout << "Error! Cannot open file " << inputfilename << std::endl;
    return 1;
  }

  TGraphErrors* graphtest = new TGraphErrors();

  double norm[8];
  for (int i=0; i<8; i++)
    norm[i] = 0;

    double sourcepos[8] = {0,5,10,15,25,50,75,99};
    //double sourcepos[4] = {25,50,75,99};

  double x, y;
  int lines = 0;
  while(infile >> x >> y)
  {
    x = -(x-251+42)*0.5;
    //set normalization at positions of sources
    for(int j=0; j<(sizeof(sourcepos)/sizeof(sourcepos[0])); j++)
    {
      if(x==sourcepos[j])
        norm[j] = y;
    }

    graphtest->SetPoint(lines,x,y);
    graphtest->SetPointError(lines, 0.5/sqrt(12),sqrt(y));
    lines++;
  }

  double fwhm[(sizeof(sourcepos)/sizeof(sourcepos[0]))];
  double err_fwhm[(sizeof(sourcepos)/sizeof(sourcepos[0]))];

  std::stringstream outfilename;
  outfilename << "out" << inputfilename;
  ofstream outfile((outfilename.str()).c_str());

  for(int j=0; j<(sizeof(sourcepos)/sizeof(sourcepos[0])); j++)
  {
    //prepare name of function
    std::stringstream namefunc;
    namefunc << "source" << j;

    TF1* funzione = new TF1((namefunc.str()).c_str(), "gaus(0)", sourcepos[j]-2, sourcepos[j]+2);
    funzione->SetParameter(0, norm[j]);
    funzione->SetParameter(1, sourcepos[j]+0.25);
    funzione->SetParameter(2, 1);
    funzione->SetNpx(10000);
    //graphtest->Fit((namefunc.str()).c_str());
    TFitResultPtr fp = graphtest->Fit((namefunc.str()).c_str(), "S");
    if(fp->Status() == 0 && (funzione->GetParError(2)) < 1) //HACK because sometimes it converges but error is too big to make any  sense
    {
      fwhm[j] = fabs((funzione->GetParameter(2)))*2.355;
      err_fwhm[j] = (funzione->GetParError(2))*2.355;
      outfile << sourcepos[j] << "\t" << fwhm[j] << "\t" << err_fwhm[j] << "\n";
    }



  }

  outfile.close();
	//TCanvas* c1 = new TCanvas("boh");
	//graphtest->Draw("ALP");
	//Grafica->Run();
	return 0;
}
