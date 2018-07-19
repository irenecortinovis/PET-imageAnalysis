function fitfwhm()

    %to be changed
    filename = '../CylindricalPET/0.5mm/line/eff1.txt'
    %import data from file
    delimiterIn = '\t';
    data = importdata(filename,delimiterIn);

    %change x to distance from centre
    datax = double(-(data(:,1)-251+42)*0.5);
    datay = double(data(:,2));

    %definition of sources
    nsources = 8;
    sourcepos = [0,5,10,15,25,50,75,99];

    %open output file
    outfilename = strcat('out',infile) %only if in the same directory!!
    %outfilename = 'test.txt';
    outfile = fopen(outfilename,'w');

    %cycle on all sources
    for i = 1:nsources

        %find range of x and y near the source
        index = find(datax==sourcepos(i));
        x = datax((index-4):(index+4));
        y = datay((index-4):(index+4));

        %plot and fit
        plot(x,y)
        hold on
        f = fit(x,y,'gauss1');
        plot(f,x,y)

        %fwhm
        coefficients = coeffvalues(f);
        confidencebounds = confint(f);
        fwhm = coefficients(3)*2.355

        %error on fwhm
        minCB = confidencebounds(1,2);
        maxCB = confidencebounds(2,2);
        errorfwhm = (maxCB-minCB)/2/1.96*2.355

        %print on output file
        fprintf(outfile,'%.4f\t%.4f\n',fwhm,errorfwhm);

        %reset arrays
        x = [];
        y = [];
    end

    fclose(outfile);
end
