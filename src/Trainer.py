# imports
from src.Neural_Network import Network
from src.Email import Email
import os
from src.save import save, load_bdd
from src.Analyser import mark_email
import numpy as np

# datas ################################################################################################################
path_correct = "../data/Spam_mail/mail_convert/"
path_incorrect = "../data/mail_invalide/invalide/"

correct_email = []
incorrect_email = []

training_data = []
target_data = []

# fonction #############################################################################################################
def load(path, num):
    mails = []
    for f in os.listdir(path):
        mail = Email(os.path.join(path, f), num)
        mails.append(mail)
        num += 1

    return mails, num

def evaluate(list_emails, stop = -1):
    i = 0
    try:
        for emails in list_emails:
            for mail in emails[0]:
                if stop <= mail.num:
                    mark = mark_email(mail)
                    target = list_emails[1]
                    training_data.append(np.array(mark, dtype=np.float32))
                    target_data.append(target_data)
                    save(mail, mark, grade=target_data)
                    i = mail.num
                elif stop >= mail.num:
                    mark, grade = load_bdd(mail)
                    training_data.append(np.array(mark, dtype=np.float32))
                    target_data.append(grade)
                    i = mail.num
    except Exception as e:
        print(e)
        print('Num email stop at = '+str(i))
        False

# create data ##########################################################################################################
i = 0
correct_email, i = load(path_correct, i)
incorrect_email = load(path_incorrect, i)

list_emails = [(correct_email, 1), (incorrect_email, 0)]

stop_at = 500

if not evaluate(list_emails, stop=stop_at):
    evaluate(list_emails[1], stop=stop_at)
print('evaluate finish')

# run training #########################################################################################################
bot = Network(create=True, size_inputs=len(training_data[0]))

bot.train(training_data=np.array(training_data), target_data=np.array(target_data), epochs=1000, batch_size=10, verbose=1)

bot.save()
# test #################################################################################################################



