import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('yncrea.test.projet.M1@gmail.com', 'ujikolpm')

old_mes_nb = -1
x = 1
while True:
    
    mail.list() 
    mail.select('inbox')


    result, data = mail.uid('search', None, "ALL")
    i = len(data[0].split())
    new_mes_nb = i

    if(old_mes_nb == -1):
        old_mes_nb = new_mes_nb
    

    if(new_mes_nb > old_mes_nb):
        print("NOUVEAU MESSAGE")
        latest_email_uid = data[0].split()[new_mes_nb - 1]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = email_data[0][1]

        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        for part in email_message.walk():
            save_string = r"C:\\Users\\qboen\\Desktop\\02-Projet\\00-Fishing\\Phising-Analising\\src\\email" + str(x) + ".txt"
            myfile = open(save_string, 'a')
            myfile.write(str(part))
            myfile.close()
        x += 1
        old_mes_nb = new_mes_nb
    elif(new_mes_nb < old_mes_nb):
        old_mes_nb = new_mes_nb

mail.list() 
mail.select('inbox')


result, data = mail.uid('search', None, "ALL")
print("Contenu data :",data)
i = len(data[0].split())
print("Nombre messages :",i)
new_mes_nb = i
"""
for x in range(i):
    latest_email_uid = data[0].split()[x]
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = email_data[0][1]

    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    
for part in email_message.walk():
    save_string = r"C:\\Users\\qboen\\Desktop\\02-Projet\\00-Fishing\\Phising-Analising\\src\\email" + str(x) + ".txt"
    myfile = open(save_string, 'a')
    myfile.write(str(part))
    myfile.close()
"""
