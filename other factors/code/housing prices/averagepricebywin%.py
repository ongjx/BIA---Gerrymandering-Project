prices = {}
with open('results.txt', 'r') as f:
    for line in f: 
        temparr = line.strip().split(',')
        if temparr[-1] not in prices.keys():
            prices[temparr[-1]] = [ float(temparr[-2]) ]
        else:
            prices[temparr[-1]].append( float(temparr[-2]) )

