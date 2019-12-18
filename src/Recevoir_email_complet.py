from goto import with_goto

import sys
from threading import Thread, RLock
import threading

import imaplib
import email
from time import sleep
from random import randint
import importlib
import src.Analyser





verrou = RLock()



class checkMail(Thread):

    def __init__(self,ident, x,data,new_mes_nb):
        Thread.__init__(self)
        self.ID = ident
        self.x = x
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login('yncrea.test.projet.M1@gmail.com', 'ujikolpm')
        self.data = data
        self.new_mes_nb = new_mes_nb
        
    def run(self):

        
        try:
            print("\n---NOUVEAU MESSAGE : %i---"%self.x)
            self.mail.list()
            self.mail.select('inbox')
            with verrou:
                latest_email_uid = self.data[0].split()[self.new_mes_nb - 1]
                
                result, email_data = self.mail.uid('fetch', latest_email_uid, '(RFC822)')

                
                raw_email = email_data[0][1]
                
                raw_email_string = raw_email.decode('utf-8')
                email_message = email.message_from_string(raw_email_string)
                
                for part in email_message.walk():
                    save_string = r"email" + str(self.x) + ".txt"
                    myfile = open(save_string, 'a')
                    myfile.write(str(part))
                    
                    myfile.close()


                
                
                cible_dossier = 'traitement'
                
                result_move, err_mes = self.mail.uid('move',latest_email_uid,cible_dossier)
                if(result_move =='OK'):
                    print("Mail déplacé avec succès")
                else:
                    print(err_mes)

                
                    
                self.mail.select(cible_dossier)

                result, data = self.mail.uid('search', None, "ALL")
                
                latest_email_uid = data[0].split()[- 1]       

                sortie_traitement = randint(1,3)

                print("Résultat traitement :", sortie_traitement)

                if(sortie_traitement == 3):
                    result_move, err_mes = self.mail.uid('move',latest_email_uid,"sur")
                    if(result_move =='OK'):
                        print("Mail", self.x, "déplacé dans sur")
                    else:
                        print(err_mes)

                elif(sortie_traitement == 2):
                    result_move, err_mes = self.mail.uid('move',latest_email_uid,"moyen")
                    if(result_move =='OK'):
                        print("Mail", self.x, "déplacé dans moyen")
                    else:
                        print(err_mes)

                else:
                    result_move, err_mes = self.mail.uid('move',latest_email_uid,"danger")
                    if(result_move =='OK'):
                        print("Mail", self.x, "déplacé dans danger")
                    else:
                        print(err_mes)

                
                self.mail.logout()
                print("Analyse effectuée")
                self.join()
        except KeyboardInterrupt:
            self.join()
        except RuntimeError:
            a = 1

ai = importlib.import_module("Neural_Network", package=None)

def efface_old_mail():
    import os

    arret = False
    x = 1
    while not arret:
        if os.path.exists("email"+str(x)+".txt"):
          os.remove("email"+str(x)+".txt")
          x += 1
        else:
          print("Fichiers supprimés")
          arret = True

old_mes_nb = -1
x = 1



@with_goto
def run():
    print("start")
    label.start
    
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login('yncrea.test.projet.M1@gmail.com', 'ujikolpm')
        old_mes_nb = -1
        x = 1
        ident = 1
        list_thread = list()
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
                
                list_thread.append(checkMail(ident, x, data, new_mes_nb))
                list_thread[len(list_thread) - 1].setDaemon(True)
                list_thread[len(list_thread) - 1].start()
                
                ident += 1
                x += 1
                old_mes_nb = new_mes_nb
                
            elif(new_mes_nb < old_mes_nb):
                old_mes_nb = new_mes_nb
    except TimeoutError:
        goto.start
    except KeyboardInterrupt:
        goto.end

    label.end
    mail.logout()
    print("Good Bye")
run()



