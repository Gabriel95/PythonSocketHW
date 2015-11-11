class Client:
    def __init__(self, username, name, email, id, birthday, foto):
        self.username = username
        self.name = name
        self.email = email
        self.id = id
        self.birthday = birthday
        self.foto = foto
    def toString(self):
        return (self.username + ', ' + self.name + ', ' + self.email + ', ' + self.id + ', ' + self.birthday + ', ' + self.foto)
