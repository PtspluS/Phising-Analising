import imaplib
import email
from time import sleep
from random import randint

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('yncrea.test.projet.M1@gmail.com', 'ujikolpm')

def efface_old_mail():
    import os

    arret = False
    x = 1
    while not arret:
        if os.path.exists("email"+str(x)+".txt"):
          os.remove("email"+str(x)+".txt")
        else:
          print("Fichiers supprimés")
          arret = True

old_mes_nb = -1
x = 1

efface_old_mail()

while True:
    
    mail.list() 
    mail.select('inbox')


    result, data = mail.uid('search', None, "ALL")
    
    i = len(data[0].split())
    new_mes_nb = i

    if(old_mes_nb == -1):
        old_mes_nb = new_mes_nb
    

    if(new_mes_nb > old_mes_nb):
        print("\n---NOUVEAU MESSAGE : %i---"%x)
        latest_email_uid = data[0].split()[new_mes_nb - 1]
        print(latest_email_uid)
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')


        raw_email = email_data[0][1]
        
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        for part in email_message.walk():
            save_string = r"email" + str(x) + ".txt"
            myfile = open(save_string, 'a')
            myfile.write(str(part))
            
            myfile.close()


        
        
        cible_dossier = 'traitement'
        
        result_move, err_mes = mail.uid('move',latest_email_uid,cible_dossier)
        if(result_move =='OK'):
            print("Mail déplacé avec succès")
        else:
            print(err_mes)
            
        mail.select(cible_dossier)

        result, data = mail.uid('search', None, "ALL")
        print(data[0])
        latest_email_uid = data[0].split()[- 1]
        sleep(15)       

        sortie_traitement = randint(1,3)

        print("Résultat traitement :", sortie_traitement)

        if(sortie_traitement == 3):
            result_move, err_mes = mail.uid('move',latest_email_uid,"sur")
            if(result_move =='OK'):
                print("Mail", str(latest_email_uid), "déplacé dans sur")
            else:
                print(err_mes)

        elif(sortie_traitement == 2):
            result_move, err_mes = mail.uid('move',latest_email_uid,"moyen")
            if(result_move =='OK'):
                print("Mail", str(latest_email_uid), "déplacé dans moyen")
            else:
                print(err_mes)

        else:
            result_move, err_mes = mail.uid('move',latest_email_uid,"danger")
            if(result_move =='OK'):
                print("Mail", str(latest_email_uid), "déplacé dans danger")
            else:
                print(err_mes)

        
        x += 1
        old_mes_nb = new_mes_nb
        print("Analyse effectuée")
    elif(new_mes_nb < old_mes_nb):
        old_mes_nb = new_mes_nb




