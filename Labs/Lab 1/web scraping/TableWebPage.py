import urllib.request
from bs4 import BeautifulSoup
import os

url = "https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015"
source_code = urllib.request.urlopen(url)
soup = BeautifulSoup(source_code, "html.parser")
file = open("output.txt","w")

# get all the content with table tag
for table in soup.findAll('table'):
    # get all the content with tr tag
    for row in table.findAll('tr'):
        file.write("\n")
        # get all the content with tr tag
        for col in row.findAll('td'):
            if(col.string != None):
                # writing content to file
                file.write(col.string)
                file.write(" ")
file.close()


