# imports
import numpy as np
from src.Neural_Network import Network
from src.Email import Email
import os
import email

# datas ################################################################################################################
path_correct = "./data/Spam_mail/mail_convert/"
path_incorrect = "./data/mail_invalide/invalide/"

correct_email = []
incorrect_email = []

training_data = []
target_data = []

# create correct data


# run training #########################################################################################################
#bot = Network(create=True)

# test #################################################################################################################
f = open("email1.txt", 'r')
msg = email.message_from_file(f)
f.close()
e = Email(msg)

print(e.get_sender())
