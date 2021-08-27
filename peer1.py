import socket
import ssl
import threading
import time
from tkinter import*

from tkinter import ttk

class Screen():
    def __init__(self):
        self.i = 0
        self.root = Tk()
        self.root.geometry("300x200")
        self.t = Text(self.root, height=500, width=200)      
        self.t.pack()
        self.root.bind('<Return>', self.callback)
        self.root.mainloop()
        self.input = ''
    
    def getInput(self):
        self.input = "fdsfdsdsf"
       
      

    def type(self):
        input = self.t.get("1.0", "end-1c")
        self.t.insert(END,input)
        print(input)
     

    def callback(self, event): 
        print(self.input)
        if(event.keysym): 
            self.t.insert(END,self.input)         
            self.t.insert(END,"")
    

def receive():
    HOST = '127.0.0.1'  # this peer
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

def send():#client
    HOST = '127.0.0.2'  # peer destine
    PORT = 60000        # peer destine
    while(True):
        try:
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


   
   
