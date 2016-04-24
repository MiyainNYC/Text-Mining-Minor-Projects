import gc
import csv
import re
import mmap

filename = raw_input("What is the filename? \n")
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
         elif re.search(ur'<span class="uinreply">(.*?)+?',record, re.DOTALL):
              replytospan = re.search(ur'<span class="uinreply-msg uinreply-msg-single">(.*?)</p>+?',record, re.DOTALL)
              if replytospan:
                   print len(str(replytospan.group(1)))
                   end = len(str(replytospan.group(1)))
                   start = str(replytospan.group(1)).index('</span>')+len('</span>')
                   spanreply = str(replytospan.group(1))[start:end]
                   print spanreply
                   csvfile.writerow(['span reply',user.group(1), postDate.group(1), spanreply])
         else:
              csvfile.writerow(['new post',user.group(1), postDate.group(1),opinion.group(1)])
gc.collect()
file.close()
print "scraping complete."
