import requests
from bs4 import BeautifulSoup

def get_homepages(pages,categories):
    for page,category in zip(pages,categories):
        soup = BeautifulSoup(page, 'html.parser')
        for i in soup.find_all("a"):
           if "Meer informatie" in i.contents[0]:
                   yield ("http://www.out2fun.nl"+i["href"],category)

outfun_urls = [line.rstrip('\n') for line in open('outfun.txt')]
category = [url.split('/')[-2] for url in outfun_urls]
category_pages = (requests.get(url).text for url in outfun_urls)
company_urls = get_homepages(category_pages,category)


with open('locationPagesUnique.txt','w') as f:
    all_urls,last_category = list(),""
    for url in company_urls:
        if url[0] not in all_urls:    
            if url[1] != last_category:
                last_category = url[1]
                f.write("###category: " + url[1] + "###\n")        
            f.write(url[0]+"\n")
            all_urls.append(url[0])
        






