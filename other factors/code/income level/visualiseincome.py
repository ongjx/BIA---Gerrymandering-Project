income = {}
arrincomerange = []
with open('income.csv', 'r') as f:
    next(f)
    for line in f:
        temparr = line.strip().split(',')
        if len(temparr) == 6:
            temparr[1] = temparr[1] + ',' + temparr.pop(2)
            temparr[1] = temparr[1].strip('"')
            temparr[2] = temparr[2].strip('"')
            temparr[3] = temparr[3].strip('"')
        if len(temparr) == 7:
            temparr[1] = temparr[1] + ',' + temparr.pop(2) + ',' + temparr.pop(2)
            temparr[1] = temparr[1].strip('"')
            temparr[2] = temparr[2].strip('"')
            temparr[3] = temparr[3].strip('"')

        if temparr[1] != 'Total':
            name = temparr[-2].strip('"')
            incomerange = temparr[1]
            num = temparr[-1]
            if incomerange not in arrincomerange:
                arrincomerange.append(incomerange)
            if name not in income.keys():
                income[name] = [num]
            else:
                income[name].append(num)

import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
import numpy as np
for k in income.keys():
    plt.plot(arrincomerange, income[k])
plt.show()