from tkinter import *
from PIL import Image, ImageTk

BUTTON_LARGURA = "4"
BUTTON_ALTURA = "2"

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)                 
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
        botaoV2 = Button(self, image=self.loadimageV, border=0, bg="white")
        botaoA1 = Button(self, image=self.loadimageA, border=0, bg="white")
        botaoA2 = Button(self, image=self.loadimageA, border=0, bg="white")
        botaoBranco = Button(self, image=self.loadimageB, border=0, bg="white")
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
        

root = Tk()
#size of the window
root.geometry("800x400")
app = Window(root)
root.mainloop()  