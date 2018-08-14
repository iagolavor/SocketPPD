from tkinter import *

BUTTON_LARGURA = "4"
BUTTON_ALTURA = "2"

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):
        # changing the title of our master widget      
        self.master.title("Jogo Chinês")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        #criar o canvas das linhas do jogo 
        background = Canvas(self, height=640, width=480, bg="yellow") 
        # creating a button instance
        #Link para criar botões arredondados : https://stackoverflow.com/questions/42579927/rounded-button-tkinter-python
        botaoV1 = Button(self, text="", width=BUTTON_LARGURA, height=BUTTON_ALTURA, bg="red") #Adicionar comando com quitButton = Button(self, bg="x", ->command= helloCallBack <-)
        botaoV2 = Button(self, text="", width=BUTTON_LARGURA, height=BUTTON_ALTURA, bg="red")
        botaoA1 = Button(self, text="", width=BUTTON_LARGURA, height=BUTTON_ALTURA, bg="blue")
        botaoA2 = Button(self, text="", width=BUTTON_LARGURA, height=BUTTON_ALTURA, bg="blue")
        botaoBranco = Button(self, text="", width=BUTTON_LARGURA, height=BUTTON_ALTURA, bg="white")
        # placing the button on my window
        botaoV1.place(x=100, y=20)
        botaoV2.place(x=380, y=20)
        botaoA1.place(x=100, y=220)
        botaoA2.place(x=380, y=220)
        botaoBranco.place(x=240, y=120)
        background.pack()

root = Tk()
#size of the window
root.geometry("640x480")
app = Window(root)
root.mainloop()  