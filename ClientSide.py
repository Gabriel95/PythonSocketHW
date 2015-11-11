# Echo client program
import socket
import Validations
from Client import Client
HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Connected!')
option = True
while option:
    print ("""
    1.Add Users
    2.View User in Console
    3.Delete User
    4.Send User To Email
    5.Exit """)
    option = input("")
    if option == "1":
        sentinel = True
        while(sentinel):
            sentinel = False
            username = input("Username: ")
            name = input("Name: ")
            email = input("Email: ")
            id = input("Id: ")
            birthday = input("Birthday: ")
            foto = input("Foto: ")
            if not Validations.isUserNameUnique(username):
                print("Username already exists")
                sentinel = True
            elif not Validations.isEmail(email):
                print("Invalid Email")
                sentinel = True
            elif not Validations.isId(id):
                print("Invalid Id")
                sentinel = True
            elif not Validations.isDate(birthday):
                print("Invalid Date")
                sentinel = True
            else:
                newclient = Client(username,name,email,id,birthday,foto)
                stringtosend = '1 ' + newclient.toString()
                s.send(stringtosend.encode('utf-8'))
                print("User Created!")

    elif option == "2":
        username = input("Username: ")
        stringtosend = '2 ' + username
        s.send(stringtosend.encode('utf-8'))
        response = s.recv(1024).decode('utf8')
        if response == ' ':
            print('User Not Found!')
        else:
            print(response)
    elif option == "3":
        username = input("Username: ")
        stringtosend = '3 ' + username
        s.send(stringtosend.encode('utf-8'))
        response = s.recv(1024).decode('utf8')
        if response == 'Ok':
            print("User Deleted!")
        else:
            print("User Not Found")
    elif option == "4":
        username = input("Username: ")
        stringtosend = '4 ' + username
        s.send(stringtosend.encode('utf-8'))
    elif option == "5":
        s.send(option.encode('utf-8'))
        print(s.recv(1024).decode('utf8'))
        break
#s.sendall(b'Hello, world')
#data = s.recv(1024)
#s.close()
print('Connection Closed')