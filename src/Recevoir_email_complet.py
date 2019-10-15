import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('yncrea.test.projet.M1@gmail.com', 'ujikolpm')
mail.list() 
mail.select('inbox')

while True :
    result, data = mail.uid('search', None, "ALL")
    i = len(data[0].split())
    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = email_data[0][1]

        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
    for part in email_message.walk():
        
            
        #body = part.get_payload(decode=True)
        save_string = r"C:\\Users\\qboen\\Desktop\\02-Projet\\00-Fishing\\Phising-Analising\\src\\email" + str(x) + ".txt"
        myfile = open(save_string, 'a')
        myfile.write(str(part))
        myfile.close()
    
