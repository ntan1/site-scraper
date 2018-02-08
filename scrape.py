from bs4 import BeautifulSoup as bs
import requests as r
import time
import urllib
import re
import json

class scrape():

# TODO: remove double quotes from price
# TODO: check escaped chars work on app when retrieved from mongo
# TODO: resolve bad JSON array format on mongoimport (due to double square bracket on append)
    def scrape(url, write_to_filename, overwrite=True):
        '''currently built to scrape Amazon results page

        url: string. url to request
        write_to_filename: string. file to write results to
        overwrite: boolean. True overwrites file, False appends

        '''

        response = r.get(url)
        html = response.text
        soup = bs(html, "html.parser")
        docs = []

        # retrieves all items
        item_list = soup.find_all('li', id=re.compile("^result_"))

        for item in item_list:
            title = item.find('h2').getText()
            # get only the number from the price, removes currency shortname and dollar sign
            price = re.sub(("[A-z $]"),"",item.find('span', re.compile("price")).getText())
            img = item.find('img').get('src')

            doc = {
                'title': title,
                'price': price,
                'img': img
            }
            docs.append(doc)
            print(title, "\n")

        if(overwrite == True):
            with open(write_to_filename, 'w') as f:
                json.dump(docs, f)
        else:
            with open(write_to_filename, 'a') as f:
                json.dump(docs, f)

    #test scrape
    scrape("https://www.amazon.ca/s/ref=sr_nr_n_3?fst=as%3Aoff&rh=n%3A8396312011%2Ck%3Aguitar&keywords=guitar&ie=UTF8&qid=1518072560&rnid=5264023011", "guitars.json", False)