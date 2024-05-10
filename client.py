import threading
import socket

name=input("What's your name: ")

Client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Client.connect((socket.gethostname(), 54321 ))

def receive():
    while True:
     try:
        message=Client.recv(1024).decode("ascii")
        if message =="nick":
            Client.send(name.encode("ascii"))
        else:
            print(message)
     except:
         print("an error occurred")
         Client.close()
         break

def write():
    while True:
      message=f"{name}=> {input("")} "
      Client.send(message.encode("ascii"))

receive_thread=threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()
