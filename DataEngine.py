import os

def createFile():
    try:
        f = os.path.join(os.path.abspath('data.txt'))
        archive = open(f, 'r')
        archive.close()
    except:
        f = os.path.join(os.path.abspath('data.txt'))
        archive = open(f, 'w')
        archive.write('')
        archive.close()

def writeToFile(client):
    f = os.path.join(os.path.abspath('data.txt'))
    archive=open(f,'r+')
    archive.seek(0,2)
    archive.write(client+'\n')
    archive.close()

def searchFromFile(username):
    createFile()
    f = os.path.join(os.path.abspath('data.txt'))
    with open(f, 'r') as data:
        for user in data:
            if user.startswith(username):
                return user
    data.close()
    return ' '

def cleanFile():
    f = os.path.join(os.path.abspath('data.txt'))
    archive = open(f, 'w')
    archive.write('')
    archive.close()

def getAll():
    createFile()
    list = ''
    fn = os.path.join(os.path.abspath('Data.txt'))
    with open(fn, 'r') as inF:
        for line in inF:
            list+=line
        return list

def deleteFromFile(username):
    toDelete = searchFromFile(username)
    if toDelete == '':
        return 'Not Found'
    list = getAll().split("\n")
    cleanFile()
    for user in list:
        if (user+'\n') != toDelete:
            writeToFile(user)
    return 'Ok'




