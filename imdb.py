# @time    : 2017/12/7 10:01
# @Author  : chiew
# @File    : imdb.py

import requests
from bs4 import BeautifulSoup

url = "http://www.imdb.com/chart/top"
html = requests.get(url)
content = html.text

soup = BeautifulSoup(content, "html.parser")
soup.prettify()
tr = soup.select('.titleColumn')

for i in range(250):
    for string in tr[i].stripped_strings:
        print(string, end='')
    print('')
