from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

data = None
#open the results file
with open('out_model1/result.txt') as f:
    #Parse the results file in a array, each line is a element of the array element are separated by a '|', there are some space 
    # so we remove them a line is like this : |./out_model1/Instance120.1.txt   | 28159.0 | FEASIBLE | 77297.0 | 36 | 2147483647 | 180.21 |
    lines = [line.replace(' ', '').split('|') for line in f]
    #remove empty element in lines 
    for line in lines:
        for e in line:
            if e == '':
                line.remove(e)
            if e == '\n':
                line.remove(e)
    #no header in the file so we create one
    header = ["Instance Name", "Linear", "Status", "Solution","Ratio", "Nodes", "Time"]
    #create a dataframe with the array and the header
    df = pd.DataFrame(lines, columns=header)
    # print(df)
    data = df


#sort time in increasing order
data = data.sort_values(by=['Time'])
#plot ratio in function of time, only points, green color for OPTIMAL, red for FEASIBLE
# the plot must be along a linear x 

#float
data['Ratio'] = data['Ratio'].astype(float)
data['Time'] = data['Time'].astype(float)

#plot
plt.scatter(data['Time'], data['Ratio'], c=data['Status'].map({'OPTIMAL': 'green', 'FEASIBLE': 'red'}))
plt.xlabel('Time(s)')
plt.ylabel('linear/value (%)')
plt.title('Ratio in function of time')
#LEGENDS FOR COLORS
import matplotlib.patches as mpatches
OPTIMAL = mpatches.Patch(color='green', label='OPTIMAL')
FEASIBLE = mpatches.Patch(color='red', label='FEASIBLE')
plt.legend(handles=[OPTIMAL, FEASIBLE])

plt.show()


data2 = None
#open the results file
with open('out_model2/results.txt') as f:
    #Parse the results file in a array, each line is a element of the array element are separated by a '|', there are some space 
    # so we remove them a line is like this : |./out_model1/Instance120.1.txt   | 28159.0 | FEASIBLE | 77297.0 | 36 | 2147483647 | 180.21 |
    lines = [line.replace(' ', '').split('|') for line in f]
    #remove empty element in lines 
    for line in lines:
        for e in line:
            if e == '':
                line.remove(e)
            if e == '\n':
                line.remove(e)
    #no header in the file so we create one
    header = ["Instance Name", "Linear", "Status", "Solution","Ratio", "Nodes", "Time"]
    #create a dataframe with the array and the header
    df = pd.DataFrame(lines, columns=header)
    # print(df)
    data2 = df


#sort time in increasing order
data2 = data2.sort_values(by=['Time'])
#plot ratio in function of time, only points, green color for OPTIMAL, red for FEASIBLE
# the plot must be along a linear x 

#float
data2['Ratio'] = data2['Ratio'].astype(float)
data2['Time'] = data2['Time'].astype(float)

#plot Time data and data2 on for each instance compare
X = np.arange(1, len(data['Time'])+1)

plt.scatter(X, data['Time'], c='blue')
plt.scatter(X, data2['Time'], c='red')
plt.xlabel('Instance')
plt.ylabel('Time(s)')
plt.title('Time in function of instance for each model')
#LEGENDS FOR COLORS
import matplotlib.patches as mpatches
OPTIMAL = mpatches.Patch(color='blue', label='Model 1')
FEASIBLE = mpatches.Patch(color='red', label='Model 2')
plt.legend(handles=[OPTIMAL, FEASIBLE])




plt.show()


#plot Ratio data and data2 on for each instance compare
#sort ratio
data = data.sort_values(by=['Ratio'])
data2 = data2.sort_values(by=['Ratio'])

X = np.arange(1, len(data['Ratio'])+1)

plt.scatter(X, data['Ratio'], c='blue')
plt.scatter(X, data2['Ratio'], c='red', s=10)
plt.xlabel('Instance')
plt.ylabel('Ratio')
plt.title('Ratio in function of instance for each model')
#LEGENDS FOR COLORS
import matplotlib.patches as mpatches
OPTIMAL = mpatches.Patch(color='blue', label='Model 1')
#reduce size of the points
FEASIBLE = mpatches.Patch(color='red', label='Model 2')
plt.legend(handles=[OPTIMAL, FEASIBLE])

plt.show()
