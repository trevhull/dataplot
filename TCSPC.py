# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:51:00 2017

@author: trevario

Automatically plot TCSPC data using matplotlib.pyplot
"""



import glob, os
import numpy as np
import matplotlib.pyplot as plt
import csv
#%matplotlib inline

print("what directory are the files in?")
name = input()
os.chdir('/home/trevario/Documents/Labnotebook/TCSPC/' + str(name))


spt = glob.glob("*.dat")

for i in range(len(spt)):
    
    data = np.genfromtxt(str(spt[i]),skip_header=2)

    #this size is in inches
    plt.figure(figsize=(5, 3), dpi=240)
    
    #get those labels right
    sps = spt[i]
    plt.title(str(sps[:-4]), fontsize=16)
    with open(str(sps), encoding="latin_1") as bunch:
        spamreader = csv.reader(bunch, delimiter='\t')
    
        col_1 = list(zip(*spamreader))[0]
    xaxis = col_1[1]
    plt.xlabel(str(xaxis), fontsize=12)
    with open(str(sps), encoding="latin_1") as bunch:
        spamreader = csv.reader(bunch, delimiter='\t')
    
        col_2 = list(zip(*spamreader))[1]
    yaxis = col_2[1]
    plt.ylabel(str(yaxis), fontsize=12)
    
    #change the plotted data if you want
    #plt.ylim(0,15000)
    #TCSPC data does not need to be inverted, ignore this line
    #plt.gca().invert_xaxis()
    
    #tell it you wanna change the axes
    ax = plt.subplot(1,1,1)
    
    #get rid of top and right axes
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    #get rid of the ticks on the top and right axis
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    
    #set size of font for data labels
    ax.tick_params(axis='both', which='major', labelsize=10)
    
    #set thickness of axes
    ax.spines['left'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    
    #make room for the labels
    plt.tight_layout()
    plt.gcf().subplots_adjust(left=0.15)
    
    #show the plot
    plt.plot(data[:,0],data[:,1], color = "blue", linewidth=2.0)
    
    #save the plot
    plt.savefig(str(spt[i]) + ".png", dpi=240)
    
    plt.show()
