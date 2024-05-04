from tkinter import HORIZONTAL, NO, VERTICAL, Scrollbar, Tk, messagebox
from tkinter import ttk
from tkinter import Menu
from tkinter import Frame
from util import Util
from janelaNormalidade import JanelaNormalidade



class Louise(Tk):

    
    def __init__(self):

        super().__init__()


        

        self.title("Louise - Teste de Hipótese")
        self.iconbitmap('C:\\Users\\alber\\Documents\\LabMax\\Louise\\img\\lamed.ico')
        #self.resizable(width=False, height=False)

        util = Util()

        larguraDispositivo, alturaDispositvo = util.tamanhoTelaDispositivo(self,1.00,1.00)

        self.configure(background=util.corFundoTela)

        #x, y = util.posicaoJanelaCentralizada(self,int(larguraDispositivo*0.80), int(alturaDispositvo*0.80))
        
        self.geometry("{}x{}+{}+{}".format(util.larguraTela,util.alturaTela,0,0))


        larguraTelaPrincipal = int(larguraDispositivo*0.80)
        alturaTelaPrincipal = int(alturaDispositvo*0.80)

    

        barraMenu = Menu(self)


        menuTestes = Menu(barraMenu,tearoff=False)
        menuTestes.add_command(
            label='Normalidade',
            accelerator="Crtl+N",
            activebackground="#324aa8",
            command= lambda: JanelaNormalidade(larguraMae=larguraTelaPrincipal, alturaMae=alturaTelaPrincipal)

        )

        menuTestes.add_command(
            label='Hipótese',
            accelerator="Crtl+H",
            activebackground="#324aa8",
            command=lambda: print('Hipótese')
        )

        barraMenu.add_cascade(label='Testes',menu=menuTestes)

        barraMenu.add_command(label='Sobre',
                              command=lambda: self.showSobre())
        
        barraMenu.add_command(label='Sair', 
                              command=self.destroy)

        self.config(menu=barraMenu)


    def showSobre(self):
            messagebox.showinfo("Sobre Louise", "Louise é um projeto com objetivo de desenvolver uma ferramenta livre com suporte à interface gráfica para a realização de teste de hipótese.\n Contato: albertfrancajosuacosta@gmail.com") 
            



louise = Louise()
louise.mainloop()
