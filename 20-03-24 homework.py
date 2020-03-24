import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200309&hh=14&rtm=N&pg=1',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

genie = soup.select("table.list-wrap>tbody>tr")
rank = 0
for name in genie:
        rank = rank + 1
        title = name.select("a")[2].text.lstrip()
        singer = name.select("a")[3].text

        if len(title) > 0:
            print(rank, title, singer)

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200309&hh=14&rtm=N&pg=2',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

genie = soup.select("table.list-wrap>tbody>tr")
rank = 50
for name in genie:
        rank = rank + 1
        title = name.select("a")[2].text.lstrip()
        singer = name.select("a")[3].text

        if len(title) > 0:
            print(rank, title, singer)
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200309&hh=14&rtm=N&pg=3',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

genie = soup.select("table.list-wrap>tbody>tr")
rank = 100
for name in genie:
        rank = rank + 1
        title = name.select("a")[2].text.lstrip()
        singer = name.select("a")[3].text

        if len(title) > 0:
            print(rank, title, singer)
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200309&hh=14&rtm=N&pg=4',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

genie = soup.select("table.list-wrap>tbody>tr")
rank = 150
for name in genie:
        rank = rank + 1
        title = name.select("a")[2].text.lstrip()
        singer = name.select("a")[3].text

        if len(title) > 0:
            print(rank, title, singer)

