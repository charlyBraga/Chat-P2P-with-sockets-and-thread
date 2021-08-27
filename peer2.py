import socket
import ssl
import threading
import time

def receive():
   
    HOST = '127.0.0.2'  # this peer
    PORT = 60000        # this peer
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
        print("Conectado...")          
        s.bind((HOST, PORT))
        while(True):
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if data:
                        print("Receber: " + data.decode())
                    break
                                   
      
def send():
    HOST = '127.0.0.1'  # peer destine
    PORT = 60000        # peer destine
    while(True):
        try:
            #text = input("Type value in peer2: ")
            text = input()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(str.encode(text))
                data = s.recv(1024)
        except:
            pass

time.sleep(5)

try:
    th1 = threading.Thread(target=receive, args=())
    th1.start()   
except:
    pass 
try:         
    th2 = threading.Thread(target=send, args=())
    th2.start()
except:
    pass 
   
