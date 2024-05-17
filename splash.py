from tkinter import *
from PIL import Image 

splash = Tk()
altura = 500
largura = 500

x = (splash.winfo_screenwidth()//2)-(largura//2)
y = (splash.winfo_screenheight()//2)-(altura//2)

splash.geometry('{}x{}+{}+{}'.format(largura,altura,x,y))

backgroundImage = PhotoImage(file='C:\\Users\\alber\\Documents\\LabMax\\Louise\\img\\Background.png')

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

gifImage = "C:\\Users\\alber\\Documents\\LabMax\\Louise\\img\\load.gif"


openImage = Image.open(gifImage)

frames = openImage.n_frames

imageObject = [PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]

count = 0

showAnimation = None

def animation(count):
    global showAnimation
    newImage = imageObject[count]

    gif_Label.configure(image=newImage)
    count += 1
    if count == frames:
        count = 0
    showAnimation = splash.after(50, lambda: animation(count))


gif_Label = Label(splash, image="")
gif_Label.place(x=200, y=220, width=100, height=100)




def main_window():

    splash.withdraw()

    window = Tk()
    window.configure(bg="#525561")
    window.geometry("1240x650")

    altura = 1240
    largura = 650

    x = (window.winfo_screenwidth()//2)-(largura//2)
    y = (window.winfo_screenheight()//2)-(altura//2)

    window.geometry('{}x{}+{}+{}'.format(largura,altura,x,y))

    def ExitWindow():
        window.quit()
    window.protocol("WM_DELETE_WINDOW", ExitWindow)


splash.after(3000,main_window)

animation(count)

splash.mainloop()