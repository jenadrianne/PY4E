import urllib.request as ur
from bs4 import BeautifulSoup

url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = ur.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
href = soup('a')

for i in range(count):
    link = href[position].get('href', None)
    print (href[position].contents[0])
    html = ur.urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')
