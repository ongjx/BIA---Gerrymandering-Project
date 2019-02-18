outputdicroom = {}
with open('results.txt', 'r') as f:
    for line in f:
        block = line.strip().split(',')
        if block[-1] not in outputdicroom.keys():
            outputdicroom[block[-1]] = [ float(block[3]), 1 ]
        elif block[-1] in outputdicroom.keys():
            outputdicroom[block[-1]][0] += float(block[3])
            outputdicroom[block[-1]][1] += 1

for k in outputdicroom:
    temp = outputdicroom[k][0] / outputdicroom[k][1]
    outputdicroom[k] = temp

geresults2015 = {}
with open('geresults.csv', 'r') as ge:
    for line in ge:
        temparr = line.strip().split(',')
        if temparr[0] == '2015':
            if temparr[1] not in geresults2015.keys() and temparr[-3] == 'PAP':
                geresults2015[temparr[1]] = float(temparr[-1])
            elif temparr[1] in geresults2015.keys() and temparr[-3] == 'PAP':
                if float(temparr[-1]) > geresults2015[temparr[1]]:
                    geresults2015[temparr[1]] = float(temparr[-1])

results = {}
for k in geresults2015.keys():
    if k in outputdicroom.keys():
        results[k] = ( outputdicroom[k],geresults2015[k] )
averageppsm = []
electionresults = []
for line in results.values():
    averageppsm.append(line[0])
    electionresults.append(line[1])

import matplotlib.pyplot as plt
import numpy as np
plt.scatter(averageppsm, electionresults)
plt.xlabel('Average $psm')
plt.ylabel('Winning Percentage')
plt.title('Price Per Square Meter to Winning Percentage')
# plt.plot(np.unique(electionresults), np.poly1d(np.polyfit(electionresults, averageppsm, 1))(np.unique(electionresults)))
plt.plot(averageppsm, np.poly1d(np.polyfit(averageppsm, electionresults, 1))(averageppsm))
plt.show()

import pandas as pd
import statsmodels.api as sm
output1 = sm.OLS(averageppsm, sm.add_constant(electionresults)).fit()
with open('OLS results.txt', 'w+') as out:
    out.write(output1.summary().as_text())