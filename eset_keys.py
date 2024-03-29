from urllib.request import Request, urlopen
import sys
import os
import ssl
import re
from bs4 import BeautifulSoup


def filterKeys(data):
    ''' Filter out keys and rearrange from web data. '''
    patX = r'<p>([\w\d\-]+)<\/p>'
    try:
        keys_list = re.findall(patX, data)
        ex_keys = ''
        keys_num = 0
        for key_ in keys_list:
            keys_num += 1
            ex_keys = ex_keys + str(keys_num) + ') ' + key_ + '\n'
        return ex_keys
    except Exception as ex:
        print('Unable to retrive keys!')

def getWebData():
    ''' Get data from web '''
    url = 'https://t2bot.ru/en/esetkeys/'
    try:
        data = urlopen(url=url).read()
        return str(data)
    except Exception as ex:
        print('Please check your internet connection.')

def BeautifulSoup_HTML(data):
    ''' Parse data from web page '''
    x_data = ''
    try:
        bSoup = BeautifulSoup(data, 'html.parser')
        for text in bSoup.find_all('p'):
            x_data = x_data + str(text) + '\n'
        return x_data
    except Exception as ex:
        print('Please install required packages.')
    

def main():
    ''' Main function '''
    unFiltered_data = BeautifulSoup_HTML(getWebData())
    eset_keys = filterKeys(unFiltered_data)
    # Generated key file path
    path_ = 'C:\\Users\\<USER_NAME>\\Desktop\\ESET_Keys.txt'
    path_ = path_.replace('<USER_NAME>', os.getlogin())
    try:
        with open(path_, 'w') as file:
            file.write(eset_keys)
        print('Keys saved. Location: {0}'.format(path_))
    except Exception as ex:
        print('No keys generated.')

if __name__ == '__main__':
    main()
    sys.exit(0)
