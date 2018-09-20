import urllib.request
from bs4 import BeautifulSoup
import os

url = "https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015"
source_code = urllib.request.urlopen(url)
soup = BeautifulSoup(source_code, "html.parser")
file = open("output.txt","w")
for table in soup.findAll('table'):
    for row in table.findAll('tr'):
        file.write("\n")
        for col in row.findAll('td'):
            if(col.string != None):
                file.write(col.string)
                file.write(" ")
file.close()


