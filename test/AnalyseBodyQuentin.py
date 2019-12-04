
import nltk

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from IPython.display import display
import base64
import string
import re
from collections import Counter
from time import time
# from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS as stopwords
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt
from pywaffle import Waffle

from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

from gensim.models.word2vec import Word2Vec

import io
import spacy
nlp = spacy.load('en_core_web_sm')

import warnings

from sklearn.preprocessing import label_binarize
from sklearn.model_selection import train_test_split

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.collocations import *
try:
    stopwords = set(stopwords.words('english'))
except LookupError:
    import nltk
    nltk.download('stopwords')
    stopwords = set(stopwords.words('english'))


import sys
sys.path.append('../')
from src.Email import *


lemm = WordNetLemmatizer()

text_dim = 300

class LemmaCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(LemmaCountVectorizer, self).build_analyzer()
        return lambda doc: (lemm.lemmatize(w) for w in analyzer(doc))




def print_top_words(model, feature_names, n_top_words):
    j = 1
    for topic_idx, topic in enumerate(model.components_):
        j+=1
        print("Topic n°", topic_idx,":")
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print(j)


punctuations = string.punctuation

# Define function to cleanup text by removing personal pronouns, stopwords, and puncuation
def cleanup_text(docs, logging=False):
    texts = []
    counter = 1
    for doc in docs:
        if counter % 1000 == 0 and logging:
            print("Processed %d out of %d documents." % (counter, len(docs)))
        counter += 1
        doc = nlp(doc, disable=['parser', 'ner'])
        tokens = [tok.lemma_.lower().strip() for tok in doc if tok.lemma_ != '-PRON-']
        tokens = [tok for tok in tokens if tok not in stopwords and tok not in punctuations]
        tokens = ' '.join(tokens)
        texts.append(tokens)
    return pd.Series(texts)


def cleanup_text_word2vec(docs, logging=False):
    sentences = []
    counter = 1
    for doc in docs:
        if counter % 1000 == 0 and logging:
            print("Processed %d out of %d documents" % (counter, len(docs)))
        # Disable tagger so that lemma_ of personal pronouns (I, me, etc) don't getted marked as "-PRON-"
        doc = nlp(doc, disable=['tagger'])
        # Grab lemmatized form of words and make lowercase
        doc = " ".join([tok.lemma_.lower() for tok in doc])
        # Split into sentences based on punctuation
        doc = re.split("[\.?!;] ", doc)
        # Remove commas, periods, and other punctuation (mostly commas)
        doc = [re.sub("[\.,;:!?]", "", sent) for sent in doc]
        # Split into words
        doc = [sent.split() for sent in doc]
        sentences += doc
        counter += 1
    return sentences

# Define function to create word vectors given a cleaned piece of text.
def create_average_vec(doc, wordvec_model):
    average = np.zeros((text_dim,), dtype='float32')
    num_words = 0.
    for word in doc.split():
        if word in wordvec_model.wv.vocab:
            average = np.add(average, wordvec_model[word])
            num_words += 1.
    if num_words != 0.:
        average = np.divide(average, num_words)
    return average


with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)

    from keras.models import Sequential, Model
    from keras.layers import Dense, Dropout, Input, LSTM, Embedding, Bidirectional, Flatten
    from keras.layers import Conv1D, MaxPooling1D, GlobalMaxPooling1D
    from keras.optimizers import SGD

def build_model():
    model = Sequential()
        # Densely Connected Neural Network (Multi-Layer Perceptron)
    model.add(Dense(512, activation='relu', kernel_initializer='he_normal', input_dim=300))
    model.add(Dropout(0.2))
    model.add(Dense(512, activation='relu', kernel_initializer='he_normal'))
    model.add(Dropout(0.2))
    model.add(Dense(512, activation='relu', kernel_initializer='he_normal'))
    model.add(Dropout(0.2))
    model.add(Dense(512, activation='relu', kernel_initializer='he_normal'))
    model.add(Dropout(0.2))
    model.add(Dense(3, activation='softmax'))
    return model

def run():
      

    mails = pd.read_csv("essai.csv",delimiter=",",skiprows=1, names=['ID', 'Text', 'Author'], encoding="latin-1").set_index('ID')

    text = list(mails.Text.values)
    
    
    # Calling our overwritten Count vectorizer
    tf_vectorizer = LemmaCountVectorizer(stop_words='english',
                                         decode_error='ignore')
    tf = tf_vectorizer.fit_transform(text)
    print(tf)
    return 0
    nb_components = 10
    
    lda = LatentDirichletAllocation(n_components=nb_components, max_iter=5,
                                learning_method = 'online',
                                learning_offset = 50.,
                                random_state = 0)

    lda.fit(tf)

    """
    LatentDirichletAllocation(batch_size=128, doc_topic_prior=None,
                          evaluate_every=-1, learning_decay=0.7,
                          learning_method='online', learning_offset=50.0,
                          max_doc_update_iter=100, max_iter=5,
                          mean_change_tol=0.001, n_components=nb_components, n_jobs=None,
                          perp_tol=0.1, random_state=0, topic_word_prior=None,
                          total_samples=1000000.0, verbose=0)

    """
    n_top_words = 5
    #print("\nTopics in LDA model: ")

    
    
    tf_feature_names = tf_vectorizer.get_feature_names()
    print(len(tf_feature_names))
        
    print_top_words(lda, tf_feature_names, n_top_words)

    text =[ """
    The most merciful thing in the world, I think, is the inability of the human mind to correlate all its contents. We live on a placid island of ignorance in the midst of black seas of infinity, and it was not meant that we should voyage far. The sciences, each straining in its own direction, have hitherto harmed us little; but some day the piecing together of dissociated knowledge will open up such terrifying vistas of reality, and of our frightful position therein, that we shall either go mad from the revelation or flee from the deadly light into the peace and safety of a new dark age.
    """]

    
    
    """for i in top_topic:
        print(i)
        print(tf_vectorizer.get_feature_names()[i])"""
    
    
    """
    firstcloud = WordCloud(stopwords=stopwords,
                       background_color='black',
                       width=2500,
                       height=1800
                       ).generate(" ".join(first_topic_words))
    
    
    plt.imshow(firstcloud)
    plt.axis('off');
    plt.show()
    """
    """
    second_topic_words = [tf_feature_names[i] for i in second_topic.argsort()[:-50 - 1 :-1]]


    second_cloud = WordCloud(
                          stopwords=stopwords,
                          background_color='black',
                          width=2500,
                          height=1800
                         ).generate(" ".join(second_topic_words))
    """"""
    plt.imshow(second_cloud)
    plt.axis('off');
    plt.show()
    """
"""
    print('Original mailsing data shape: ', mails['Text'].shape)
    mails_cleaned = cleanup_text(mails['Text'], logging=True)
    print('Cleaned up mailsing data shape: ', mails_cleaned.shape)

    print('Parsing documents...')

    start = time()

    mails_vec = []
    for doc in nlp.pipe(mails_cleaned, batch_size=500):
        if doc.has_vector:
            mails_vec.append(doc.vector)
        # If doc doesn't have a vector, then fill it with zeros.
        else:
            mails_vec.append(np.zeros((128,), dtype="float32"))

    mails_vec = np.array(mails_vec)
    print('Total time passed parsing documents: {} seconds'.format(end - start))
    print('Total number of documents parsed: {}'.format(len(mails_vec)))
    print('Number of words in first document: ', len(mails['Text'][1]))
    print('Number of words in second document: ', len(mails['Text'][2]))
    print('Size of vector embeddings: ', mails_vec.shape)
    print('Shape of vectors embeddings matrix: ', mails_vec.shape)

    all_text = pd.DataFrame(mails, columns=['Text'])

    print('Number of total text documents:', len(all_text))

    mails_cleaned_word2vec = cleanup_text_word2vec(all_text['Text'], logging=True)
    print('Cleaned up mailsing data size (i.e. number of sentences): ', len(mails_cleaned_word2vec))


    from gensim.models.word2vec import Word2Vec

    

    print("mailsing Word2Vec model...")

    wordvec_model = Word2Vec(mails_cleaned_word2vec, size=text_dim, window=5, min_count=3, workers=4, sg=1)

    print("Word2Vec model created.")
    print("%d unique words represented by %d dimensional vectors" % (len(wordvec_model.wv.vocab), text_dim))

    print(wordvec_model.wv.most_similar(positive=['mother','woman']))
    print(wordvec_model.wv.most_similar(positive=['love']))
    print(wordvec_model.wv.most_similar(positive=['fear']))

    # Counting the number of empty strings are in mails_cleaned
    count = 0
    for i in range(len(mails_cleaned)):
        if mails_cleaned[i] == "":
            print("index:", i)
            count += 1
    print("Empty strings :",count)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)

        mails_cleaned_vec = np.zeros((mails.shape[0], text_dim), dtype="float32")  # 19579 x 300
        for i in range(len(mails_cleaned)):
            mails_cleaned_vec[i] = create_average_vec(mails_cleaned[i], wordvec_model)

    print("mails word vector shape:", mails_cleaned_vec.shape)

    # Transform labels into one hot encoded format.
    y_mails_ohe = label_binarize(mails['Author'], classes=['EAP', 'HPL', 'MWS'])
    print('y_mails_ohe shape: {}'.format(y_mails_ohe.shape))
    print('y_mails_ohe samples:')
    print(y_mails_ohe[:5])

    
    # If using spaCy word vectors
    # X_mails, X_test, y_mails, y_test = mails_test_split(mails_vec, y_mails_ohe, test_size=0.2, random_state=21)
    # If using Word2Vec word vectors
    X_mails, X_test, y_mails, y_test = train_test_split(mails_cleaned_vec, y_mails_ohe, test_size=0.2, random_state=21)

    print('X_mails size: {}'.format(X_mails.shape))
    print('X_test size: {}'.format(X_test.shape))
    print('y_mails size: {}'.format(y_mails.shape))
    print('y_test size: {}'.format(y_test.shape))

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)

        model = build_model()  #('mlp')
        model.summary()

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)

        sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['acc'])

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)

        # Define number of epochs
        epochs = 50

        # Fit the model to the training data
        estimator = model.fit(X_mails, y_mails,
                              validation_split=0.2,
                              epochs=epochs, batch_size=128, verbose=100)

    print("Training accuracy: %.2f%% / Validation accuracy: %.2f%%" %
      (100*estimator.history['acc'][-1], 100*estimator.history['val_acc'][-1]))

    # Plot model accuracy over epochs
    fig, ax = plt.subplots(1, 2, figsize=(12,4))

    sns.reset_orig()   # Reset seaborn settings to get rid of black background
    ax[0].plot(estimator.history['acc'])
    ax[0].plot(estimator.history['val_acc'])
    ax[0].set_title('model accuracy')
    ax[0].set_ylabel('accuracy')
    ax[0].set_xlabel('epoch')
    ax[0].legend(['mails', 'valid'], loc='upper left')

    # Plot model loss over epochs
    ax[1].plot(estimator.history['loss'])
    ax[1].plot(estimator.history['val_loss'])
    ax[1].set_title('model loss')
    ax[1].set_ylabel('loss')
    ax[1].set_xlabel('epoch')
    ax[1].legend(['mails', 'valid'], loc='upper left');

    plt.show()

    predicted_prob = model.predict(X_test)
    print(predicted_prob.shape,"\n\n<-------->\n")

    print(predicted_prob, y_test,sep='\n------\n')
    """
end = time()

run()


