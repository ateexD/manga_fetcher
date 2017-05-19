# coding: utf-8
from __future__ import print_function
import urllib,bs4,os,sys
manga_name="boruto"
pathx="./Manga/"+manga_name
start_point=1
if not os.path.exists(pathx):
    os.makedirs(pathx)
else:
    start_point=len(os.listdir(pathx))+1
u=urllib.urlopen("http://www.mangahit.com/"+manga_name+"/1/1")
u=u.read()
bo=bs4.BeautifulSoup(u,"lxml")
chapter_num=bo.text.count("Chapter")
print_flag=1
if start_point == chapter_num:
    print_flag=None
    print("You're up to date!")
for c in xrange(start_point,chapter_num):
    if not os.path.exists(pathx+"/Chapter-"+str(c)):
        os.mkdir(pathx+"/Chapter-"+str(c))
    u=urllib.urlopen("http://www.mangahit.com/"+manga_name+"/"+str(c)+"/"+str(1))
    u=u.read()
    bo=bs4.BeautifulSoup(u,"lxml")
    page_num_pos=bo.text[::-1].find("egaP")
    page_num=int(bo.text[-1*page_num_pos:].split("\n")[2][-2:])
    print ("Reading Chapter : "+str(c))
    print ("Pages in Chapter : "+str(page_num))
    #print
    for i in xrange(1,page_num+1):
        print("#",end="",sep="")
        sys.stdout.flush()
        u=urllib.urlopen("http://www.mangahit.com/"+manga_name+"/"+str(c)+"/"+str(i))
        u=u.read()
        bo=bs4.BeautifulSoup(u,"lxml")
        to_download=bo.find("img")["src"]
        if "label" not in to_download:
            urllib.urlretrieve(bo.find("img")["src"],os.path.join(pathx+"/Chapter-"+str(c) ,"Page-" +str(i)))
    print()
if print_flag:
    print ("All done!")
