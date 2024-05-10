
################# concurent chat #####################################
from socket import *
import threading

s= socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1",1234))

while True:
    y=input("client:")
    s.send(y.encode("utf-8"))
    
    x=s.recv(2048)
    print("server:",x.decode("utf-8"))
s.close()


