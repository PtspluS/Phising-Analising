# imports
import numpy as np
from src.Neural_Network import Network
from src.Email import Email
import os
from src.save import save
from src.Analyser import mark_email

# datas ################################################################################################################
path_correct = "../data/Spam_mail/mail_convert/"
path_incorrect = "../data/mail_invalide/invalide/"

correct_email = []
incorrect_email = []

training_data = []
target_data = []

# fonction #############################################################################################################
def load(path):
    mails = []
    for f in os.listdir(path):
        mail = Email(os.path.join(path, f))
        mails.append(mail)

    return mails

# create data ##########################################################################################################
correct_email = load(path_correct)
incorrect_email = load(path_incorrect)

for mail in correct_email:
    training_data.append(mark_email(mail))
    target_data.append(1)
    save(mail, mark_email(mail), grade=1)

for mail in incorrect_email:
    training_data.append(mark_email(mail))
    target_data.append(0)
    save(mail, mark_email(mail), grade=0)

# run training #########################################################################################################
bot = Network(create=True)

bot.train(training_data=training_data, target_data=target_data, epochs=1)
# test #################################################################################################################



