from spellchecker import SpellChecker
import nltk



poem = """Over hill, over dale,
Thorough bush, thorough brier,
Over park, over pale,
Thorough flood, thorough fire!
I do wander everywhere,
Swifter than the moon's sphere;
And I serve the Fairy Queen,
To dew her orbs upon the green;
The cowslips tall her pensioners be;
In their gold coats spots you see;
Those be rubies, fairy favours;
In those freckles live their savours;
I must go seek some dewdrops here,
And hang a pearl in every cowslip's ear. """

poem_mistakes = """
Overz hillz, overz dalez,
Thoroughz bushz, thoroughz brierz,
Overz parkz, overz palez,
Thoroughz floodz, thoroughz firez!
Iz zdzo wanderz everywherez,
Swifterz thanz thez moon's sphere;
And I servez the Fairy Queen,
To dewz herz orbs upon the green;
The cowslips tall her pensioners be;
In their gold coats spots you see;
Those be rubies, fairy favours;
In those freckles live their savours;
I must go seek some dewdrops here,
And hang a pearl in every cowslip's ear. 
"""

def error_grammar_frequency_en(text):

    spell = SpellChecker()

    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    size_txt = len(tokens)

    misspelled = spell.unknown(tokens)

    # frequency of the word who have are misspelled
    freq = len(misspelled)/size_txt

    # transform in percent
    return freq*100

print(error_grammar_frequency_en(poem))
print(error_grammar_frequency_en(poem_mistakes))
