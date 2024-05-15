from datetime import datetime
from random import choices
import ttkbootstrap as ttk
from ttkbootstrap.style import Bootstyle
from ttkbootstrap.dialogs import Messagebox,MessageDialog
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

        #self.

        image_files = {
            'properties-dark': 'icons8_settings_24px.png',
            'properties-light': 'icons8_settings_24px_2.png',
            'add-to-backup-dark': 'icons8_add_folder_24px.png',
            'add-to-backup-light': 'icons8_add_book_24px.png',
            'stop-backup-dark': 'icons8_cancel_24px.png',
            'stop-backup-light': 'icons8_cancel_24px_1.png',
            'play': 'icons8_play_24px_1.png',
            'refresh': 'icons8_refresh_24px_1.png',
            'stop-dark': 'icons8_stop_24px.png',
            'stop-light': 'icons8_stop_24px_1.png',
            'opened-folder': 'icons8_opened_folder_24px.png',
            'logo': 'backup.png',
            'curve': 'curve_24px.png',
            'sair': 'exit_24px.png',
            'sobre': 'sobre_24px.png'
        }

    
        

        self.photoimages = []
        imgpath = Path(__file__).parent / 'img'
        for key, val in image_files.items():
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
