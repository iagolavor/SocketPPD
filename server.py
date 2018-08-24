import socket
from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
        self.init_layout()
    def init_window(self):
        self.master.title("Configuração do servidor")
        self.pack()
    def init_layout(self):
        self.input_user = StringVar()
        text = Label(self, text="Porta: ")
        text.grid(row = 1, column=1)
        self.entry = Entry(self, text=self.input_user)
        self.entry.grid(row = 1, column=2)
        self.entry.bind("<Return>", self.get_port)
        botaoOk = Button(self, text="OK")
        botaoOk.grid(row = 1, column=3)
        botaoOk.bind("<Button-1>", self.get_port)
        self.portLabel = Label(self, text="")
        self.portLabel.grid(row=2, column=2)
    def get_port(self,event):
        input = self.entry.get()
        self.portLabel.config(text="Porta escolhida: "+input)
        print(input)
        return input

root = Tk()
#root.geometry("200x100")
app = Application(root)
root.mainloop()