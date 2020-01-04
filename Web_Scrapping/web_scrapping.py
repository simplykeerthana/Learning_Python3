#web scrapping in python
#grabbing the data from the website
# downloading the webpage, gabbing the data from the webpage, cleanign it up and sso it is useful data


#use cases of web scrapping
# http://www.entropywebscraping.com/2017/01/01/big-list-web-scraping-uses/

#robot.txt simply says what can be scrapped from a webpage. 
#there exists chrome plugins that allow you to web scraper
# check the website terms and conditions before you web scrape

#how google bot works. Google uses to index website


#hacker news project... scrape articles that have more than 100 points

#beautiful soup is a library for web scrapping
# requests to grab html file

import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news') #grab the html website from the server.
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

#print(res.text)

#print(soup.body) #you can grab anything with this, soup.body, soup.heading
#print(soup.contents)

#css selector is a list of attributes to grab elements from a web page

#print(soup.select('.score')) #grabs all the scores from the website

#(soup.select('.storylink')[0]) #grabs the first story in the hacker news website

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'])

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                 hn.append({'title':title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))