from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)   
        self.buttons_list = []
        self.mapa = ["V1", "A1", "Branco", "V2", "A2"]
        self.whitebtn = 2        
        self.master = master
        self.init_window()
        self.init_image()
        self.init_button()
        self.init_chat()
        
    #Creation of init_window
    def init_window(self):
        # changing the title of our master widget      
        self.master.title("Jogo Chinês")
        # allowing the widget to take the full space of the root window
        self.pack()
        #criar o canvas das linhas do jogo 
        #background = Canvas(self, height=640, width=480, bg="yellow") 
        #background.pack()
    
    def init_button(self):
        # creating a button instance
        self.loadimageV = PhotoImage(file="bolaV.png")
        self.loadimageA = PhotoImage(file="bolaA.png")
        self.loadimageB = PhotoImage(file="bolaBr.png")
        #Link para criar botões arredondados : https://stackoverflow.com/questions/42579927/rounded-button-tkinter-python
        botaoV1 = Button(self, image=self.loadimageV, border=0, bg="white") #Adicionar comando com quitButton = Button(self, bg="x", ->command= helloCallBack <-)
        botaoA1 = Button(self, image=self.loadimageA, border=0, bg="white")
        botaoBranco = Button(self, image=self.loadimageB, border=0, bg="white")
        botaoV2 = Button(self, image=self.loadimageV, border=0, bg="white")
        botaoA2 = Button(self, image=self.loadimageA, border=0, bg="white")
        self.buttons_list.extend([botaoV1, botaoA1, botaoBranco, botaoV2, botaoA2])
        botaoV1.bind("<Button-1>", self.movement)
        botaoV2.bind("<Button-1>", self.movement)
        botaoA1.bind("<Button-1>", self.movement)
        botaoA2.bind("<Button-1>", self.movement)
        #botaoBranco.bind("<Button-1>", self.movement)
        # placing the button on my window
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
        self.messages.insert(INSERT, '%s\n' % input_get)
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
        print(event)
        btn = event.widget
        btn_place = self.buttons_list.index(btn)
        btn.config(image=self.loadimageB)
        if(btn_place == self.mapa.index("V1") or btn_place == self.mapa.index("V2")):
            self.buttons_list[self.whitebtn].config(image=self.loadimageV)
            #Atualizando a lista dos botoes, e em seguida, a lista do mapa.
            #self.buttons_list[self.whitebtn], self.buttons_list[btn_place] = self.buttons_list[btn_place], self.buttons_list[self.whitebtn]
            self.mapa[self.whitebtn], self.mapa[btn_place] = self.mapa[btn_place], self.mapa[self.whitebtn]
            print(self.mapa)
            self.whitebtn = btn_place
            #Disabilitar os botões vermelhos
            self.buttons_list[self.mapa.index("V1")].config(state = "disabled")
            self.buttons_list[self.mapa.index("V2")].config(state = "disabled")
        else:
            self.buttons_list[self.whitebtn].config(image=self.loadimageA)
        """btn.config(image=self.loadimageB)
        self.buttons_list[self.whitebtn].config(image=self.loadimageV)
        self.whitebtn = btn_place"""
        print(self.buttons_list[4])
        print(self.buttons_list.index(btn))
        print(self.buttons_list)


        

root = Tk()
#size of the window
root.geometry("800x400")
app = Window(root)
root.mainloop()  