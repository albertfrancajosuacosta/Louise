from datetime import datetime
import os
from random import choices
from tkinter import Label
import ttkbootstrap as ttk
from ttkbootstrap.style import Bootstyle
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.constants import *
from pathlib import Path
from util.util import Util


CAMINHO_IMAGEM = Path(__file__).parent / 'img'


class Louise_v0_05(ttk.Frame):

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=YES)
        self.util = Util()
        self.master.geometry("{}x{}+{}+{}".format(self.util.larguraTela,self.util.alturaTela,0,0))
        self.master.title("Louise - Teste de Hipótese - Versão "+str(self.util.versao_0_5))
        self.master.iconbitmap(CAMINHO_IMAGEM.__str__()+"\\lamed.ico")
      
        self.photoimages = []
        imgpath = Path(__file__).parent / 'img'
        for key, val in self.util.arquivo_imagem.items():
            _path = imgpath / val
            self.photoimages.append(ttk.PhotoImage(name=key, file=_path))


        
        

        # buttonbar
        buttonbar = ttk.Frame(self, style='primary.TFrame')
        buttonbar.pack(fill=X, pady=1, side=TOP)

        ## new backup
        _func = lambda: self.showFrameTeste()
        btn = ttk.Button(
            master=buttonbar, text='Testes',
            image='curve', 
            compound=LEFT, 
            command=_func
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=(1, 0), pady=1)

        ## backup
        _func = lambda: self.showSobre()
        btn = ttk.Button(
            master=buttonbar, 
            text='Sobre', 
            image='sobre', 
            compound=LEFT, 
            command=_func
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        ## refresh
        _func = lambda: self.master.destroy()
        btn = ttk.Button(
            master=buttonbar, 
            text='Sair', 
            image='sair',
            compound=LEFT, 
            command=_func
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        

        # painel central
        painelCentral = ttk.Frame(self, padding=(1, 1),bootstyle="light")
        painelCentral.pack(side=TOP, fill=BOTH, expand=YES)


        
        textoSelecioneTeste = "Selecione o teste"
        self.frameSelecioneTeste = ttk.Labelframe(painelCentral, text=textoSelecioneTeste,bootstyle="dark")

        self.frameTestesNormalidadeHipoteses = ttk.Frame(self.frameSelecioneTeste,bootstyle="light")
        self.frameTestesNormalidadeHipoteses.pack(fill=BOTH, expand=Y, anchor=N)


        self.labelNormalidade = ttk.Label(self.frameTestesNormalidadeHipoteses, text="Testes de Normalidade:",width=50)
        self.labelNormalidade.place(x=30,y=30)  


        botaoTesteNormalidade = ttk.Button(
            master=self.frameTestesNormalidadeHipoteses,
            text="Normalidade",
            command=lambda : print('normalidade'),
            bootstyle=INFO,
            width=25
        )
        botaoTesteNormalidade.place(x=50,y=80)
        
        
        self.labelHipotese= ttk.Label(self.frameTestesNormalidadeHipoteses, text="Testes de Hipótese:",width=50)
        self.labelHipotese.place(x=30,y=130)

        botaoTesteHipoteseParametrico2Grupos = ttk.Button(
            master=self.frameTestesNormalidadeHipoteses,
            text="Paramétrico 2 Grupos",
            command=lambda : print('Paramétrico 2 Grupos'),
            bootstyle=PRIMARY,
            width=25
        )
        botaoTesteHipoteseParametrico2Grupos.place(x=50,y=180)

        botaoTesteHipoteseNaoParametrico2Grupos = ttk.Button(
            master=self.frameTestesNormalidadeHipoteses,
            text="Não Paramétrico 2 Grupos",
            command=lambda : print('Não Paramétrico 2 Grupos'),
            bootstyle=PRIMARY,
            width=25
        )
        botaoTesteHipoteseNaoParametrico2Grupos.place(x=50,y=230)

        #self.name1 = ttk.StringVar(value="")
        #self.ent1 = ttk.Entry(master=self.frameTestesNormalidadeHipoteses, textvariable=self.name1)
        #self.ent1.pack(side=TOP, padx=5, fill=X, expand=YES)
        
        #cnl_btn = ttk.Button(
        #    master=container,
        #    text="Cancel",
        #    command=self.on_cancel,
        #    bootstyle=DANGER,
        #    width=6,
        #)
        #cnl_btn.pack(side=RIGHT, padx=5)


        #textoTesteNormalidade = "Teste de Normalidade"
        #self.frameTesteNormalidade = ttk.LabelFrame(self.frameTestesNormalidadeHipoteses, text=textoTesteNormalidade, padding=15, bootstyle="dark")
        #self.frameTesteNormalidade.pack(fill=BOTH, expand=YES, anchor=N)

        #textoTesteHipotese = "Teste de Hipótese"
        #self.frameTesteHipotese = ttk.LabelFrame(self.frameTestesNormalidadeHipoteses, text=textoTesteHipotese, padding=15, bootstyle="dark")
        #self.frameTesteHipotese.pack(fill=BOTH, expand=YES, anchor=N)

        #self.frameHipoteses = ttk.Frame(self.frameSelecioneTeste,bootstyle="danger")
       # self.frameHipoteses.pack(fill=BOTH, expand=Y, anchor=N)

        #textoTesteNormalidade = "Teste de Normalidade"
        #self.frameSelecioneTeste = ttk.Labelframe(self.frameSelecioneTeste , text=textoTesteNormalidade, padding=1,bootstyle="dark")
        
        #label2 = Label(self.frameSelecioneTeste, text=textoTesteNormalidade)
        #label2.pack(fill=BOTH, expand=YES, anchor=N)
        #label2.place(x=0, y=35)
        
        self.frameSelecioneTeste.pack_forget()
        #self.frameSelecioneTeste.pack(fill=BOTH, expand=YES, anchor=N)
        

        #self.create_path_row()


    def create_form_entry(self, widget, label, variable):
        """Create a single form entry"""
        #container = ttk.Frame(self)
        container = widget
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def showFrameTeste(self):
         self.frameSelecioneTeste.pack(fill=BOTH, expand=YES, anchor=N)
       
    def showSobre(self):
                mensagem = "Louise tem como objetivo fornecer uma ferramenta livre com suporte à interface gráfica para a realização de teste de hipótese.\n Contato: albertfrancajosuacosta@gmail.com"
                Messagebox.show_info(mensagem, title='Sobre', alert=True, parent=self)
                 #app.eval('tk::PlaceWindow . center')
               

   

if __name__ == '__main__':


    app = ttk.Window()
    Louise_v0_05(app)
   
    app.mainloop()
