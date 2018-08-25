from tkinter import *
import socket
import sys
from PIL import Image, ImageTk

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)   
        self.buttons_list = []       
        self.master = master
        self.init_window()
        self.init_image()
        self.init_button()
        self.init_chat()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    #Creation of init_window
    def init_window(self):
        # changing the title of our master widget      
        self.master.title("Jogo Chinês")
        # allowing the widget to take the full space of the root window
        self.pack()

        my_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        file = Menu(my_menu)
        file.add_command(label='Conectar a servidor', command=self.connect_to_server)
        my_menu.add_cascade(label='Menu', menu = file)
    
    def init_button(self):
        self.loadimageV = PhotoImage(file="bolaV.png")
        self.loadimageA = PhotoImage(file="bolaA.png")
        self.loadimageB = PhotoImage(file="bolaBr.png")
        botaoV1 = Button(self, image=self.loadimageV, border=0, bg="white") #Adicionar comando com quitButton = Button(self, bg="x", ->command= helloCallBack <-)
        botaoV1.image = self.loadimageV
        botaoA1 = Button(self, image=self.loadimageA, border=0, bg="white")
        botaoA1.image = self.loadimageA
        botaoBranco = Button(self, image=self.loadimageB, border=0, bg="white")
        botaoBranco.image = self.loadimageB
        botaoV2 = Button(self, image=self.loadimageV, border=0, bg="white")
        botaoV2.image = self.loadimageV
        botaoA2 = Button(self, image=self.loadimageA, border=0, bg="white")
        botaoA2.image = self.loadimageA
        self.buttons_list.extend([botaoV1, botaoA1, botaoBranco, botaoV2, botaoA2])
        #Adicionando os eventos a cada botao
        botaoV1.bind("<Button-1>", self.movement)
        botaoV2.bind("<Button-1>", self.movement)
        botaoA1.bind("<Button-1>", self.movement)
        botaoA2.bind("<Button-1>", self.movement)
        botaoBranco.bind("<Button-1>", self.movement)
        #Colocando os botoes na janela
        botaoV1.place(x=5, y=6)
        botaoV2.place(x=300, y=6)
        botaoA1.place(x=5, y=295)
        botaoA2.place(x=300, y=295)
        botaoBranco.place(x=155, y=142)

    def init_chat(self):
        self.messages = Text(self, height="23", width="49")
        self.input_user = StringVar()
        self.input_field = Entry(self, text=self.input_user)
        self.label_user = Label(self, text="Chat: ")
        self.input_field.bind("<Return>", self.send_message)
        self.messages.grid(row=0,column=1, columnspan=2, sticky=NW)
        self.label_user.grid(row=0,column=1, sticky=S+W)
        self.input_field.grid(row=0,column=2, ipadx=150, sticky=S)

    def send_message(self,event):
        input_get = self.input_field.get()
        print(input_get)
        self.messages.insert(INSERT, 'Jogador 1: %s\n' % input_get)
        self.input_user.set('')
        return "break"
    
    def init_image(self):
        load = Image.open("pong02.jpg")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.grid(row=0,column=0)
    
    def movement(self,event):
        #Chama a função switcher para escolher qual botao rodar
        btn = event.widget
        btn_place = self.buttons_list.index(btn)
        self.switcher(btn_place)

    def switcher(self,argument):
        #De acordo com o argumento dado(lugar do botao do evento), chama a função apropriada
        switch = {
            0: self.pos_0,
            1: self.pos_1,
            2: self.pos_2,
            3: self.pos_3,
            4: self.pos_4
        }
        func = switch.get(argument, lambda: "Invalid")
        func()
        self.my_send(self.buttons_list)

    def connect_to_server(self):
        print('to no connect')
        host = socket.gethostbyname()
        self.sock.connect((host,5000)) 
    def my_send(self, msg):
        self.sock.sendall(str.encode(msg))  
        amount_received = 0
        amount_expected = len(msg)
        while(amount_expected<amount_received):
            data = self.sock.recv(16)
            amount_received =+ len(data)
            print('received {!r}'.format(data))
    
    def pos_0(self):
        if(self.buttons_list[0].image == self.loadimageV):
            if(self.buttons_list[1].image == self.loadimageB):
                self.buttons_list[0].config(image = self.loadimageB)
                self.buttons_list[0].image = self.loadimageB
                self.buttons_list[1].config(image = self.loadimageV)
                self.buttons_list[0].image = self.loadimageV
            elif(self.buttons_list[2].image == self.loadimageB):
                self.buttons_list[0].config(image = self.loadimageB)
                self.buttons_list[0].image = self.loadimageB
                self.buttons_list[2].config(image = self.loadimageV)
                self.buttons_list[2].image = self.loadimageV
        elif(self.buttons_list[0].image == self.loadimageA):
            if(self.buttons_list[1].image == self.loadimageB):
                    self.buttons_list[0].config(image = self.loadimageB)
                    self.buttons_list[0].image = self.loadimageB
                    self.buttons_list[1].config(image = self.loadimageA)
                    self.buttons_list[1].image = self.loadimageA
            elif(self.buttons_list[2].image == self.loadimageB):
                    self.buttons_list[0].config(image = self.loadimageB)
                    self.buttons_list[0].image = self.loadimageB
                    self.buttons_list[2].config(image = self.loadimageA)
                    self.buttons_list[2].image = self.loadimageA
        
    def pos_1(self):
        if(self.buttons_list[1].image == self.loadimageV):
            if(self.buttons_list[0].image == self.loadimageB):
                self.buttons_list[1].config(image = self.loadimageB)
                self.buttons_list[1].image = self.loadimageB
                self.buttons_list[0].config(image = self.loadimageV)
                self.buttons_list[0].image = self.loadimageV
            elif(self.buttons_list[2].image == self.loadimageB):
                self.buttons_list[1].config(image = self.loadimageB)
                self.buttons_list[1].image = self.loadimageB
                self.buttons_list[2].config(image = self.loadimageV)
                self.buttons_list[2].image = self.loadimageV
            elif(self.buttons_list[4].image == self.loadimageB):
                self.buttons_list[1].config(image = self.loadimageB)
                self.buttons_list[1].image = self.loadimageB
                self.buttons_list[4].config(image = self.loadimageV)
                self.buttons_list[4].image = self.loadimageV
        elif(self.buttons_list[1].image == self.loadimageA):
            if(self.buttons_list[0].image == self.loadimageB):
                self.buttons_list[1].config(image = self.loadimageB)
                self.buttons_list[1].image = self.loadimageB
                self.buttons_list[0].config(image = self.loadimageA)
                self.buttons_list[0].image = self.loadimageA
            elif(self.buttons_list[2].image == self.loadimageB):
                self.buttons_list[1].config(image = self.loadimageB)
                self.buttons_list[1].image = self.loadimageB
                self.buttons_list[2].config(image = self.loadimageA)
                self.buttons_list[2].image = self.loadimageA
            elif(self.buttons_list[4].image == self.loadimageB):
                self.buttons_list[1].config(image = self.loadimageB)
                self.buttons_list[1].image = self.loadimageB
                self.buttons_list[4].config(image = self.loadimageA)
                self.buttons_list[4].image = self.loadimageA
        
    def pos_2(self):
        if(self.buttons_list[2].image == self.loadimageV):
            if(self.buttons_list[0].image == self.loadimageB):
                self.buttons_list[2].config(image = self.loadimageB)
                self.buttons_list[2].image = self.loadimageB
                self.buttons_list[0].config(image = self.loadimageV)
                self.buttons_list[0].image = self.loadimageV
            elif(self.buttons_list[1].image == self.loadimageB):
                self.buttons_list[2].config(image = self.loadimageB)
                self.buttons_list[2].image = self.loadimageB
                self.buttons_list[1].config(image = self.loadimageV)
                self.buttons_list[1].image = self.loadimageV
            elif(self.buttons_list[3].image == self.loadimageB):
                self.buttons_list[2].config(image = self.loadimageB)
                self.buttons_list[2].image = self.loadimageB
                self.buttons_list[3].config(image = self.loadimageV)
                self.buttons_list[3].image = self.loadimageV
            elif(self.buttons_list[4].image == self.loadimageB):
                self.buttons_list[2].config(image = self.loadimageB)
                self.buttons_list[2].image = self.loadimageB
                self.buttons_list[4].config(image = self.loadimageV)
                self.buttons_list[4].image = self.loadimageV
        elif(self.buttons_list[2].image == self.loadimageA):
            if(self.buttons_list[0].image == self.loadimageB):
                self.buttons_list[2].config(image = self.loadimageB)
                self.buttons_list[2].image = self.loadimageB
                self.buttons_list[0].config(image = self.loadimageA)
                self.buttons_list[0].image = self.loadimageA
            elif(self.buttons_list[1].image == self.loadimageB):
                self.buttons_list[2].config(image = self.loadimageB)
                self.buttons_list[2].image = self.loadimageB
                self.buttons_list[1].config(image = self.loadimageA)
                self.buttons_list[1].image = self.loadimageA
            elif(self.buttons_list[3].image == self.loadimageB):
                self.buttons_list[2].config(image = self.loadimageB)
                self.buttons_list[2].image = self.loadimageB
                self.buttons_list[3].config(image = self.loadimageA)
                self.buttons_list[3].image = self.loadimageA
            elif(self.buttons_list[4].image == self.loadimageB):
                self.buttons_list[2].config(image = self.loadimageB)
                self.buttons_list[2].image = self.loadimageB
                self.buttons_list[4].config(image = self.loadimageA)
                self.buttons_list[4].image = self.loadimageA
    def pos_3(self):
        if(self.buttons_list[3].image == self.loadimageV):
            if(self.buttons_list[2].image == self.loadimageB):
                self.buttons_list[3].config(image = self.loadimageB)
                self.buttons_list[3].image = self.loadimageB
                self.buttons_list[2].config(image = self.loadimageV)
                self.buttons_list[2].image = self.loadimageV
            elif(self.buttons_list[4].image == self.loadimageB):
                self.buttons_list[3].config(image = self.loadimageB)
                self.buttons_list[3].image = self.loadimageB
                self.buttons_list[4].config(image = self.loadimageV)
                self.buttons_list[4].image = self.loadimageV
        elif(self.buttons_list[3].image == self.loadimageA):
            if(self.buttons_list[2].image == self.loadimageB):
                self.buttons_list[3].config(image = self.loadimageB)
                self.buttons_list[3].image = self.loadimageB
                self.buttons_list[2].config(image = self.loadimageA)
                self.buttons_list[2].image = self.loadimageA
            elif(self.buttons_list[4].image == self.loadimageB):
                self.buttons_list[3].config(image = self.loadimageB)
                self.buttons_list[3].image = self.loadimageB
                self.buttons_list[4].config(image = self.loadimageA)
                self.buttons_list[4].image = self.loadimageA
        
    def pos_4(self):
        if(self.buttons_list[4].image == self.loadimageV):
            if(self.buttons_list[1].image == self.loadimageB):
                self.buttons_list[4].config(image = self.loadimageB)
                self.buttons_list[4].image = self.loadimageB
                self.buttons_list[1].config(image = self.loadimageV)
                self.buttons_list[1].image = self.loadimageV
            elif(self.buttons_list[2].image == self.loadimageB):
                self.buttons_list[4].config(image = self.loadimageB)
                self.buttons_list[4].image = self.loadimageB
                self.buttons_list[2].config(image = self.loadimageV)
                self.buttons_list[2].image = self.loadimageV
            elif(self.buttons_list[3].image == self.loadimageB):
                self.buttons_list[4].config(image = self.loadimageB)
                self.buttons_list[4].image = self.loadimageB
                self.buttons_list[3].config(image = self.loadimageV)
                self.buttons_list[3].image = self.loadimageV
        elif(self.buttons_list[4].image == self.loadimageA):
            if(self.buttons_list[1].image == self.loadimageB):
                self.buttons_list[4].config(image = self.loadimageB)
                self.buttons_list[4].image = self.loadimageB
                self.buttons_list[1].config(image = self.loadimageA)
                self.buttons_list[1].image = self.loadimageA
            elif(self.buttons_list[2].image == self.loadimageB):
                self.buttons_list[4].config(image = self.loadimageB)
                self.buttons_list[4].image = self.loadimageB
                self.buttons_list[2].config(image = self.loadimageA)
                self.buttons_list[2].image = self.loadimageA
            elif(self.buttons_list[3].image == self.loadimageB):
                self.buttons_list[4].config(image = self.loadimageB)
                self.buttons_list[4].image = self.loadimageB
                self.buttons_list[3].config(image = self.loadimageA)
                self.buttons_list[3].image = self.loadimageA

root = Tk()
#size of the window
root.geometry("800x400")
app = Window(root)
root.mainloop()  