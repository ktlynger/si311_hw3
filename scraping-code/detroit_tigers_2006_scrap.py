import csv
import requests
from bs4 import BeautifulSoup
import re 

URL = "https://www.baseball-reference.com/teams/DET/2006.shtml"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

batting_data = soup.find('div', id='all_team_batting')
batting_headers = batting_data.find('thead')
batting_headers = [item.text.replace('\n', '').strip() for item in batting_headers]
data_body = batting_data.find('tbody')
# data = [stat.text for stat in batting_data.find_all('th')]
for stat in data_body:
    print(stat.findall('th'))
pattern = r'((C|1B|2B|SS|3B|LF|CF|RF|DH|OF|MI|IF|P)([A-Za-záéíóúÁÉÍÓÚ\s]+)(\*|#|\d))'
batter_data = [re.findall(pattern, stat.text[1:]) for stat in data_body if re.findall(pattern, stat.text[1:]) != []]
batter_data = [[item[1], item[2], item[3]] for sublist in batter_data for item in sublist if len(item)== 4]


# pitcher data
pitching_data = soup.find('div', id='all_team_pitching')
pitching_headers = pitching_data.find('thead')
pitching_headers = [item.text.replace('\n', '').strip() for item in pitching_headers]
pitching_body = pitching_data.find('tbody')
# data = [stat.text for stat in batting_data.find_all('th')]

pattern = r'(SP|CL|RP)([A-Za-záéíóúÁÉÍÓÚ\s]+)(\*|#|\d)'
pitcher_data = [re.findall(pattern, stat.text[1:]) for stat in pitching_body if re.findall(pattern, stat.text[1:]) != [] and re.findall(pattern, stat.text[1:]) != [('FI', 'P\n         WHIP\n         H', '9'), ('H', 'R', '9'), ('B', 'B', '9'), ('S', 'O', '9')]]
pitcher_data = [[item[0], item[1], item[2]] for sublist in pitcher_data for item in sublist if len(item)== 3]
"""

NOTE: The code does not work entirely right for either but it will be easier for me to fix in pandas then here. 
I got what I need to move on for now :)

"""

"""
Now I will put it into a csv file.

"""

with open('../SI_311/homework/hw3/data/batting_data_tigers_2006.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Pos', 'Name', 'Extra'])
    writer.writerows(batter_data)

with open('../SI_311/homework/hw3/data/pitching_data_tigers_2006.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Pos', 'Name', 'Extra'])
    writer.writerows(pitcher_data)




