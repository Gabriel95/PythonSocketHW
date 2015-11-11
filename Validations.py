import re
import DataEngine


def isUserNameUnique(username):
    user = DataEngine.searchFromFile(username)
    return user == ' '


def isEmail(email):
    return re.match(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email) is not None


def isId(id):
        match = re.match(r'\d{4}-\d{4}-\d{5}', id)
        if match:
            return True
        else:
            return False

def isDate(date):
    return re.match(r'\d{2}/\d{2}/\d{4}',date) is not None
