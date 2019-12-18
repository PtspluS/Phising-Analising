from spellchecker import SpellChecker
import nltk

def error_grammar_frequency_en(text):
    """

    :param text: tout le texte du mail
    :return:
    """

    spell = SpellChecker()

    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    size_txt = len(tokens)

    misspelled = spell.unknown(tokens)

    # frequency of the word who have are misspelled
    try:
        freq = len(misspelled)/size_txt
    except:
        freq = 0.5

    # transform in percent
    return freq*100
