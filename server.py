import socket
from tkinter import *
from _thread import *
import threading
import sys
import pickle
import tkinter

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.clients = []
        self.clients_lock = threading.Lock()
        self.master = master
        self.init_window()
        self.init_layout()
        #self.sock = socket.socket()
        #self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def init_window(self):
        self.master.title("Configuração do servidor")
        self.pack()
    def init_layout(self):
        input_port = StringVar()
        text = Label(self, text="Porta: ")
        text.grid(row = 1, column=1)
        #text1 = Label(self, text="IP host: ")
        #text1.grid(row=2, column=1)
        self.entryPort = Entry(self, text=input_port)
        self.entryPort.grid(row = 1, column=2)
        botaoOk = Button(self, text="OK")
        botaoOk.grid(row = 1, column=3, rowspan=2, columnspan=2)
        botaoOk.bind("<Button-1>", self.get_port)
        self.portLabel = Label(self, text="")
        self.portLabel.grid(row=3, column=2)
        self.hostLabel = Label(self, text="")
        self.hostLabel.grid(row=4, column=2)
    #Evento que dispara quando clica no Ok
    def get_port(self,event):
        self.inputPort = ""
        self.inputPort = self.entryPort.get()
        #self.inputHost = self.entryHost.get()
        self.portLabel.config(text="Porta escolhida: "+self.inputPort)
        self.hostLabel.config(text="Host escolhido: "+ socket.gethostbyname("localhost"))
        #Atualiza o frame do servidor para mostrar a porta e o IP dele
        self.master.update()
        #Conecta à porta e IP estabelecidos
        host = socket.gethostbyname("localhost")
        print("IP do servidor: "+ host)
        print("Porta do servidor: "+ str(self.inputPort))
        porta = int(self.inputPort)
        self.connect(host,porta)
    
        #Novo connect com threads
    def connect(self,host,port):
        self.sock.bind((host,port))
        self.sock.listen()
        while True:
            client, address = self.sock.accept()
            print("Conectado a: ",str(client), "address: ", str(address))
            threading.Thread(target=self.listenToClient, args=(client,address)).start()

    def listenToClient(self, client, address):
        with self.clients_lock:
            self.clients.append(client)
        try:
            while True:
                data = client.recv(1024)
                if data:
                    response = data.decode('utf-8')
                    print(response)
                    new_response = response.split()
                    print(new_response)
                    with self.clients_lock:
                        for c in self.clients:
                            c.sendall(str.encode(response))
                else:
                    break
        finally:
            with self.clients_lock:
                self.clients.remove(client)
                client.close()

root = Tk()
#root.geometry("200x100")
app = Application(root)
root.mainloop()


#Codigo legado

"""try:
            print('1')
            self.sock.bind((host, int(port)))
            print('2')
            self.sock.listen(5)
            while True:
                print('crashou')
                socket, address = self.sock.accept()
                socket.settimeout(5)
                threading.Thread(target = self.listenToClient, args=(socket, address)).start()
        except:
            print('entrou except')"""

"""def connect(self,host,port):
        self.sock.bind((host,port))
        self.sock.listen()
        while True:
            client, address = self.sock.accept()
            try:
                print('conexao de address' + str(address))
                data = client.recv(4096)
                if data:
                    response = data.decode('utf-8')
                    print(response)
                    new_response = response.split()
                    print(new_response)
                    client.sendall(str.encode(response))
                else:
                    break
            finally:
                client.close()"""