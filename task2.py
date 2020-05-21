import string

import nltk as nltk
import urllib3
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

nltk.download('punkt')
nltk.download('stopwords')

http = urllib3.PoolManager()
url = 'https://habr.com/ru/'

r = http.request('GET', url)
soup = BeautifulSoup(r.data.decode('utf-8'), 'html.parser')

text = soup.find_all(text=True)

#print(set([t.parent.name for t in text]))

s = 'str1 | !str2 | !str3'
s_list = s.split(' ')
s_list_01 = []
symbols = ['&','|']

for i_s in range(0,len(s_list)):
    s_list_01.append('')

for symbol in symbols:
    for i_s in range(1, len(s_list) - 1):
        if symbol == '&':
            if s_list[i_s] == '&':
                print(i_s)
                s_list_01[i_s - 1] = 1
                s_list_01[i_s + 1] = 1
        else:# 'str1 | str2 | str3'
            if s_list[i_s] == '|':
                print(i_s)
                if s_list_01[i_s - 1] != 1:
                    s_list_01[i_s - 1] = 2
                if s_list_01[i_s + 1] != 1:
                    s_list_01[i_s + 1] = 2
        print(s_list_01)

for i_s in range(0,len(s_list)):
    if '!' in s_list[i_s]:
        s_list_01[i_s] = -s_list_01[i_s]
        s_list[i_s] = s_list[i_s][1:]

s_final = {s_list[0] : s_list_01[0], s_list[2] : s_list_01[2], s_list[4] : s_list_01[4]}

print(s_final)

#print(s_list_01)


