import requests
from bs4 import BeautifulSoup
response = requests.get('https://wuzzuf.net/search/jobs/?q=machine+learning&a=hpb')
soup = BeautifulSoup(response.content, 'lxml')
title = soup.find("h2", {'class': 'css-m604qf'})
titles = soup.find_all("h2", {'class': 'css-m604qf'})
titles_lst = [title.a.text for title in titles]
links = [('https://wuzzuf.net' + title.a['href']).replace(' ', '%20') for title in titles]
occupations = soup.find_all("div", {'class': 'css-1lh32fc'})
occupations_lst = [occupation.text for occupation in occupations]
companies = soup.find_all("a", {'class': 'css-17s97q8'})
companies_lst = [company.text for company in companies]
scraped_data = {}
scraped_data['Title'] = titles_lst
scraped_data['Link'] = links
scraped_data['Occupation'] = occupations_lst
scraped_data['Company'] = companies_lst
import pandas as pd
df = pd.DataFrame(scraped_data)
print (df)
#ahmeadel
