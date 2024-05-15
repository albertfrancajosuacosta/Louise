from datetime import datetime
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
        #self.labelNormalidade.pack(side=TOP, padx=5)
        #self.labelNormalidade.place(x=0, y=35)
        self.labelNormalidade.pack(side=LEFT, fill=X, expand=NO, pady=10, padx=5,anchor=N)

        self.name = ttk.StringVar(value="")
        self.ent = ttk.Entry(master=self.frameTestesNormalidadeHipoteses, textvariable=self.name)
        self.ent.pack(side=LEFT, fill=X, expand=NO, pady=10, padx=5,anchor=N)
        #self.ent.place(x=0, y=100)


        self.labelHipotese= ttk.Label(self.frameTestesNormalidadeHipoteses, text="Testes de Hipótese:",width=50)
        self.labelHipotese.pack(side=LEFT, fill="x", expand=NO, pady=100, padx=5,anchor=N)
        #self.labelHipotese.pack(side=TOP, padx=5)

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


    def showFrameTeste(self):
         self.frameSelecioneTeste.pack(fill=BOTH, expand=YES, anchor=N)
       
    def showSobre(self):
                mensagem = "Louise tem como objetivo fornecer uma ferramenta livre com suporte à interface gráfica para a realização de teste de hipótese.\n Contato: albertfrancajosuacosta@gmail.com"
                Messagebox.show_info(mensagem, title='Sobre', alert=True, parent=self)
                 #app.eval('tk::PlaceWindow . center')
               

    def create_path_row(self):
        """Add path row to labelframe"""
        path_row = ttk.Frame(self.option_lf)
        path_row.pack(fill=X, expand=YES)
        path_lbl = ttk.Label(path_row, text="Path", width=8)
        path_lbl.pack(side=LEFT, padx=(15, 0))
        path_ent = ttk.Entry(path_row, textvariable=self.path_var)
        path_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        browse_btn = ttk.Button(
            master=path_row, 
            text="Browse", 
            command=self.on_browse, 
            width=8
        )
        browse_btn.pack(side=LEFT, padx=5)

if __name__ == '__main__':


    app = ttk.Window()
    Louise_v0_05(app)
   
    app.mainloop()
