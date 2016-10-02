
#from Import_Packages import *
import string
import csv
from nltk import *
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import stem


import pandas as pd
import wordcloud
import os

from os import path
from wordcloud import WordCloud

rowlist = []
nopunc = []
removStopwords = []
count =0
d = path.dirname(__file__)

def create_cloud(text_to_draw, filename):
    wordcloud = WordCloud().generate(text_to_draw)
    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud)
    plt.axis("off")

    # take relative word frequencies into account, lower max_font_size
    wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text_to_draw)
    wordcloud.to_file(path.join(d, filename))
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


with open('osha.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #print row[0],row[1]
        rowlist.append(row[1])




for i in range(0,len(rowlist)):
    text_nopunc = rowlist[i].translate(string.maketrans("", ""), string.punctuation).lower()
    nopunc.append(rowlist[i].translate(string.maketrans("", ""), string.punctuation).lower())
    #print text_nopunc
   # print rowlist[i]

stop = stopwords.words('english')
#print stop
#print text_nopunc
# Remove all these stopwords from the text

for i in range(0,len(nopunc)):
    removStopwords.append(" ".join(filter(lambda word: word not in stop, nopunc[i].split())))
#text_nostop=" ".join(filter(lambda word: word not in stop, text_nopunc.split()))

for i in range(0,len(removStopwords)):
    print removStopwords[i]


fullcontent =""

for i in range(0,len(removStopwords)):
    fullcontent =fullcontent+str(removStopwords[i])

create_cloud(fullcontent,"fua.png")