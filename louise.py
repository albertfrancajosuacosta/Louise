from tkinter import Tk, messagebox
from tkinter import Menu
from util import Util
from janelaNormalidade import JanelaNormalidade
from janelaHipoteseParametrico2Grupos import JanelaHipoteseParametrico2Grupos



class Louise(Tk):

    def __init__(self):

        super().__init__()
        self.versao = 0.1
        self.util = Util()
        self.definirConfiguracoes(rezisableLargura=True,rezisableAltura=True)
        self.definirBarraMenu()

    def definirConfiguracoes(self,rezisableLargura=True,rezisableAltura=True):
        
        self.title("Louise - Teste de Hipótese - Versão "+str(self.versao))
        self.iconbitmap('C:\\Users\\alber\\Documents\\LabMax\\Louise\\img\\lamed.ico')
        self.resizable(width=rezisableLargura, height=rezisableAltura)
        self.larguraDispositivo, self.alturaDispositvo = self.util.tamanhoTelaDispositivo(self,1.00,1.00)
        self.configure(background=self.util.corFundoTela)
        #x, y = util.posicaoJanelaCentralizada(self,int(larguraDispositivo*0.80), int(alturaDispositvo*0.80))
        self.geometry("{}x{}+{}+{}".format(self.util.larguraTela,self.util.alturaTela,0,0))
        self.larguraTelaPrincipal = int(self.larguraDispositivo*0.80)
        self.alturaTelaPrincipal = int(self.alturaDispositvo*0.80)


    def definirBarraMenu(self):
        self.barraMenu = Menu(self)
        self.menuTestes = Menu(self.barraMenu,tearoff=False)
        self.menuTestes.add_command(label='Normalidade',
                                    #accelerator="Crtl+N",
                                    activebackground="#324aa8",
                                    command= lambda: self.showJanelaNormalidade()
                                    )
        self.subMenuHipotese = Menu(self.menuTestes, tearoff=0)
        self.subMenuHipoteseP = Menu(self.subMenuHipotese, tearoff=False)
        self.subMenuHipoteseP.add_command(label='2 grupos', command=lambda: self.showJanelaHipoteseParametrico2grupos())
        #self.subMenuHipoteseP.add_command(label='> 2 grupos', command=lambda: print('P > 2 grupos'))
        self.subMenuHipotese.add_cascade(label="Paramétrico",menu=self.subMenuHipoteseP)
        
        #self.subMenuHipoteseNP = Menu(self.subMenuHipotese, tearoff=False)
        #self.subMenuHipoteseNP.add_command(label='2 grupos', command=lambda: print('NP 2 grupos'))
        #self.subMenuHipoteseNP.add_command(label='> 2 grupos', command=lambda: print('NP > 2 grupos'))
        #self.subMenuHipotese.add_cascade(label="Não Paramétrico", menu=self.subMenuHipoteseNP)

        self.menuTestes.add_cascade(label='Hipóteses',
                                    activebackground="#324aa8",
                                    menu=self.subMenuHipotese
                                    )

        self.barraMenu.add_cascade(label='Testes',menu=self.menuTestes)

        self.barraMenu.add_command(label='Sobre', command=lambda: self.showSobre())
        
        self.barraMenu.add_command(label='Sair',command=self.destroy)

        self.config(menu=self.barraMenu)

    def showJanelaNormalidade(self):
        JanelaNormalidade(larguraMae=self.larguraTelaPrincipal, alturaMae=self.alturaTelaPrincipal)

    def showJanelaHipoteseParametrico2grupos(self):
        JanelaHipoteseParametrico2Grupos(larguraMae=self.larguraTelaPrincipal, alturaMae=self.alturaTelaPrincipal)

    def showSobre(self):
            messagebox.showinfo("Sobre Louise", "Louise é um projeto com objetivo de desenvolver uma ferramenta livre com suporte à interface gráfica para a realização de teste de hipótese.\n Contato: albertfrancajosuacosta@gmail.com") 
            

if __name__=="__main__":
    louise = Louise()
    louise.mainloop()
