# from hackernews import HackerNews
# import pandas as pd
# #imports/requirements
# #imports
# import pandas as pd
# import numpy as np
# #import matplotlib.pyplot as plt
# import nltk
# import random
# import re
# from nltk import word_tokenize, sent_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import LancasterStemmer, WordNetLemmatizer, PorterStemmer
# from wordcloud import WordCloud, STOPWORDS
# from textblob import TextBlob,Word, Blobber
# nltk.download('stopwords')
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# from sklearn.metrics import f1_score, accuracy_score
# import html
# from html.parser import HTMLParser

# hn = HackerNews()

# # request last 2000 items
# last = hn.get_last(5000)


# # view item type and item text
# items_dict = []
# for item in last:
#     #only keep users and text from comments
#     if item.item_type == 'comment':
#         user = item.by
#         text = item.text
#         date = item.submission_time

#         #output metrics as a row
#         dictionary_data = {"User":user, "Text":text, 'Date':date}
#         items_dict.append(dictionary_data) 

# # create dataframe for modelling use
# df = pd.DataFrame.from_dict(items_dict)

# #convert to string
# df['Text'] = df['Text'].astype(str)

# def cleanup_html(raw_html):
#     clean_html = re.sub(r'<.*?>', '', raw_html)
#     clean_html_http = re.sub(r'http\S+([\.]{3})?', '', clean_html)
#     clean_txt = html.unescape(clean_html)
#     return clean_txt
# df['Text'] = df['Text'].apply(cleanup_html)
# df.sample(10)
# for row in df['Text'].sample(10):
#     print(row)
#     print()


# class MLStripper(HTMLParser):
#     def __init__(self):
#         super().__init__()
#         self.reset()
#         self.fed = []
#     def handle_data(self, d):
#         self.fed.append(d)
#     def get_data(self):
#         return ' '.join(self.fed)


# def strip_tags(html):
#     s = MLStripper()
#     s.feed(html)
#     return s.get_data()

# df['Text']  = df['Text'].apply(html.unescape)

# #convert to lower case
# df['Text'] = df['Text'].apply(lambda x: ' '.join(x.lower() for x in x.split()))

# print(df['Text'][77])

# #stopwords:
# stop = stopwords.words('english')
# df['Text'] = df['Text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
# #df['Text'][77]

# #stemming
# st = PorterStemmer()
# df['Text'] = df['Text'].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))
# #df['Text'][77]

# #create object
# nltk.download('vader_lexicon')
# analyzer = SentimentIntensityAnalyzer()

# #define analyzer
# def vaderize(sentence):
#     return analyzer.polarity_scores(sentence)

# df['Scores'] = df['Text'].apply(vaderize)

# df[['neg', 'neu', 'pos', 'compound']] = df.Scores.apply(pd.Series)

# #sort
# for text in df.sort_values(by='neg', ascending=False)['Text'].head(20):
#     print(text, '\n')

# df['len'] = df['Text'].str.len()  # Store string length of each sample

# #define analyzer
# vader = SentimentIntensityAnalyzer()
# def score_vader(sentence, vader):
#     return vader.polarity_scores(sentence)['compound']

# # Calculate Vader sentiment score
# df['vader_score'] = df['Text'].apply(lambda x: score_vader(x, vader))
# # Convert float score to category based on binning
# df['vader_pred'] = pd.cut(df['vader_score'], bins=5, labels=[1, 2, 3, 4, 5])
# df = df.drop('vader_score', axis=1)

# df['vader_pred'] = df.vader_pred.astype(str)
# print(df.head(20))

