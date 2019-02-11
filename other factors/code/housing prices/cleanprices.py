output = []

geresults = {}
with open('geresults.csv', 'r') as ge:
    for line in ge:
        seat = line.strip().split(",")
        if seat[0][:4] == '2015':
            if seat[1] not in geresults.keys():
                geresults[seat[1]] = float(seat[-1])
            elif float(seat[-1]) > float(geresults[seat[1]]):
                geresults[seat[1]] = float(seat[-1])

with open('results.txt', 'r') as f:
    for line in f:
        temparr = line.strip().split(',')
        if temparr[-1] in geresults.keys():
            output.append( (float(temparr[-3]), geresults[temparr[-1]]) )

x = []
y = []
for line in output:
    x.append(line[0])
    y.append(line[1])

import matplotlib.pyplot as plt
import numpy as np
plt.scatter(y, x)
plt.ylabel('Price Per Squaremeter')
plt.xlabel('Winning Percentage')
plt.title('Price Per Square Meter to Winning Percentage')
plt.plot(y, np.poly1d(np.polyfit(y, x, 1))(y))
plt.show()

import pandas as pd
import statsmodels.api as sm
output1 = sm.OLS(y, sm.add_constant(x)).fit()
with open('OLS results.txt', 'w+') as out:
    out.write(output1.summary().as_text())