import csv
import requests
from bs4 import BeautifulSoup
import re 

"""

Used Beautiful Soup to scrape the softball data from the Big10 Website and wrote the data in a csv file.

"""

URL = "http://sagarin.com/mills/mlb2006.htm"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

pre = soup.find('pre')
data_p1 = pre.prettify()[:100000]
data_p2 = pre.prettify()[100000:124699]
data_p3 = pre.prettify()[124699:]

"""

    Using regular expression to separate the data before I put it in a csv file.

"""

def prepare_data(data):
    cleaned_data = "|".join(data.split(' '))
    pattern = r'\|([^|]+)\|'
    result = re.findall(pattern, cleaned_data)

    saragin_data = []
    lst = []
    for item in result:
        if item not in [ 'WIN', 'LOSS', 'NET', 'PWA', 'POINTS', 'POINTS', 'POINTS', 'SITUATIONS', [],'AVERAGE</b>\n<b>league','POINTS</b>\n']:
            if '\n' in item:
                if len(lst) == 10:
                    saragin_data.append(lst)
                lst=[]
            else:
                lst.append(item)
    return saragin_data

data_p1 = prepare_data(data_p1)
data_p2 = prepare_data(data_p2)
data_p3 = prepare_data(data_p3)


"""

    Write data in a csv file.

"""

# should be ten items in each list

with open('../SI_311/homework/hw3/data/saragin_data.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Player Number', 'Player Info', 'Mills PWA', 'Win Points', 'Loss Points', 'Net Points', 'Situations', '=', 'Average Points', 'Player Info 2'])
    writer.writerows(data_p1)
    writer.writerows(data_p2)
    writer.writerows(data_p3)
