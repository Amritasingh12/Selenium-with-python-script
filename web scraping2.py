import requests
from bs4 import BeautifulSoup as bs
import csv
URL ='https://www.flipkart.com/audio-video/headphones/~cs-53mrbtcuf5/pr?sid=0pm%2Cfcn&p%5B%5D=facets.headphone_type%255B%255D%3DIn%2Bthe%2BEar&otracker=categorytree&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.brand%255B%255D%3DboAt'
req = requests.get(URL)
soup = bs(req.text,'html.parser')
 
titles = soup.find_all('', attrs={'class', 'head'})
titles_list = []
count = 1
for title in titles:
    d = {}
    d['Title Number'] = f'Title {count}'
    d['Title Name'] = title.text
    count += 1
    titles_list.append(d)

print(titles_list)
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Title Number','Title Name'])
    w.writeheader() 
    w.writerows(titles_list)
