import matplotlib.pyplot as plt
import matplotlib.axes as ax
import fileinput
import numpy as np
import math as mt

for counter in range(7,8):

    mean_sb_num = 0
    mean_sb_den = 0
    mean_b_num = 0
    mean_b_den = 0

    sum_sb = 0
    sum_b = 0
    std_sum_sb = 0
    std_sum_b = 0

    for lesion in range(1,7):

        source1 ="output%isignal%i" %(lesion,counter)
        source2 ="output%ibkg%i" %(lesion,counter)

        f1 = open(source1,"r")
        f2 = open(source2,"r")

        content1 = []
        content2 = []

        for line1 in f1:
            content1.append(line1.strip())
        for line2 in f2:
            content2.append(line2.strip())

        f1.close()
        f2.close()

        sum_ROI_1 = 0
        std_ROI_1 = 0
        sum_ROI_2 = 0
        std_ROI_2 = 0

        #signal+background
        #sum and std for a single ROI signal+background
        for x1 in range(100, 113):
            a1,b1,c1,d1 = content1[x1].split()
            sum_ROI_1 += float(c1)
            std_ROI_1 +=  float(d1) * float(d1)
        std_ROI_1 = mt.sqrt(std_ROI_1)
        #print(lesion, "  signal+background ", sum_ROI_1, " ", std_ROI_1)

        sum_sb += sum_ROI_1
        std_sum_sb += std_ROI_1*std_ROI_1
        mean_sb_num += (sum_ROI_1)/(std_ROI_1 * std_ROI_1)
        mean_sb_den += 1/(std_ROI_1 * std_ROI_1)

        #background
        #mean and std for a single ROI bkg
        for x2 in range(100, 113):
            a2,b2,c2,d2 = content2[x2].split()
            sum_ROI_2 += float(c2)
            std_ROI_2 +=  float(d2) * float(d2)
            #print(b2)
        std_ROI_2 = mt.sqrt(std_ROI_2)
        #print(lesion, "  background ", sum_ROI_2, " ", std_ROI_2)


        sum_b += sum_ROI_2
        std_sum_b += std_ROI_2*std_ROI_2
        mean_b_num += (sum_ROI_2)/(std_ROI_2 * std_ROI_2)
        mean_b_den += 1/(std_ROI_2 * std_ROI_2)


mean_sb = mean_sb_num / mean_sb_den
mean_b = mean_b_num / mean_b_den
std_sb = mt.sqrt(1 / mean_sb_den)
std_b = mt.sqrt(1 /  mean_b_den)

std_sum_sb = mt.sqrt(std_sum_sb)
std_sum_b = mt.sqrt(std_sum_b)

SNR = (sum_sb/sum_b)-1
SNR_string = (((sum_sb/sum_b)-1)/ mt.sqrt((std_sb/sum_sb)*(std_sb/sum_sb)+(std_b/sum_b)*(std_b/sum_b)))

#errore somma è errore in quadratura: todo
print("sum signal + background: ", sum_sb, " +- ", std_sum_sb)
print ("mean signal + background: ", mean_sb, " +- ", std_sb)
print("sum background: ", sum_b, " +- ", std_sum_b)
print ("mean background: ", mean_b, " +- ", std_b)
print("SNR: ", SNR)
print("SNR_string: ", SNR_string)
