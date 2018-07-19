{
  //   gStyle->SetOptFit(1111);
  TGraph *max_gr = new TGraph("max.txt","%lg %lg");
  max_gr->SetTitle("Profile for X = 91 mm");
  max_gr->GetXaxis()->SetTitle("[mm]");
  //   max_gr->GetXaxis()->SetRangeUser(116,128);
  max_gr->GetYaxis()->SetRangeUser(0,20000);
  max_gr->SetMarkerColor(4);
  max_gr->SetMarkerSize(1.2);
  max_gr->SetMarkerStyle(21);
  max_gr->SetLineColor(2);

  TGraph *eff1_gr = new TGraph("eff1.txt","%lg %lg");
  eff1_gr->SetTitle("Profile for X = 136.5 mm");
  eff1_gr->GetXaxis()->SetTitle("[mm]");
  //   eff1_gr->GetXaxis()->SetRangeUser(3,17);
  eff1_gr->GetYaxis()->SetRangeUser(0,20000);
  eff1_gr->SetMarkerColor(4);
  eff1_gr->SetMarkerSize(1.2);
  eff1_gr->SetMarkerStyle(21);
  eff1_gr->SetLineColor(4);

  /*TGraph *eff90_gr = new TGraph("eff09.txt","%lg %lg");
  eff90_gr->SetTitle("Profile for X = 0 mm");
  eff90_gr->GetXaxis()->SetTitle("[mm]");
  //   eff80_gr->GetXaxis()->SetRangeUser(116,128);
  eff90_gr->GetYaxis()->SetRangeUser(0,20000);
  eff90_gr->SetMarkerColor(4);
  eff90_gr->SetMarkerSize(1.2);
  eff90_gr->SetMarkerStyle(21);
  eff90_gr->SetLineColor(3);
*/
  TGraph *eff80_gr = new TGraph("eff08.txt","%lg %lg");
  eff80_gr->SetTitle("Profile for X = 0 mm");
  eff80_gr->GetXaxis()->SetTitle("[mm]");
  //   eff80_gr->GetXaxis()->SetRangeUser(116,128);
  eff80_gr->GetYaxis()->SetRangeUser(0,20000);
  eff80_gr->SetMarkerColor(4);
  eff80_gr->SetMarkerSize(1.2);
  eff80_gr->SetMarkerStyle(21);
  eff80_gr->SetLineColor(1);




  TCanvas *c2 = new TCanvas("fwhm","fwhm",1800,1200);
  TMultiGraph *mg = new TMultiGraph();
  mg->Add(max_gr,"l");
  mg->Add(eff1_gr,"l");
  //mg->Add(eff90_gr,"l");
  mg->Add(eff80_gr,"l");
  mg->Draw("a");

  TLegend *legend = new TLegend(0.6,0.65,0.893,0.89,"");
  legend->SetFillStyle(0);
  legend->AddEntry(max_gr,"max","l");
  legend->AddEntry(eff1_gr,"eff1","l");
  //legend->AddEntry(eff90_gr,"eff0.9","l");
  legend->AddEntry(eff80_gr,"eff0.8","l");
  legend->Draw();
//   TGraph *sagittal = new TGraph("eff1_gr-top.tsv","%lg %lg");
//   sagittal->SetTitle("Profile for X = 45.5 mm");
//   sagittal->GetXaxis()->SetTitle("[mm]");
// //   sagittal->GetXaxis()->SetRangeUser(3,17);
//   sagittal->GetYaxis()->SetRangeUser(0,20000);
//   sagittal->SetMarkerColor(4);
//   sagittal->SetMarkerSize(1.2);
//   sagittal->SetMarkerStyle(21);

//   float centers[8] = {101.0,96.0,91.0,86.0,76.0,51.0,26.0,2.0};
//   float sigmaT[8],sigmaC[8],peakT[8],peakC[8],fwhmT[8],fwhmC[8];
//   TF1 *gaussCenter[8];
//   for(int i = 0 ; i < 8 ; i++)
//   {
//     std::stringstream name;
//     name << "gaussC" << i;
//     gaussCenter[i] = new TF1(name.str().c_str(), "gaus",centers[i]-2.0,centers[i]+2.0);
//     gaussCenter[i]->SetLineColor(i+1);
//   }
//   TF1 *gaussTop[8];
//   for(int i = 0 ; i < 8 ; i++)
//   {
//     std::stringstream name;
//     name << "gaussT" << i;
//     gaussTop[i] = new TF1(name.str().c_str(), "gaus",centers[i]-2.0,centers[i]+2.0);
//     gaussTop[i]->SetLineColor(i+1);
//   }
//
//   TCanvas *c = new TCanvas("Profiles","Profiles",1800,1200);
//   c->Divide(1,2);
//   c->cd(2);
//   max_gr->Draw("Al");
//   for(int i = 0 ; i < 8 ; i++)
//   {
//     std::stringstream name;
//     name << "gaussC" << i;
//     max_gr->Fit(name.str().c_str(),"R+","same");
//     peakC[i] = gaussCenter[i]->GetParameter(1);
//     sigmaC[i] = gaussCenter[i]->GetParameter(2);
//     fwhmC[i] = 2.355*gaussCenter[i]->GetParameter(2);
//   }
//   c->cd(1);
//   eff1_gr->Draw("Al");
//   for(int i = 0 ; i < 8 ; i++)
//   {
//     std::stringstream name;
//     name << "gaussT" << i;
//     eff1_gr->Fit(name.str().c_str(),"R+","same");
//     peakT[i] = gaussTop[i]->GetParameter(1);
//     fwhmT[i] = 2.355*gaussTop[i]->GetParameter(2);
//   }
//   c->Print("profiles.png");
//
//   TCanvas *c2 = new TCanvas("fwhm","fwhm",1800,1200);
//   c2->cd();
//   TGraph *gCenter = new TGraph(8,&peakC[0],&fwhmC[0]);
//   gCenter->SetMarkerColor(4);
//   gCenter->SetMarkerSize(1.2);
//   gCenter->SetMarkerStyle(21);
// //   gCenter->GetXaxis()->SetRangeUser(0,150);
// //   gCenter->GetYaxis()->SetRangeUser(0,3);
//   TGraph *gTop = new TGraph(8,&peakT[0],&fwhmT[0]);
//   gTop->SetMarkerColor(2);
//   gTop->SetMarkerSize(1.2);
//   gTop->SetMarkerStyle(22);
// //   gTop->GetXaxis()->SetRangeUser(0,150);
// //   gTop->GetYaxis()->SetRangeUser(0,3);
//   TMultiGraph *mg = new TMultiGraph();
// //   mg->GetXaxis()->SetRangeUser(0,150);
//   mg->SetTitle("Source dimension FWHM [mm] - FOV radial center is 101 mm;Radial Position [mm]; FWHM [mm]");
//   mg->Add(gCenter,"p");
//   mg->Add(gTop,"p");
//   mg->Draw("a");
//   mg->GetXaxis()->SetRangeUser(0,150);
//   mg->GetYaxis()->SetRangeUser(0,3);
// //   gCenter->Draw("A*");
//   TLegend *legend = new TLegend(0.6,0.65,0.893,0.89,"");
//   legend->SetFillStyle(0);
//   legend->AddEntry(gCenter,"X = 91 mm (center)","p");
//   legend->AddEntry(gTop,"X = 136.5 mm","p");
//   legend->Draw();
//   c2->Print("fwhm.png");
  TFile* fFile = new TFile("profiles.root","recreate");
  fFile->cd();
  // c->Write();
  c2->Write();
  fFile->Close();

}
