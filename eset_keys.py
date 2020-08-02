from urllib.request import Request, urlopen
import sys
import ssl
import re
from bs4 import BeautifulSoup


def filterKeys(data):
    patX = r'<p>([\w\d\-]+)<\/p>'
    keys_list = re.findall(patX, data)
    ex_keys = ''
    for key_ in keys_list:
        ex_keys = ex_keys + key_ + '\n'
    return ex_keys

def getWebData():
    url = 'https://t2bot.ru/en/esetkeys/'
    data = urlopen(url=url).read()
    return str(data)

def BeautifulSoup_HTML(data):
    x_data = ''
    bSoup = BeautifulSoup(data, 'html.parser')
    for text in bSoup.find_all('p'):
       x_data = x_data + str(text) + '\n'
    return x_data
    

def main():
    unFiltered_data = BeautifulSoup_HTML(getWebData())
    eset_keys = filterKeys(unFiltered_data)
    with open('ESET_Keys.txt', 'w') as file:
        file.write(eset_keys)

if __name__ == '__main__':
    main()
    sys.exit(0)
