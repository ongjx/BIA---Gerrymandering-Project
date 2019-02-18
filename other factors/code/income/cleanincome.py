gedata = []
with open('geresults.csv', 'r') as f:
    next(f)
    for line in f:
        temparr = line.strip().split(',')
        if temparr[0] == '2015':
            if temparr[1] not in gedata:
                
                gedata.append(temparr[1])
print (gedata)