import requests
import bs4
from random import randint
from collections import OrderedDict

nick_arr = []
nick_arr_clear = []
root_url = 'http://eune.op.gg/summoner/userName='
summoner_url = 'Broken+Fang'
index_url = root_url + summoner_url
divTag = None
myset = []

def scrape(index_url):
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return soup.find_all('div', {'class':'SummonerName'})

def list_add(divTag):
    for tag in divTag:
        aTags = tag.find_all('a')
        for tag in aTags:
            nick_arr.append(tag.text)

def list_clean(nick_arr):
    return list(set(nick_arr))

def list_print(nick_arr):
    print ('[%s]' % ', '.join(map(str, nick_arr)))

def save_file(array):
    f = open('output.txt', 'a', encoding='utf-8')
    for nick in array:
        f.write('%s\n' % nick)
    f.close()

def choose_random(nick_arr_clear):
    intgr = randint(0,len(nick_arr_clear))
    if not nick_arr_clear[intgr] in myset:
        summoner_url = nick_arr_clear[intgr]
        myset.append(nick_arr_clear[intgr])
        print(summoner_url)
    else:
        choose_random(nick_arr_clear)

def lets_do_this():
    divTag = scrape(index_url)
    list_add(divTag)
    nick_arr_clear = list_clean(nick_arr)
    save_file(nick_arr_clear)
    choose_random(nick_arr_clear)

for x in range(0, 10):
    lets_do_this()
