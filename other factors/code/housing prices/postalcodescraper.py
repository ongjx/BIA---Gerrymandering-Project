import requests
from bs4 import BeautifulSoup
import string

addressdata2015 = {}
with open('address.csv','r') as f:
    next(f)
    for line in f:
        clean = line.strip().split(',')
        year = clean[0][:4]
        pricepsm = float(clean[10]) / float(clean[6])
        if year == '2015':
            keyname = clean[2] + ',' + clean[3] + ',' + clean[4]
            if keyname not in addressdata2015.keys():
                addressdata2015[keyname] = [pricepsm, 1]
            else:
                addressdata2015[keyname][0] += pricepsm
                addressdata2015[keyname][1] += 1
for k in addressdata2015.keys():
    temp = addressdata2015[k][0] / addressdata2015[k][1]
    addressdata2015[k] = round(temp, 6)

for k in addressdata2015.keys():
    key = k.split(',')
    building = key[1]
    street =  key[2]
    param = {'building':building, 'street_name':street, 'op':'Find'}
    response = requests.post('https://www.singpost.com./find-postal-code', data=param)
    soup = BeautifulSoup(response.text, 'html.parser')
    # <tr class="odd">
    output = str(soup.findAll('tr',"odd"))
    out = ''
    counter = 0 
    for i in output:
        if i in string.digits:
            out += i
            counter += 1
        if counter == 6:
            break
    real = key[1] + ',' + key[2] + ',' + key[0] + ',' + str(addressdata2015[k]) + ',' + out
    with open('test.txt', 'a') as result:
        result.write(real)
        result.write('\n')