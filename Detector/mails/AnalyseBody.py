from BodyExtract import *

class liste_mots():
    def __init__(self):
        self.liste_mots = list()
        self.liste_mots_oc = list()

    def add(self,mot):
        self.liste_mots.append(mot)
        self.liste_mots_oc.append([mot,1])

    def new_oc(self, mot):
        pos = self.liste_mots.index(mot)
        self.liste_mots_oc[pos][1] += 1

    def sort_lists(self):
        self.liste_mots.sort()
        self.liste_mots_oc.sort()

    def exist(self, mot):
        if mot in self.liste_mots:
            return True
        else:
            return False

class lexique_domaine():
    def __init__(self):
        self.lexique = list()
        self.occu_in_mail = 0

    def __int__(self):
        return self.occu_in_mail

    def __str__(self):
        return str(self.occu_in_mail)

    def check_occu(self, mot):
        for mot_lex in self.lexique:
            if mot_lex in mot[0].lower():
                self.occu_in_mail += mot[1]
    


lexique_vente = lexique_domaine()
lexique_vente.lexique = [
    'achat', 'achetez',
    'coupon', 'exceptionnel', 'gratuit',
    'rembours',
    'frais', 'vente', 'télévision',
    'recevoir',
    'télé'
    ]

lexique_vie_priv = lexique_domaine()
lexique_vie_priv.lexique = [
    'amour','célibataire','sexy',
    'rencontrer','rencontre',
    'homme', 'femme',
    ]

lexique_argent = lexique_domaine()
lexique_argent.lexique = [
    '€','$','£',
    'argent','doublez','prix',
    'gains','profit', 'revenus'
    ]

lexique_finance = lexique_domaine()
lexique_finance.lexique = [
    'facture', 'affaire', 'assurance'
    'cash', 'chèque', 'débit',
    'dépot', 'économisez', 'hypothèque',
    'investi', 'finance', 'rendement',
    'mastercard', 'visa/mastercard'
    ]

lexique_marketing = lexique_domaine()
lexique_marketing.lexique = [
    'gratuit', 'facile', 'marketing',
    'opportunité', 'solution'
    ]

fichier = "email.txt"

texte = BodyExtract(fichier)

liste_paragraphes = texte.split('\n')

liste_complete_mots = liste_mots()

for paragraphe in liste_paragraphes:
    if (len(paragraphe)!=0):
        liste_mots = paragraphe.split(' ')
        for mot in liste_mots:
            if not liste_complete_mots.exist(mot) :
                liste_complete_mots.add(mot)
            else:
                liste_complete_mots.new_oc(mot)

liste_complete_mots.sort_lists()

for mot in liste_complete_mots.liste_mots_oc:
    lexique_vente.check_occu(mot)
    lexique_vie_priv.check_occu(mot)
    lexique_argent.check_occu(mot)
    lexique_finance.check_occu(mot)
    lexique_marketing.check_occu(mot)
    

print("Mot du lexique vente présents :", lexique_vente)
print("Mot du lexique vie privée présents :", lexique_vie_priv)
print("Mot du lexique argent présents :", lexique_argent)
print("Mot du lexique finance présents :", lexique_finance)
print("Mot du lexique marketing présents :", lexique_marketing)

print('finance' in 'refinancement')


    
