import requests
from bs4 import BeautifulSoup
import string
output = open('test1.txt', 'a')
with open("test.txt", "r") as f:
    for line in f:
        play = line.strip().split(',')
        if play[4] == '':
            building = play[0]
            street =  play[1][4:]
            param = {'building':building, 'street_name':street, 'op':'Find'}
            response = requests.post('https://www.singpost.com./find-postal-code', data=param)
            soup = BeautifulSoup(response.text, 'html.parser')
            tempstr = str(soup.findAll('tr',"odd"))
            out = ''
            counter = 0 
            for i in tempstr:
                if i in string.digits:
                    out += i
                    counter += 1
                if counter == 6:
                    break
            play[4] = out
            temp = ",".join(play)
            print (play)
            output.write(temp)
            output.write('\n')
        else:
            output.write(line)
