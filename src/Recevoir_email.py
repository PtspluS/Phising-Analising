import easyimap
def run():
    login = 'yncrea.test.projet.M1@gmail.com'
    password = 'ujikolpm'

    imapper = easyimap.connect('imap.gmail.com', login, password)
    
    old_email = list()

    for mail_id in imapper.listids(limit=100):
        mail = imapper.mail(mail_id)
        old_email.append(mail)

    i = 1

    while True:
        print(len(old_email))
        i += 1
        if(i == 20 and len(old_email) == 0):
            imapper.quit()
            imapper = easyimap.connect('imap.gmail.com', login, password)
            print("Maj")
            i = 1
        elif (i > 20):
            i = 1
        new_email = list()
        try:
            
            for mail_id in imapper.listids(limit=100):
                mail = imapper.mail(mail_id)
                new_email.append(mail)

            if(len(new_email) > len(old_email)):
                traitement_mail(new_email[0])
            
            old_email = new_email
            
            
            
        except IndexError as e:
            print(e)
        except TypeError as e:
            print("Des messages ont été supprimés")
        old_email = new_email
        


def traitement_mail(mail):
    save_email = open("save_mail.txt",'w')
    print("Y a un nouveau mail")
    save_email.write("From : " + str(mail.from_addr))
    save_email.write("Return path : " + str(mail.return_path))
    save_email.write("")
    save_email.write("Body :\n" + str(mail.body))
    
    save_email.close()
    return 0


run()
