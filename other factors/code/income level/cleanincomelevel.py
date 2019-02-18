ge2015 = {}
with open('geresults.csv', 'r') as f:
    next(f)
    for line in f:
        temparr = line.strip().split(',')
        if temparr[0] == '2015':
            name = temparr[1]
            winrate = float(temparr[-1])
            if name not in ge2015.keys():
                ge2015[name] = winrate
            elif name in ge2015.keys() and winrate > ge2015[name]:
                ge2015[name] = winrate
print (ge2015)
