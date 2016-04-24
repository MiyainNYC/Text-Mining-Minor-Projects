import gc
import csv
import re
import mmap
import sys
import urllib2
from bs4 import BeautifulSoup

def ScrapeData(filename):
    file = open(filename, 'r')
    print "opening file ", filename
    counter = 0
    reader = file.read()
    s = mmap.mmap(file.fileno(),0,access=mmap.ACCESS_READ)
    print "File has been read. length: ", len(reader)
    newfile = raw_input("What will be the new csv file? \n")
    csvfile = csv.writer(open(newfile,'wb'))
    for div in re.finditer(ur'<div class="user-thread"(.*?)</a></span></li>',reader,re.DOTALL):
         counter = counter + 1
         record = reader[div.start():div.end()]
         user = re.search(ur'<b>(.*?)</b>+?', record, re.DOTALL)
         if user is None:
              user = re.search(ur'<li class="uname2">(.*?)</li>+?', record, re.DOTALL)
         postDate = re.search(ur'<li class="upost"><time>(.*?)</time>+?', record,re.DOTALL)
         opinion = re.search(ur'<p class="uopin">(.*?)</p>+?',record, re.DOTALL)
         if opinion:
              replyto = re.search(ur'<a class="uinreply"(.*?)</a></span>+?',record, re.DOTALL)
              if replyto:
                   reply = re.search(ur'more</a></span>(.*?)</p>+?',record, re.DOTALL)
                   if reply:
                        csvfile.writerow(['reply',user.group(1), postDate.group(1), reply.group(1)])
              elif re.search(ur'<span class="uinreply"(.*?)</a></span>+?',record, re.DOTALL):
                   replytospan = re.search(ur'<span class="uinreply"(.*?)</p>+?',record, re.DOTALL)
                   if replyto:
                        spanreply = re.search(ur'</span>(.*?)</p>+?',str(replyto.group(1)),re.DOTALL)
                        csvfile.writerow(['span reply',user.group(1), postDate.group(1), spanreply.group(1)])
              else:
                   csvfile.writerow(['new post',user.group(1), postDate.group(1),opinion.group(1)])
    gc.collect()
    file.close()
    print "scraping complete."

def CrawlPages():
    pageCounter = input("from page: ")
    limit = input("to page: ")
    appender = raw_input("enter filename appender: ")
    txtfilename = 'galaxyS6-' + appender + '.txt'
    while pageCounter > limit:
        #348
        url = ('http://www.gsmarena.com/samsung_galaxy_s6-reviews-6849p' + str(pageCounter) + '.php')
        ourUrl = urllib2.urlopen(url)
        soup = BeautifulSoup(ourUrl, "html.parser")
        new_string = soup.findAll(attrs={'class' : re.compile("user-thread$")})
        with open (txtfilename,'a') as txtfile:           
            txtfile.write(str(new_string))
        pageCounter = pageCounter - 1
        print pageCounter
    print "file write completed."
    txtfile.close()
    print txtfilename
    ScrapeData(txtfilename)
    
    if raw_input("run again? Y/N \n") == 'Y':
        CrawlPages()

CrawlPages()

