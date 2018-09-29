###############################################################################
###############################################################################
##---------------------------------------------------------------------------##
##Date the file was last edited  : 9/12/2018                                 ##
##---------------------------------------------------------------------------##
##Programmer			 :Anurag Dhungel                             ##
##---------------------------------------------------------------------------##
##Contact			 :pranavlife09@gmail.com                     ##
##---------------------------------------------------------------------------##
###############################################################################
###############################################################################

#imports the required things in the code
from __future__ import division
import matplotlib.pyplot as mplot
import numpy as np

#opening the data file in read mode
data=open("LimeBison_ch1.csv","r")  
data=data.read()
data=data.split("\n")  #splitting the data by line
data.pop()  #deleting the end  ' ' character that's visible in the data file

amplitude=[]  #declaring a list to store the amplitudes
time=[]  #declaring a list to store the time
#using the proper structured data's frequency
frequency=np.float64("73.608125")  

#looping through file contents
for counter in range(0,len(data)):
    
    data[counter]=data[counter].split(",")  #splits each line by commas 
    
    #selects the data from correct frequency
    if np.float64(data[counter][2])==frequency:  
        
        #stores time from correct frequency
        time.append(np.float64(data[counter][0])) 
        #stores amplitude from correct frequency
        amplitude.append(np.float64(data[counter][1]))  

#scatter plots the entire data (time vs amplitude)        
mplot.scatter(time,amplitude,color="red", marker="o")   

#deletes duplicate values in time and stores unique value in timeFunction   
timeFunction=[]
for counterTime in range(0, len(time)):
    count=0# recycles count
    if counterTime==0:
        timeFunction.append(time[counterTime]) #adds the first value 
    for counterTimeFunction in range(0,len(timeFunction)):
        #check for duplicate values
        if time[counterTime]==timeFunction[counterTimeFunction]:
              count=count+1# checks number of repetation
    if count==0: # if no match found on the time , adds value to timeFunction
        timeFunction.append(time[counterTime])      
             
#creates a list to store average amplitude corresponding unique time 
amplitudeFunction=[]  

#loops through the unique time list
for counterTimeFunction in range(0,len(timeFunction)):  
    count=0  # initilizes repeates and sets it to zero in every loop
    averageAmplitude=0  #same as above with amplitude
    for counterTime in range(0,len(time)):  #loops through the list time
        #checks the time list's duplicate in timeFunction
        if timeFunction[counterTimeFunction]==time[counterTime]:   
             # adds the amplitude correspoding same time
            averageAmplitude=averageAmplitude+amplitude[counterTime]  
            count=count+1 #counts number of amplitudes for each time varialbe
    
    # average outs the amplitude for each time     
    averageAmplitude=averageAmplitude/count   
    #stores the average amplitues corresponding to the time lists
    amplitudeFunction.append(averageAmplitude)   

 #plots a curve of time vs average amplitude
mplot.plot(timeFunction,amplitudeFunction, color="blue", linestyle="-") 

#readiblity of graph
mplot.title("Amplitude vs Time Graph" )  #gives tile to the graph
mplot.xlabel("Milliseconds")  #labels thes axis
mplot.ylabel("Amplitude")  # labels the y axis
mplot.ylim((-1.5,1.5))  # provides the range for y axis
mplot.xlim((-200,1200))  #provides the range for x-axis
mplot.show()  #displays the graph
