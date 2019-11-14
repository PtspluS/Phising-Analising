import smtplib
import ssl

import Email
from Link_analyser import *


class Mail_box(object):

    def __init__(self, adress, pw, port=587):# adress = adress email, pw = passe word, port (by default 587)
        self.port = port  # For starttls
        self.smtp_server = "smtp.gmail.com"
        self.sender_email = adress
        self.password = pw

    def send_mail(self, mail, debug=False):
        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            if debug:
                server.set_debuglevel(1)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, mail.dir_add, mail.message)
            server.quit()

sender_email = "yncrea.test.projet.M1@gmail.com"
receiver_email = "yncrea.test.projet.M1@gmail.com"
password = "ujikolpm"
message = 'Test'

mail_box = Mail_box(sender_email, password)
email = Email.Email("", receiver_email, "test", "testy test")
mail_box.send_mail(email)
pasta()