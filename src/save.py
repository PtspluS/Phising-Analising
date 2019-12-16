import pymongo
from hashlib import sha3_512
import os

client = pymongo.MongoClient("localhost", 27017)

def save(Email, marks, path = 'localhost:27017', port = 0, grade = 0):
    """

    :param Email: Email object
    :param marks: All the marks for the Email
    :param path: The path to the data base
    :param port: The port for the data base
    :return: True if no problem or False if they are
    """

    key = sha3_512((Email.raw).encode('utf-8')).hexdigest()

    data = {'key': key, 'marks': marks, 'grade': grade}
    try:
        if port == 0 and path == 'localhost:27017':
            client = pymongo.MongoClient()
        elif port == 0 and path != 'localhost:27017':
            client = pymongo.MongoClient(path, port=port)
        else :
            client = pymongo.MongoClient(path)

        db = client.Project
        col = db.mails
        col.insert_one(data)

        return True
    except Exception as e:
        print(e)
        return False

