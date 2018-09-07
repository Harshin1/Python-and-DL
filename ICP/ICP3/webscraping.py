import urllib.request
from bs4 import BeautifulSoup
import os

url = "https://en.wikipedia.org/wiki/Deep_learning"
source_code = urllib.request.urlopen(url)
plain_text = source_code
soup = BeautifulSoup(plain_text, "html.parser")
print(soup.title.string)
for link in soup.find_all('a'):
    print(link.get('href'))