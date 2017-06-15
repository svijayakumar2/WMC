#####
### Women's Media Center
### @svijayakumar2
### enter as python eliza.py articles_to_enter.txt
### may encounter article irregularity problems 
######

import numpy as np
import random
import collections
import nltk
import csv
import sys

f = open("articles_to_enter.txt","r")
print f.read()

bigdic = [['Section','Headline','Journalist','Word Count','Date','News Outlet','Outlet Abbreviation','Edition','Page','Language','Copyright','Content']]

def num_in_string(s):
    return any(i.isdigit() for i in s)

def isBlank (myString):
    return not (myString and myString.strip())


with open(sys.argv[1],"r") as mainfile:
    reader = mainfile.read()
    for part in enumerate(reader.split("Document ")):
        data = part[1]
        i = 3
        t = data.splitlines()
        #print t
        leng = len(t)
        print leng
        if leng>13:
        
            possible_section = t[i]
            if isBlank(possible_section):
                i = i + 1

            section =  t[i]
            headline =  t[i+1]

            possible_journalist = t[i+3]
            if num_in_string(possible_journalist):
                i = i - 1
                journalist = ' '
            else:
                journalist = t[i+3]

            possible_wordcount = t[i+4] #sometimes journalists have two lines
            if num_in_string(possible_wordcount): #shouldn't have to do this more than once but if that isn't the case turn this into a while 
                i = i
            else:
                i = i+1

            wordcount = t[i+4] #check that it contains a number. many contain journalist, and then journalist 
            #info on the next line. others only contain journalist
            date = t[i+5] #check that it is a date 
            news_outlet = t[i+6]
            outlet_abbreviation = t[i+7]
            edition = t[i+8]
            page =  t[i+9]
            language =  t[i+10]
            copyright =  t[i+11]
            list1 = t[(i+12):leng]
            str1 = ' '.join(list1)
            content =  str1

            dic = []
            dic.append(section)
            dic.append(headline)
            dic.append(journalist)
            dic.append(wordcount)
            dic.append(date)
            dic.append(news_outlet)
            dic.append(outlet_abbreviation)
            dic.append(edition)
            dic.append(page)
            dic.append(language)
            dic.append(copyright)
            dic.append(content)
            bigdic.append(dic)
        else:
            print 'failed or end'

with open(sys.argv[2], "wb") as g:
    writer = csv.writer(g)
    writer.writerows(bigdic)