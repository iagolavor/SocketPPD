import socket
from tkinter import *
from _thread import *
import threading
import sys

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
        self.init_layout()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def init_window(self):
        self.master.title("Configuração do servidor")
        self.pack()
    def init_layout(self):
        self.input_port = StringVar()
        self.input_host = StringVar()
        text = Label(self, text="Porta: ")
        text.grid(row = 1, column=1)
        text1 = Label(self, text="IP host: ")
        text1.grid(row=2, column=1)
        self.entryPort = Entry(self, text=self.input_port)
        self.entryPort.grid(row = 1, column=2)
        self.entryPort.bind("<Return>", self.get_port)
        self.entryHost = Entry(self, text=self.input_host)
        self.entryHost.grid(row = 2, column=2)
        self.entryHost.bind("<Return>", self.get_port)
        botaoOk = Button(self, text="OK")
        botaoOk.grid(row = 1, column=3, rowspan=2, columnspan=2)
        botaoOk.bind("<Button-1>", self.get_port)
        self.portLabel = Label(self, text="")
        self.portLabel.grid(row=3, column=2)
        self.hostLabel = Label(self, text="")
        self.hostLabel.grid(row=4, column=2)
    #Evento que dispara quando clica no Ok
    def get_port(self,event):
        self.inputPort = self.entryPort.get()
        self.inputHost = self.entryHost.get()
        self.portLabel.config(text="Porta escolhida: "+self.inputPort)
        self.hostLabel.config(text="Host escolhido: "+self.inputHost)
        #Conecta à porta e IP estabelecidos
        self.connect(self.inputHost, self.inputPort)
    def connect(self, host, port):
        try:
            port = int(port)
            self.sock.bind((host, port))
            self.sock.listen(5)
            while True:
                socket, address = self.sock.accept()
                socket.settimeout(600)
                threading.Thread(target = self.listenToClient, args=(socket, address)).start()
        finally:
            socket.close()
    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    #Colocar a resposta para fazer um echo com data
                    response = data.decode('utf-8')
                    client.send(str.encode(response))
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False
    """def listen_to_client(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)"""

root = Tk()
#root.geometry("200x100")
app = Application(root)
root.mainloop()