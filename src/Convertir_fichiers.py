import os.path
import glob
import os

def run():
    l = glob.glob(os.getcwd()+'\spam\\*')
    num = 991
    for i in l:
        try:
            f = open(i,"r")
            file_conv = open(os.getcwd()+r'\mail_convert\invalide\mail_invalide_'+str(num)+'.txt','w')
            file_conv.write(f.read())
            file_conv.close()
            f.close()
        except:
            continue
        num += 1

run()
