# Echo server program
import socket
import DataEngine
import EmailService

HOST = 'localhost'        # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    message = data.decode('utf-8')
    if message.startswith("1"):
        message = message[2:]
        DataEngine.createFile()
        DataEngine.writeToFile(message)
    elif message.startswith("2"):
        message = message[2:]
        searcheduser = DataEngine.searchFromFile(message)
        conn.send(searcheduser.encode('utf-8'))
    elif message.startswith("3"):
        message = message[2:]
        response = DataEngine.deleteFromFile(message)
        conn.send(response.encode('utf-8'))
    elif message.startswith("4"):
         message = message[2:]
         EmailService.send_simple_message(message)
    elif (message) == "5":
        conn.send('Recieved'.encode('utf-8'))
        break
conn.close()