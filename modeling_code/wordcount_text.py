import pandas as pd
from collections import Counter
import nltk
import csv

data = []
col = 'comment'
df = pd.read_csv("../data/walmart_amazon/wal_ama_score_45.csv", usecols = [col])
#add words to be removed
stop_words = nltk.corpus.stopwords.words('english')
stop_words.extend(['tried','brand','products','boxes','used','made','give','bags','fan','maybe','away','still','item','two','though','food','contains','amazon','know','tastes','however','way','sure','ordered','tasted','make','fresh','review','bit','light','right',"can't",'store','something','find','liked','loved','really','great','go','eat','halo',"i'm", "ocean's", 'x99s', 'seaweed', 'snack', 'flavor', 'snacks', 'like', 'product', 'bought', 'okay', 'buy', 'ok', 'buying','better','one', 'would', 'get', 'box', 'thought', 'much', 'eating', 'bag', 'received', 'could', 'also', 'got', 'think', 'time', 'definitely', 'little', 'chips', 'perfect', 'well', "i've", 'nice', 'even'])

#create excel file
file = open('pos_words2.csv', 'w')
writer = csv.writer(file)
writer.writerow(['word', 'count', 'sentiment'])

def wordcount(df):
    text = ''
    for i in range(len(df.index)):
        data.append(df[col].iloc[i])
    for i in data:
        text += str(i)

# Cleaning text and lower casing all words
    for char in '-.,\n;[]?!0123456789$':
        text = text.replace(char,' ')
    text = text.lower()     #combined text without punctuation

# split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s)
    word_list = text.split() #words splited
    filtered_list = []  #filtering stop_words
    for word in word_list:
        if word not in stop_words:
            filtered_list.append(word)
    word_count = Counter(filtered_list).most_common()
    for index in range(40):
        writer.writerow(word_count[index])


wordcount(df)


