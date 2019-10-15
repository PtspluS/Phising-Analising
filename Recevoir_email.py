import easyimap

login = 'yncrea.test.projet.M1@gmail.com'
password = 'ujikolpm'

imapper = easyimap.connect('imap.gmail.com', login, password)
for mail_id in imapper.listids(limit=100):
    mail = imapper.mail(mail_id)
    print(mail.from_addr)
    print(mail.to)
    print(mail.cc)
    print(mail.title)
    print(mail.body)
    print(mail.attachments)
