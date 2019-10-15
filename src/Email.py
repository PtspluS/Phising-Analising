class Email():

    def __init__(self, from_add, dir_add, obj='None object', corps='No body'):#from_add = sender adress, dir_add = receiver adress, obj = object of the mail, corps = text of the mail
        self.from_add = str(from_add)
        self.dir_add = str(dir_add)
        self.message = 'Subject:'+obj+'\n\n'+corps

    # get the message
    def getMessage(self):
        return self.message

    def setMessage(self, m):
        self.message = m

    # get the receiver
    def getDir(self):
        return self.dir_add

    # set the sender adresse
    def setFrom(self, add):#adress
        self.from_add = add