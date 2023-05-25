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



