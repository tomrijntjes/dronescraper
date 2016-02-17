import re, urllib
from bs4 import BeautifulSoup
import csv

#textfile = file('depth_1.txt','wt')
myurl = "http://www.out2fun.nl"
j=0
'''
r = urllib.urlopen(myurl + "/groepsuitje/").read()

soup = BeautifulSoup(r, 'html.parser')
content = soup.find_all("div", id="content")

hrefs = []
print "getting hrefs"
for i in soup.find_all("li"):
        if "groepsuitje" in i.find("a")["href"]:
                hrefs.append(myurl + i.find("a")["href"])
print "done getting hrefs"

print "getting location pages"
print len(hrefs)
j = 0
locationPages = []
f = open('locationPages.txt', 'w')
for href in hrefs:
     print j
     j+=1
     f.write("###category: " + href + "###\n")
     r = urllib.urlopen(href).read()
     soup = BeautifulSoup(r, 'html.parser')
     for i in soup.find_all("a"):
        if "Meer informatie" in i.contents[0]:
                locationPages.append(myurl + i["href"])
                f.write(myurl + i["href"] + "\n")



f = open('locationPages.txt', 'r')
g = open('locationPagesUnique.txt', 'w')
locations = []
i = 0
for line in f:
        if "###" not in line:
                if line not in locations:
                        locations.append(line)
                        g.write(line)
                else:
                        print "already in there"
                        i += 1
        else:
                g.write(line)
'''

g = open('locationPagesUnique.txt', 'r')

p = 0
for line in g:
        if "###" not in line:
                title = ""
                url = ""
                phone = ""
                address = ""
                activity_string = ""
                r = urllib.urlopen(line).read()
                soup = BeautifulSoup(r, 'html.parser')
                
                #get title
                title = soup.h1.contents[0].encode('utf-8')
                print str(p) + title
                #get activities and put in comma separated string
                activity_list = [x.text for x in soup.find("div", {"id": "content"}).find_all("li")]
                for activity in activity_list:
                        if activity_string != "":activity_string += "," + str(activity.encode('utf-8')).strip()
                        else: activity_string += str(activity.encode('utf-8')).strip()
                        
                #find address
                contact = soup.find("div", {"class" : "right"})
                address = contact.find_all("div")[0].text.encode('utf-8').strip()
                
                #find website url and phone_number
                for url in contact.find_all("a"):
                        if "http" in url["href"]:
                                url = url["href"]                
                        elif "get_number" in url["href"]:
                            phone_html = urllib.urlopen(myurl+url["href"]).read()
                            phone = str(BeautifulSoup(phone_html, 'html.parser').text.encode('utf-8').strip())    
                
                with open('locations.csv', 'ab') as fp:
                        a = csv.writer(fp, delimiter=';',quoting=csv.QUOTE_MINIMAL)
                        data = [title, activity_string, address, url, phone]
                        a.writerow(data)
        else:
                 with open('locations.csv', 'ab') as fp:
                        a = csv.writer(fp, delimiter=';',quoting=csv.QUOTE_MINIMAL)
                        data = [line.strip()]
                        a.writerow(data)
        p+=1

