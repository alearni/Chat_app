import threading
import socket
header = 10
port = 54321

Server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


Server.bind((socket.gethostname(),port))
Server.listen()
clients=[]
names=[]
def broadcast(message):
      for client in clients:
            client.send(message)
def handle(client):
 while True:
  try:
      x=client.recv(2048)
      broadcast(x)
  except:
        index=clients.index(client)
        clients.remove(client)
        client.close()
        name=names[index]
        broadcast(f"{name} left the chat".encode("ascii"))
        names.remove(name)
        break


def receive():
      while True:
            client,address=Server.accept()
            print(f"Connected with {address}" )

            client.send("nick".encode("ascii"))
            name=client.recv(1024).decode("ascii")
            names.append(name)
            clients.append(client)
            print(f"Client {name} joined the chat")

            broadcast(f"Client {name} joined the chat".encode("ascii"))
            client.send("Connected To The Sever".encode("ascii"))

            thread=threading.Thread(target=handle,args=(client,))
            thread.start()

receive()


