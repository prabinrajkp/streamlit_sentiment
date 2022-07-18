import pandas as pd
import numpy as np
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


	

# preprocess text
def preprocess(text):

    stop_words=set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    stop_words.add('update')
    
    text=str(text)
    
    # remove new lines
    text = text.replace('\n', ' ')
    
    # remove links
    text = re.sub('https?://\S+|www\.\S+', ' ', text)
    
    # remove hashtags at the end of text
    text = re.sub('#(?!(?:hashtag)\b)[\w-]+(?=(?:\s+#[\w-]+)*\s*$)', '',text)
    
    # remove handles
    text = re.sub('@[\w]+', '',text)
    
    # remove punctuations
    punc ='''.?!,:;-_—[](){}'"`~|\/@#$%^&+=*'''
    for i in text:
        if i in punc:
            text = text.replace(i, '') 
    
    # remove extra spaces
    re.sub("\s\s+", " ", text)
    
    # lower case
    text = text.strip().lower()
    
    # lemmatization
    text = [lemmatizer.lemmatize(word) for word in text.split(' ')]
    text=" ".join(text)
    
    # stopword removal
    text = [word for word in text.split(' ') if word not in stop_words]
    text=" ".join(text)

    # replace covid19 with covid
    text=text.replace('covid19','covid')
    
    return text
    
    
    # function
def demoji(text):

    
    # frequent emojis whhich will be kept
    pattern = '😤|😡|😠|😑|🙄|🤨|😶|😱|🙀|😲|😓|😰|😢|😥|😭|😪|🤕|😔|😣|🙁|😒|😖|😕|🥴|🤒|☹️|😞|😷|🤧|😧|😨|😩|🥺|😦|😆|😀|🤭|🤩|😌|🥰|😁|😘|😂|😅|😊|😝|😙|😇'
    text=str(text)
    for word in text:    
        if re.match(pattern, word):
            continue
            
        # remove all other non ascii characters
        text=text.replace(word, re.sub('[^\x00-\x7f]','', word)).strip()
        
    return text
    
    
def convert(text):
   
    
    # dictionary of emoji with their meaning
    text=str(text)
    d = {'😤':'frustrated','😡':'angry','😠':'angry','😱':'horrified','🙀':'shock','😲':'shock','🙄':'disapproval',
         '🤨':'suspicion','😶':'disappointment','😓':'sad','😰':'sad','😢':'sad','😥':'sad','😭':'sad','😪':'sad',
         '🤕':'sad','😔':'sad','😣':'sad','🙁':'sad','😒':'sad','😖':'sad','😕':'sad','🥴':'sad','🤒':'sad','☹️':'sad',
         '😞':'sad','😷':'sick','🤧':'sick','😧':'sad','😨':'sad','😩':'sad','🥺':'sad','😦':'sad','😫':'sad',
         '😆':'happy','😀':'smile','🤭':'embarrassment','🤩':'exciting','🥰':'affection','😁':'smile','😂':'laugh',
         '😅':'nervousness','😊':'smile','😝':'fun','😙':'affection','😇':'blessed'}
    
    for emoji, sentiment in d.items():
        text=text.replace(emoji, sentiment)
    return text
    
def dataclean(df):
	
	df['Text'].apply(preprocess)
	df['Text']= df['Text'].apply(demoji)
	df['senti_text']= df['Text'].apply(convert)
	print('preprocess run')
	
	return df
    
    
    
    
    
