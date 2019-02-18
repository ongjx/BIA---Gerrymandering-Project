import requests
from bs4 import BeautifulSoup
# e.g. <h4><a href="/mps/constituency/details/ang-mo-kio-grc">Ang Mo Kio GRC</a></h4>

with open('test.txt', 'r') as f:
    for line in f:
        address = line.strip().split(',')
        postalcode = address[-1]
        params = {"SearchKeyword":postalcode}
        response = requests.post('https://www.parliament.gov.sg/mps/find-my-mp', data=params)
        soup = BeautifulSoup(response.text, 'html.parser')

        temp = (soup.findAll('h4'))
        tempstr = str(temp[-1])
        # tempstr = '<h4><a href="/mps/constituency/details/jurong-grc">Jurong GRC</a></h4>'
        for i in range(len(tempstr)):
            if tempstr[i] == '>' and tempstr[i + 1] != '<':
                start = i + 1
                break
        for i in range(len(tempstr)):
            if tempstr[i] == '<' and tempstr[i - 1] != '>':
                end = i
        result = tempstr[start:end]
        address.append(result[:-4])
        address = ','.join(address)
        output = open('results.txt', 'a')
        output.write(address)
        output.write('\n')
