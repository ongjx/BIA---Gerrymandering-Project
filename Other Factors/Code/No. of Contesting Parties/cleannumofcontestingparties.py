data = []
with open('geresults.csv', 'r') as f:
    next(f)
    for line in f:
        temparr = line.strip().split(',')
        if len(temparr) != 7: # some names got comma so must remove them
            temparr[3] = temparr[3] + temparr[4]
            temparr.pop(4)
            temparr[0] = temparr[0] + ' ' + temparr[1]
            temparr.pop(1)
            data.append(temparr)
        else:
            data.append(temparr)
            temparr[0] = temparr[0] + ' ' + temparr[1]
            temparr.pop(1)

results = {}
for line in data:
    if line[0] not in results.keys():
        if line[5] != 'na':
            results[line[0]] = [ (line[3],float(line[5])) ] # [ (contesting party, percentage of votes), count_of_contesting_parties ]
        # else:
        #     results[line[0]] = [ (line[3],1) ]
    else:
        results[line[0]].append( (line[3],float(line[5])) )
axis = []
for k in results.keys():
    highest = 0
    for pair in results[k]:
        if pair[1] > highest:
            highest = pair[1]
    axis.append( ( len(results[k]), highest ) )
# for k in results.keys():
#     for val in results[k]:
#         if val[1] == 1:
#             print (k, results[k])

x = []
y = []
for pair in axis:
    x.append(pair[0])
    y.append(pair[1])

import pandas as pd
import statsmodels.api as sm
output1 = sm.OLS(x, sm.add_constant(y)).fit()
with open('OLS results.txt', 'w+') as out:
    out.write(output1.summary().as_text())

import matplotlib.pyplot as plt
import numpy as np
plt.scatter(x, y)
plt.xlabel('Number of Contesting Parties')
plt.ylabel('Winning Percentage')
plt.title('Number of Contessting Parties to Winning Percentage')
plt.plot(x, np.poly1d(np.polyfit(x, y, 1))(x))
plt.show()