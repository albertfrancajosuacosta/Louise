from tkinter import *
from PIL import Image
import ttkbootstrap as ttk
from Main_Louise import Main_Louise
from util.util import Util

splash = Tk()
altura = 500
largura = 500

util = Util()

x = (splash.winfo_screenwidth()//2)-(largura//2)
y = (splash.winfo_screenheight()//2)-(altura//2)

splash.geometry('{}x{}+{}+{}'.format(largura,altura,x,y))

backgroundImage = PhotoImage(file=util.CAMINHO_IMAGEM.__str__()+'\\Background.png')

bg_image = Label(
    splash,
    image=backgroundImage
)
bg_image.pack()

splash.overrideredirect(True)

labelAguarde = Label(
    splash,
    text="LabMax",
    font=("yu gothic ui bold", 30 * -1),
    bg="#1F41A9",
    fg="#ed9c32"
)
labelAguarde.place(x=200, y=100)

labelAguarde = Label(
    splash,
    text="Aguarde...",
    font=("yu gothic ui bold", 15 * -1),
    bg="#1F41A9",
    fg="#FFFFFF"
)
labelAguarde.place(x=220, y=350)


gifImage = util.CAMINHO_IMAGEM.__str__()+'\\load.gif'

openImage = Image.open(gifImage)

frames = openImage.n_frames

imageObject = [PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]

count = 0

showAnimation = None


gif_Label = Label(splash, image="")
gif_Label.place(x=200, y=220, width=100, height=100)



def main_window():

    splash.destroy()

    app = ttk.Window()
    Main_Louise(app)
    app.mainloop()


def animation(count):
    global showAnimation
    newImage = imageObject[count]
    gif_Label.configure(image=newImage)
    count += 1
    if count == frames:
        count = 0
    showAnimation = splash.after(50, lambda: animation(count))


animation(count)

splash.after(5000, lambda: main_window())


splash.mainloop()