from bs4 import BeautifulSoup as bs
import requests as r
import re
import json

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

    if overwrite==True:
        o = "w"
    else:
        o = "a"

    with open(write_to_filename, o) as f:
        for item in item_list:
            title = item.find('h2').getText()
            brand = item.find('div', 'a-spacing-mini').findAll('span', re.compile("secondary"))[1].getText()
            # get only the number from the price, removes currency shortname and dollar sign
            price = re.sub(("[A-z $]"),"",item.find('span', re.compile("price")).getText())
            img = item.find('img').get('src')

            try:
                stars = item.find('span', string=re.compile("star")).getText()
            except AttributeError:
                stars = ""

            try:
                num_of_reviews = item.find('a', href=re.compile("customerReviews")).getText()
            except AttributeError:
                num_of_reviews = ""

            doc = {
                'title': title,
                'brand': brand,
                'price': price,
                'img': img,
                'rating': {
                    'stars': stars,
                    'num_of_reviews': num_of_reviews
                }
            }
            print(doc)
            json.dump(doc, f)

    #     doc = {
    #         'title': title,
    #         'brand': brand,
    #         'price': price,
    #         'img': img,
    #         'rating': {
    #             'stars': stars,
    #             'num_of_reviews': num_of_reviews
    #         }
    #     }
    #     docs.append(doc)
    #     print(title, "\n")

    # if(overwrite == True):
    #     with open(write_to_filename, 'w') as f:
    #         json.dump(docs, f)
    # else:
    #     with open(write_to_filename, 'a') as f:
    #         json.dump(docs, f)

def clearFile(filename):
    open(filename, 'w').close()

# test scrape
# scrape("https://www.amazon.ca/s/ref=sr_in_-2_p_89_29?fst=as%3Aoff&rh=n%3A6916844011%2Cn%3A8396311011%2Cn%3A8396312011%2Cn%3A8396314011%2Ck%3Aguitar%2Cp_89%3AYamaha&bbn=8396314011&keywords=guitar&ie=UTF8&qid=1518130386&rnid=2528832011", "guitars.json", True)
"https://www.amazon.ca/s/gp/search/ref=sr_nr_p_89_7?fst=as%3Aoff&rh=n%3A6916844011%2Cn%3A8396311011%2Cn%3A8396312011%2Cn%3A8396314011%2Ck%3Aguitar%2Cp_89%3AGibson+Gear&keywords=guitar&ie=UTF8&qid=1518120932"
"https://www.amazon.ca/s/gp/search/ref=sr_nr_p_89_8?fst=as%3Aoff&rh=n%3A6916844011%2Cn%3A8396311011%2Cn%3A8396312011%2Cn%3A8396314011%2Ck%3Aguitar%2Cp_89%3AEpiphone&keywords=guitar&ie=UTF8&qid=1518120971"