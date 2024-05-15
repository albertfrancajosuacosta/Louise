from datetime import datetime
from random import choices
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
        _func = lambda: Messagebox.ok(message='Adding new backup')
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
        painelCentral.pack(side=RIGHT, fill=BOTH, expand=YES)
       
       
    def showSobre(self):
                mensagem = "Louise tem como objetivo fornecer uma ferramenta livre com suporte à interface gráfica para a realização de teste de hipótese.\n Contato: albertfrancajosuacosta@gmail.com"
                Messagebox.show_info(mensagem, title='Sobre', alert=True, parent=self)
               
               
if __name__ == '__main__':


    app = ttk.Window()
    Louise_v0_05(app)
    app.mainloop()
