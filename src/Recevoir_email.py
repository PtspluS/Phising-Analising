import easyimap, re
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
            boucle = 0
            save_id = 0
            for mail_id in imapper.listids(limit=100):
                if boucle == 0:
                    save_id = mail_id
                boucle += 1
                mail = imapper.mail(mail_id)
                new_email.append(mail)
            
            if(len(new_email) > len(old_email)):
                print(save_id)
                traitement_mail(new_email[0])
            
            old_email = new_email
            
        except TypeError as e:
            print(e)
        old_email = new_email

    imapper.quit()  


def traitement_mail(mail):
    save_email = open("save_mail.txt",'w')
    print("Nouveau mail")
    for att in dir(mail):
        if(re.match(r'^[a-zA-Z]',att)):
            save_email.write(att)
            save_email.write(" : ")
            save_email.write(str(getattr(mail,att)))
            save_email.write("\n")
    save_email.close()
    return 0


run()
