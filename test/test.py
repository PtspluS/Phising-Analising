"""
import pandas as pd
import spacy
spacy.load('en_core_web_sm')


from spacy.lang.en import English
parser = English()

def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens

import nltk


from nltk.corpus import wordnet as wn

def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma
    
from nltk.stem.wordnet import WordNetLemmatizer

def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)


en_stop = set(nltk.corpus.stopwords.words('english'))


def prepare_text_for_lda(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens

from gensim import corpora
import gensim
import pickle


def run():
      

    mails = pd.read_csv("essai.csv",delimiter=",",skiprows=1, names=['ID', 'Text', 'Author'], encoding="latin-1").set_index('ID')

    text_data = list()
    for i in mails.Text.values:
        #print(prepare_text_for_lda(i))
        text_data.append(prepare_text_for_lda(i))

    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]
    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictionary.gensim')
    NUM_TOPICS = 5
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
    ldamodel.save('model5.gensim')

    topics = ldamodel.print_topics(num_words=4)
    for topic in topics:
        print(topic)

    new_doc = """"""
    The most merciful thing in the world, I think,
    is the inability of the human mind to correlate all its contents.
    We live on a placid island of ignorance in the midst of black seas of infinity,
    and it was not meant that we should voyage far.
    The sciences, each straining in its own direction,
    have hitherto harmed us little;
    but some day the piecing together of dissociated knowledge will open up such terrifying vistas of reality,
    and of our frightful position therein,
    that we shall either go mad from the revelation or flee from the deadly light into the peace and safety of a new dark age.
Theosophists have guessed at the awesome grandeur of the cosmic cycle wherein our world and human race form transient incidents.
They have hinted at strange survivals in terms which would freeze the blood if not masked by a bland optimism.
But it is not from them that there came the single glimpse of forbidden aeons which chills me when I think of it and maddens me when I dream of it.
That glimpse, like all dread glimpses of truth, flashed out from an accidental piecing together of separated things—in this case an old newspaper item and the notes of a dead professor. I hope that no one else will accomplish this piecing out; certainly, if I live, I shall never knowingly supply a link in so hideous a chain. I think that the professor, too, intended to keep silent regarding the part he knew,
and that he would have destroyed his notes had not sudden death seized him."""
"""new_doc = prepare_text_for_lda(new_doc)
    new_doc_bow = dictionary.doc2bow(new_doc)
    #print(new_doc_bow)
    print(ldamodel.get_document_topics(new_doc_bow))

run()"""
import pandas as pd
import re
from stop_words import get_stop_words
en_stop = get_stop_words('en')
from gensim import corpora, models
import gensim
import csv 

mails = pd.read_csv("essai.csv",delimiter=",",skiprows=1, names=['ID', 'Text', 'Author'], encoding="latin-1").set_index('ID')

text = list(mails.Text.values)

email_process_list=list()
number = 1
for email in text:
    email_process=[word for word in email.split() if word not in en_stop]
    email_process=' '.join(email_process)
    email_process=re.sub(r'(http:\S+)', ' ' ,email_process)
    email_process=re.sub(r'(www\.\S+)', ' ' ,email_process)
    email_process=re.sub(r'\S+\.com', ' ' ,email_process)
    email_process=re.sub(r'\S+@\S+', ' ' ,email_process)
    email_process=re.sub('\d+', '', email_process)
    email_process=re.sub(r'\$','dollarmoneyprocess',email_process)
    email_process=re.sub(r'[^\w\d\s\+]',' ',email_process)
    email_process=re.sub(r'pm','timetableprocess',email_process)
    email_process=re.sub(r'\b\w{1,2}\b', ' ', email_process)
    email_process=re.sub(r'\S+_\S*', '' ,email_process)
    email_process=re.sub(r'_\S*', '' ,email_process)
    email_process=re.sub(r'\s(dollars)\s','dollarmoneyprocess',email_process)
    email_process=re.sub(r'\s(dollar)\s','dollarmoneyprocess',email_process)
    email_process=email_process.split()
    email_process=set(email_process)
    email_process_list.append((number,email_process))
    number+=1

words_dico=dict()
for number,email in email_process_list:
    for word in set(email):
        if word not in words_dico:
            words_dico[word]=1
        else:
            words_dico[word]=words_dico[word]+1

words_freq = list()
for key, val in words_dico.items():
    words_freq.append( (key, val) )
words_freq.sort(key=lambda tup: tup[1] ,reverse=True)
#print(words_freq[:50])

words_to_delete1= [t[0] for t in words_freq]# if t[1] &;amp;lt;11]
words_to_delete2=[t[0] for t in words_freq[:30]]
words_to_delete=words_to_delete1+words_to_delete2

email_process_list_new=list()
itera=0
for number,email in email_process_list:
    email_process=[word for word in email if word not in words_to_delete]
    email_process_list_new.append((itera,number,email_process))
    itera=itera+1
 
email_process_list_new2=email_process_list_new

for idx,email in enumerate(email_process_list_new2):
    if len(email[2])&amp;amp;lt;11:
        del email_process_list_new2[idx]
 
emailsonly=[x[2] for x in email_process_list_new2]

dictionary = corpora.Dictionary(emailsonly)
corpus = [dictionary.doc2bow(text) for text in emailsonly]

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=30, id2word = dictionary, passes=20)
