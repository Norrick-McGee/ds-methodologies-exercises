import nltk
import unicodedata
import re
from nltk.corpus import stopwords

stopword_list = nltk.corpus.stopwords.words('english') + ['r', 'u', '2', 'ltgt']

stopword_list.remove('no')
stopword_list.remove('not')


def basic_clean(article):
    article = ' '.join(article.split()).lower()
    article = unicodedata.normalize('NFKD',article).encode('ASCII','ignore').decode('utf-8', 'ignore')
    article = re.sub(r"[^a-z0-9'\s]", '', article)
    return article

def stem_words(article):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in article.split()]
    return ' '.join(stems)

def drop_stop_words(article):
    words = article.split()
    filtered_words = [w for w in words if w not in stopword_list]
    return ' '.join(filtered_words)

def clean(article):
    article = basic_clean(article)
    article = stem_words(article)
    article = drop_stop_words(article)
    return article
