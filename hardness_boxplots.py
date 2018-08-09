# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 16:10:04 2018

@author: Luke Rollings

Script for producing box plots of hardness distributions measured from a number of specimens

Modify working directory, number of points and number of samples

Change labels for plots and number of digits to remove from filenames where appropriate
"""

import os
import numpy as np
import xml.etree.ElementTree as ET
import pandas as pd
import glob
import matplotlib.pyplot as plt


os.chdir('E:\\nuffield_project\\Hardness_Measurements') #Working Directory

n = 27 #number of indents

N = 7 #number of samples


#Setup

x = np.arange(0, n, 1)
h = np.empty([n,N]) #set up an empty array for all data points to be added to

filenames = glob.glob('*.spe') #read all .spe files

I = 0 #Iteration counter

for f in filenames:
    
    hardness = [] #define a blank list to add data to

    #read .spe files as .xml files, specify root
    tree = ET.parse(f)
    root = tree.getroot()
    
    i = 0 #Second iteration counter
    
    print(f) #Current file
    
    while i < n:
        
        HV = float(root[6][i+24][0].text) #Pulls hardness values from .xml tree
        
        print(i, HV)
        
        hardness.insert(i, HV) #list of hardness values for file f
        
        i = i+1
        
    filenames[I] = float(filenames[I][:-5]) #converts file names into floating point variables of cooling rates
    
    h[:,I] = hardness #insert hardness data for file f into global array h, in column I
    
    df = pd.DataFrame(h, columns=filenames) #convert global array into dataframe
    
    I = I+1
    
    hardness = np.array(hardness) #convert hardness list into arrray
    
    plt.figure(I, figsize=(10,5))
    plt.plot(x, hardness)
    plt.title(str(f[:-5])+"\u2103/second")
    plt.ylim(300, 750)
    plt.xlabel("indent number")
    plt.ylabel("vickers hardness")
    plt.savefig(str(f[:-5])+".png")
    
print(df)

plt.figure(I+1, figsize=(10,5))
boxplot = df.boxplot(column=sorted(filenames))
plt.xlabel("Cooling rate (\u2103/second)")
plt.ylabel("Vickers Hardness")
plt.savefig("boxplot.png")
