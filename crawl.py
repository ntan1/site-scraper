import scrape
import time

guitars=['Epiphone', 'Yamaha', 'Fender', 'Dean', 'Stagg', 'Ibanez']
write_to = "guitars.json"

scrape.clearFile(write_to)

for guitar in guitars:
    url = "https://www.amazon.ca/s/ref=sr_in_-2_p_89_29?fst=as%3Aoff&rh=n%3A6916844011%2Cn%3A8396311011%2Cn%3A8396312011%2Cn%3A8396314011%2Ck%3Aguitar%2Cp_89%3A"+guitar+"&bbn=8396314011&keywords=guitar&ie=UTF8&qid=1518130386&rnid=2528832011"
    print(url)
    scrape.scrape(url, write_to, False)
    time.sleep(2)

"https://www.amazon.ca/s/ref=sr_in_-2_p_89_29?fst=as%3Aoff&rh=n%3A6916844011%2Cn%3A8396311011%2Cn%3A8396312011%2Cn%3A8396314011%2Ck%3Aguitar%2Cp_89%3AEpiphone&bbn=8396314011&keywords=guitar&ie=UTF8&qid=1518130386&rnid=2528832011"