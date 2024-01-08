import requests
from bs4 import BeautifulSoup as bs4

#Experiments

URL = 'https://billwurtz.com/expert.html'
page = requests.get(URL)

soup = bs4(page.content,"html.parser")
results = soup.find_all('a')
indi_elements = soup.find_all('tr')
word = 'Perfect!'

results_tr = soup.find('tr')
first = results_tr.find('td',recursive=False)
first_text = first.get_text()
next = first.find_next_sibling('td')
#print(first_text)
output = soup.find_all('a',string=word)

def FindItemByDate(date):
    URL = 'https://billwurtz.com/expert.html'
    page = requests.get(URL)
    soup = bs4(page.content,"html.parser")
    results = soup.find_all('tr')
    for i in results:
        first = i.find('td',recursive=False)
        if first.get_text() == date:
            next = first.find_next_sibling('td')
            return next
    return 'Not Found'
        
#Test Cases: 3/3 PASSED
#print(FindItemByDate('1.18.21'))
#print(FindItemByDate('1.15.19'))
#print(FindItemByDate('1.2.20'))

def FindSongByName(input):
    URL = 'https://billwurtz.com/songs.html'
    page = requests.get(URL)
    soup = bs4(page.content,'html.parser')
    output = soup.find_all('a',string=input)
    if len(output) > 0:
        return output[0]
    else:
        return 'Not Found'
    
#print(FindSongByName('fly around'))