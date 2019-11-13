"""
python -m pip install spellchecker
"""

from spellchecker import SpellChecker


spell = SpellChecker()



texte = "The Kinng is reelly angrye"

misspelled= texte.split(" ")

#for word in misspelled:
print(spell.unknown(misspelled))
