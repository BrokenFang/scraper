import requests
import bs4
from random import randint
import re

root_url = 'http://eune.op.gg/summoner/userName='
summoner_url = 'Broken+Fang'
nick_arr = []
used_nicks = []
endings = ['pl', 'cz', 'srb', 'gr', 'sk', 'xd']

def rchop(thestring, endings):
    for end in endings:
      if thestring.endswith(end):
        return thestring[:-len(end)]
    else:
      return thestring

def clean_my_shit(nickarr, endings):
    for (index, nick) in enumerate(nick_arr):
         nick_arr[index] = rchop(nick,endings)

def scrape(index_url):
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    divTag = soup.find_all('div', {'class':'SummonerName'})
    for tag in divTag:
        aTags = tag.find_all('a')
        for tag in aTags:
            tag.text.replace(" ", "")
            if re.match("^[A-Za-z0-9_-]*$", tag.text):
                nick_arr.append(tag.text.lower())

def choose_random(nick_arr):
    intgr = randint(0,len(nick_arr))
    if not nick_arr[intgr] in used_nicks:
        global summoner_url
        summoner_url = nick_arr[intgr]
        used_nicks.append(nick_arr[intgr])
    else:
        choose_random(nick_arr)

def save_file(array):
    f = open('output.txt', 'a', encoding='utf-8')
    for nick in array:
        f.write('%s\n' % nick)
    f.close()

def lets_go():
    scrape(root_url + summoner_url)
    choose_random(nick_arr)
    print(summoner_url.encode('ascii','ignore'))

for x in range(0,10):
    lets_go()

print(len(nick_arr))
print(len(list(set(nick_arr))))
clean_my_shit(nick_arr, endings)
save_file(list(set(nick_arr)))
