import smtplib, ssl

def run():
        

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "yncrea.test.projet.M1@gmail.com"
    receiver_email = "qboens@hotmail.fr"
    password = "ujikolpm"
    message = """\
    Subject: Hi there

    L'envoi d'un merveilleux message"""
    context = ssl.create_default_context()
    try : 
        with smtplib.SMTP(smtp_server, port) as server:
            #server.set_debuglevel(1)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            
            server.quit()
    except smtplib.SMTPException as e :
        print(e)
        
    
run()
