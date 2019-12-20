import imaplib
import email
from time import sleep
from random import randint
import importlib
from src.Analyser import mark_email
from src.Email import Email
import numpy as np
from goto import with_goto
from src.save import save


ai = importlib.import_module("Neural_Network", package=None)

def efface_old_mail():
    import os

    arret = False
    x = 1
    while not arret:
        if os.path.exists("email" + str(x) + ".txt"):
            os.remove("email" + str(x) + ".txt")
            x += 1
        else:
            print("Fichiers supprimés")
            arret = True


old_mes_nb = -1
x = 1

efface_old_mail()


@with_goto
def run():
    print('start')
    label.start
    try:
        old_mes_nb = -1
        x = 1

        label.connexion
        connexion_pos = False
        while not connexion_pos:
            adresse = input("Adresse mail: ")
            mdp = input("Mot de passe: ")

            if("@gmail.com" in adresse):
                connexion_pos = True
            else:
                print("Adresse mail non valide\n")
                continue
        try : 
            mail = imaplib.IMAP4_SSL('imap.gmail.com')
            ###Dans login : parametre 1 adresse mail###
            ###             parametre 2 mot de passe###
            #mail.login('yncrea.test.projet.M1@gmail.com', 'ujikolpm')
            mail.login(adresse, mdp)
        except Exception:
            print("Echec connexion\n")
            goto.connexion
            


        while True:

            mail.list()
            mail.select('inbox')

            result, data = mail.uid('search', None, "ALL")

            i = len(data[0].split())
            new_mes_nb = i

            if (old_mes_nb == -1):
                old_mes_nb = new_mes_nb

            if (new_mes_nb > old_mes_nb):
                print("\n---NOUVEAU MESSAGE : %i---" % x)
                latest_email_uid = data[0].split()[new_mes_nb - 1]
                result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')

                raw_email = email_data[0][1]

                raw_email_string = raw_email.decode('utf-8')
                email_message = email.message_from_string(raw_email_string)
                for part in email_message.walk():
                    save_string = r"email" + str(x) + ".txt"
                    myfile = open(save_string, 'a')
                    myfile.write(str(part))
                    mailo = Email(save_string)
                    myfile.close()

                cible_dossier = 'traitement'

                result_move, err_mes = mail.uid('move', latest_email_uid, cible_dossier)
                if (result_move == 'OK'):
                    print("Mail déplacé avec succès")
                else:
                    print(err_mes)

                mail.select(cible_dossier)

                result, data = mail.uid('search', None, "ALL")
                latest_email_uid = data[0].split()[- 1]

                mark = mark_email(mailo)
                marks = np.array([mark])
                sortie_traitement = ai.analyse_mail(marks)[0][0]
                save(mailo, marks=mark, grade=sortie_traitement.item())

                print("Résultat traitement :", sortie_traitement)

                if (sortie_traitement >= 0.6):
                    result_move, err_mes = mail.uid('move', latest_email_uid, "sur")
                    if (result_move == 'OK'):
                        print("Mail déplacé dans sur")
                    else:
                        print(err_mes)

                elif (sortie_traitement >= 0.4 and sortie_traitement < 0.6):
                    result_move, err_mes = mail.uid('move', latest_email_uid, "moyen")
                    if (result_move == 'OK'):
                        print("Mail déplacé dans moyen")
                    else:
                        print(err_mes)

                else:
                    result_move, err_mes = mail.uid('move', latest_email_uid, "danger")
                    if (result_move == 'OK'):
                        print("Mail déplacé dans danger")
                    else:
                        print(err_mes)

                x += 1
                old_mes_nb = new_mes_nb
                print("Analyse effectuée")
            elif (new_mes_nb < old_mes_nb):
                old_mes_nb = new_mes_nb
    except TimeoutError:
        goto.start
    except KeyboardInterrupt:
        goto.end

    label.end
    mail.logout()
    print("Good bye")

run()




