from datetime import datetime
from random import choices
from tkinter import StringVar, Toplevel
from tkinter import filedialog
import tkinter
import traceback
import ttkbootstrap as ttk
from ttkbootstrap.style import Bootstyle
from tkinter.filedialog import askdirectory
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.constants import *
from tkinter.scrolledtext import ScrolledText
from pathlib import Path
from util.testesEstatisticos import TesteEstatistico
from util.textoFormatado import TextoFormatado
from util.util import Util
import pandas as pd


CAMINHO_IMAGEM = Path(__file__).parent.parent / 'img'


class JanelaNormalidade_v0_5(Toplevel):

    def __init__(self, *args, **kwargs):
       
        super().__init__(*args, **kwargs)
        

        self.arquivoCarregado = False

        self.enderecoArquivoSelecionado = StringVar()

        self.tipoTesteNormalidadeEscolhido = StringVar()
      
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
            'salvar': 'save_24px.png'
        }

    
        self.util = Util()

        self.photoimages = []

        imgpath = Path(__file__).parent.parent / 'img'
        for key, val in image_files.items():
            _path = imgpath / val
            self.photoimages.append(ttk.PhotoImage(name=key, file=_path))

        
        # left panel
        painelEsquerdo = ttk.Frame(self, style='bg.TFrame')
        painelEsquerdo.pack(side=LEFT, fill=Y)

        ## Collapsible arquivo  (collapsible)
        collapsibleArquivo = CollapsingFrame(painelEsquerdo)
        collapsibleArquivo.pack(fill=X, pady=1)

        ## container
        bus_frm = ttk.Frame(collapsibleArquivo, padding=5)
        bus_frm.columnconfigure(1, weight=1)
        collapsibleArquivo.add(
            child=bus_frm, 
            title='Arquivo Selecionado', 
            bootstyle=SECONDARY)

        ## Endereço
  
        self.labelEnderecoArquivo = ttk.Label(bus_frm, text='Endereço:')
        self.labelEnderecoArquivo.grid(row=0, column=0, sticky=W, pady=2)
        self.enderecoArquivo = ttk.Label(bus_frm)
        self.enderecoArquivo.grid(row=0, column=1, sticky=EW, padx=5, pady=2)
       

        ## Tamnho Grupo
        lbl = ttk.Label(bus_frm, text='Tamanho Grupo:')
        lbl.grid(row=1, column=0, sticky=W, pady=2)
        lbl = ttk.Label(bus_frm, textvariable='tamahoGrupo')
        lbl.grid(row=1, column=1, sticky=EW, padx=5, pady=2)
        #self.setvar('lastrun', '14.06.2021 19:34:43')



        # Collapsible teste (collapsible)
        collapsibleTeste = CollapsingFrame(painelEsquerdo)
        collapsibleTeste.pack(fill=BOTH, pady=1)

       
        ## container
        busTeste = ttk.Frame(collapsibleTeste, padding=5)
        busTeste.columnconfigure(1, weight=1)
        collapsibleTeste.add(
            child=busTeste, 
            title='Teste', 
            bootstyle=SECONDARY)
        
        ## Teste
        self.labelTesteNormalidade = ttk.Label(busTeste, text='Teste:')
        self.labelTesteNormalidade.grid(row=0, column=0, sticky=W, pady=2)

    

        self.comboBoxTipoTesteNormalidade = ttk.Combobox(busTeste, 
                                            textvariable=self.tipoTesteNormalidadeEscolhido
                                            #width=(self.largura//2)
                                       )
            
        self.comboBoxTipoTesteNormalidade['values'] = ('Shapiro-Wilk', 'Anderson') 
        self.comboBoxTipoTesteNormalidade['state']= 'readonly'
        self.comboBoxTipoTesteNormalidade.grid(row=1, column=0, sticky=W, pady=2)


        ## Nível de significância
        self.labelTesteNormalidade = ttk.Label(busTeste, text='Nível de Significância:')
        self.labelTesteNormalidade.grid(row=2, column=0, sticky=W, pady=2)

        self.nivelSignificanciaeEscolhido = StringVar()

        self.comboBoxNivelSignificancia = ttk.Combobox(busTeste, 
                                            textvariable=self.nivelSignificanciaeEscolhido
                                            #width=(self.largura//2)
                                       )

        # Adding combobox drop down list 
        self.comboBoxNivelSignificancia['values'] = ('1%', '2.5%','5%', '10%', '15%') 
        self.comboBoxNivelSignificancia['state']= 'readonly'
        self.comboBoxNivelSignificancia.current(2)
        self.comboBoxNivelSignificancia.grid(row=3, column=0, sticky=W, pady=2)   


        self.botaoTestar = ttk.Button(busTeste,
                   text="Testar", 
                   command= lambda: self.testar(),
                   bootstyle="success"                  
            )
        
        self.botaoTestar.grid(row=5, column=0, pady=2)


        # Collapsible opções resultados (collapsible)
        collapsibleOpcoesResultados = CollapsingFrame(painelEsquerdo)
        collapsibleOpcoesResultados.pack(fill=BOTH, pady=1)

       
        ## container
        busOpcoesResultados = ttk.Frame(collapsibleOpcoesResultados, padding=5)
        busOpcoesResultados.columnconfigure(1, weight=1)
        collapsibleOpcoesResultados.add(
            child=busOpcoesResultados, 
            title='Opções Resultado', 
            bootstyle=SECONDARY)
        
             

        self.botaoSalvarResultado = ttk.Button(busOpcoesResultados,
                   text="Salvar", 
                   command= lambda: self.salvarResultado(),
                   bootstyle="success",
                   image='salvar', 
                   compound=LEFT, 
                              
        )
        self.botaoSalvarResultado.pack_forget()
        #self.botaoSalvarResultado.grid(row=0, column=0, pady=2)

      
      
        ## section separator
        sep = ttk.Separator(bus_frm, bootstyle=SECONDARY)
        sep.grid(row=3, column=0, columnspan=2, pady=10, sticky=EW)

        # logo
        #lbl = ttk.Label(left_panel, image='logo', style='bg.TLabel')
        #lbl.pack(side='bottom')

        # Painel Direito
        painelDireito = ttk.Frame(self, padding=(2, 1))
        painelDireito.pack(side=RIGHT, fill=BOTH, expand=YES)

        ## file input
        browse_frm = ttk.Frame(painelDireito)
        browse_frm.pack(side=TOP, fill=X, padx=2, pady=1)

        self.file_entry = ttk.Entry(browse_frm)
        self.file_entry.config(state=DISABLED)
        self.file_entry.pack(side=LEFT, fill=X, expand=YES)

        self.botaoProcurarArquivo = ttk.Button(
            master=browse_frm, 
            image='opened-folder', 
            bootstyle=(LINK, SECONDARY),
            command=lambda: self.procurarArquivo()
        )
        self.botaoProcurarArquivo.pack(side=RIGHT)

      

        ## scrolling text output
        collapsibleArquivoAberto = CollapsingFrame(painelDireito)
        collapsibleArquivoAberto.pack(fill=BOTH, expand=YES)

        output_container = ttk.Frame(collapsibleArquivoAberto, padding=1)
       
        self.st = ScrolledText(output_container)
        self.st.pack(fill=BOTH, expand=YES)
        collapsibleArquivoAberto.add(output_container, textvariable='scroll-message')

        self.textoResultado = TextoFormatado(painelDireito)
        self.textoResultado.pack(fill=BOTH, expand=YES)

        
    def salvarResultado(self):
       
        caminho = self.util.salvarResultadosInTxt(self.textoResultado.get(1.0,"end-1c"))
        Messagebox.show_info(title="Arquivo salvo em: ", message=caminho)


    def testar(self):
        
        self.sig = self.util.converteNivelSignificancia(self.nivelSignificanciaeEscolhido.get(),self.tipoTesteNormalidadeEscolhido.get())
      
        self.textoResultado.limpar()

       

        if not isinstance(self.enderecoArquivoSelecionado,str):
             if self.enderecoArquivoSelecionado.get() == "":
                Messagebox.show_warning(title="Aviso", message="É necessário selecionar o arquivo primeiro.")
                self.botaoProcurarArquivo.focus_set()
        else:
            if self.tipoTesteNormalidadeEscolhido.get() == "":
                Messagebox.show_warning(title="Aviso", message="É necessário selecionar o teste primeiro.")
                self.comboBoxTipoTesteNormalidade.focus_set()
            elif self.tipoTesteNormalidadeEscolhido.get() == "Shapiro-Wilk":
                self.shapiroWilk()
            elif self.tipoTesteNormalidadeEscolhido.get() == "Anderson":
                self.anderson()
                
        self.botaoSalvarResultado.grid(row=0, column=0, pady=2)


    def procurarArquivo(self):
       
        caminhoArquivo = filedialog.askopenfilename(title="Selecione o arquivo", filetypes=[("Excel files", "*.xlsx")])
        self.enderecoArquivoSelecionado = caminhoArquivo
        self.setvar('scroll-message', self.enderecoArquivoSelecionado.split("/")[-1])
        
        if caminhoArquivo:
            self.enderecoArquivo.config(text=self.enderecoArquivoSelecionado)
          
            self.file_entry.config(state=NORMAL)
            self.file_entry.insert(END, self.enderecoArquivoSelecionado)
            self.file_entry.config(state=DISABLED)
            self.processarArquivo(caminhoArquivo)

        self.focus_set()

    def processarArquivo(self,caminho):

        try:
            self.planilha = pd.read_excel(caminho,index_col=None)
            self.setvar('tamahoGrupo', self.util.metaDadosPlanilha(self.planilha)[0])
            self.qtdLinhasPlanilha, self.qtdColunasPlanilha = self.planilha.shape

            if self.qtdColunasPlanilha != 1:
                Messagebox.show_error(title="Erro", message="Os dados precisam estar em uma única coluna. Atualmente os dados estão em "+str(self.qtdColunasPlanilha)+' colunas.') 
            else: 
                
                self.carregarDados(self.planilha)
                self.focus_set()
            
        except Exception as e:

            Messagebox.show_error(title='Error', message='Erro ao abrir arquivo.')
            print(traceback.format_exc())


    def carregarDados(self,planilha):
        
        self.st.delete('1.0', END)
        self.st.configure(font='TkFixedFont')
        self.st.insert(END, '#\t\t\tValor\n')
        for index, row in planilha.iterrows():
           
            _texto = str(index+1)+'\t\t'+str(row.values[0])+'\n'
            self.st.insert(END, _texto)

        self.st.tag_add("start", "1.0","2.0")
        self.st.tag_configure("start", background="#2780e3", foreground="#FFFFFF")
        self.st.config(state= DISABLED)
        

    def shapiroWilk(self):
        self.textoResultado.limpar()
        te = TesteEstatistico(signi=self.sig)
        estatistica, p_value =  te.shaporiWilk(self.planilha)
        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "Resultado - "+self.tipoTesteNormalidadeEscolhido.get()+" Nível de Significância "+str(te.nivelSignificancia)+"\n", "h1")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "Hipóteses: \n", "bold")
        self.textoResultado.insert_bullet("end", "H0: Normalmente distribuído \n")
        self.textoResultado.insert_bullet("end", "H1: Não normalmente distribuído \n")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "Estatística do teste\n", "bold")
        self.textoResultado.insert("end", str(estatistica)+"\n")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "p-valor\n", "bold")
        self.textoResultado.insert("end", str(p_value)+"\n")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "\n\n")
        self.textoResultado.habitarDesabilitar("disabled")

        if(p_value<te.nivelSignificancia):
            self.textoResultado.habitarDesabilitar("normal")
            self.textoResultado.insert("end", "Reijeita H0 \n","bold")
            self.textoResultado.habitarDesabilitar("disabled")
        else:
            self.textoResultado.habitarDesabilitar("normal")
            self.textoResultado.insert("end", "Falha em rejeitar H0 \n","bold")
            self.textoResultado.habitarDesabilitar("disabled")
    

    def anderson(self):
        self.textoResultado.limpar()
        te = TesteEstatistico(signi=self.sig)
        [est, criticoValor, significanciaNivel] =  te.anderson(self.planilha,teste='norm')
        
        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "Resultado - "+self.tipoTesteNormalidadeEscolhido.get()+" Nível de Significância "+str(te.nivelSignificancia)+"\n", "h1")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "Hipóteses: \n", "bold")
        self.textoResultado.insert_bullet("end", "H0: Normalmente distribuído \n")
        self.textoResultado.insert_bullet("end", "H1: Não normalmente distribuído \n")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "Estatística do teste\n", "bold")
        self.textoResultado.insert("end", str(est)+"\n")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "Valor Crítico\n", "bold")
        self.textoResultado.insert("end", str(criticoValor)+"\n")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "Nível de Significância\n", "bold")
        self.textoResultado.insert("end", str(significanciaNivel)+"\n")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "\n\n")
        self.textoResultado.habitarDesabilitar("disabled")

        if(criticoValor<est):
            self.textoResultado.habitarDesabilitar("normal")
            self.textoResultado.insert("end", "Reijeita H0 \n","bold")
            self.textoResultado.habitarDesabilitar("disabled")
        else:
            self.textoResultado.habitarDesabilitar("normal")
            self.textoResultado.insert("end", "Falha em rejeitar H0 \n","bold")
            self.textoResultado.habitarDesabilitar("disabled")

class CollapsingFrame(ttk.Frame):
    """A collapsible frame widget that opens and closes with a click."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0, weight=1)
        self.cumulative_rows = 0

        # widget images
        self.images = [
            ttk.PhotoImage(file=CAMINHO_IMAGEM/'icons8_double_up_24px.png'),
            ttk.PhotoImage(file=CAMINHO_IMAGEM/'icons8_double_right_24px.png')
        ]

    def add(self, child, title="", bootstyle=PRIMARY, **kwargs):
        """Add a child to the collapsible frame

        Parameters:

            child (Frame):
                The child frame to add to the widget.

            title (str):
                The title appearing on the collapsible section header.

            bootstyle (str):
                The style to apply to the collapsible section header.

            **kwargs (Dict):
                Other optional keyword arguments.
        """
        if child.winfo_class() != 'TFrame':
            return

        style_color = Bootstyle.ttkstyle_widget_color(bootstyle)
        frm = ttk.Frame(self, bootstyle=style_color)
        frm.grid(row=self.cumulative_rows, column=0, sticky=EW)

        # header title
        header = ttk.Label(
            master=frm,
            text=title,
            bootstyle=(style_color, INVERSE)
        )
        if kwargs.get('textvariable'):
            header.configure(textvariable=kwargs.get('textvariable'))
        header.pack(side=LEFT, fill=BOTH, padx=10)

        # header toggle button
        def _func(c=child): return self._toggle_open_close(c)
        btn = ttk.Button(
            master=frm,
            image=self.images[0],
            bootstyle=style_color,
            command=_func
        )
        btn.pack(side=RIGHT)

        # assign toggle button to child so that it can be toggled
        child.btn = btn
        child.grid(row=self.cumulative_rows + 1, column=0, sticky=NSEW)

        # increment the row assignment
        self.cumulative_rows += 2

    def _toggle_open_close(self, child):
        """Open or close the section and change the toggle button 
        image accordingly.

        Parameters:

            child (Frame):
                The child element to add or remove from grid manager.
        """
        if child.winfo_viewable():
            child.grid_remove()
            child.btn.configure(image=self.images[1])
        else:
            child.grid()
            child.btn.configure(image=self.images[0])
