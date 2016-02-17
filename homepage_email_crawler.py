import re, urllib
import urllib2
from bs4 import BeautifulSoup
import csv

mailtos = []
i=0
with open('locations.csv', 'rb') as csvfile:
    lines = csv.reader(csvfile, delimiter=';', quotechar='|')
    for line in lines:
        print i
        if len(line) > 1:
            if "http" in line[3]:
                try:
                    r = urllib2.urlopen(line[3]).read()
                    soup = BeautifulSoup(r, 'html.parser')
                    for url in soup.find_all("a", href=True):
                        if "mailto" in url["href"] and not "javascript" in url["href"]:
                            if url["href"] not in mailtos:
                                print url["href"].strip()
                                mailtos.append(url["href"].strip())
                                f = open('mailtos.txt', 'a')
                                f.write(url["href"].strip() + "\n")
                                f.close()
                except:
                    print "failed with " + str(line[3])
        i+=1

print len(mailtos)