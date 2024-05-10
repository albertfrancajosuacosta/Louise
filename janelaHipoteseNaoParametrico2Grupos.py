from tkinter.messagebox import showerror, showwarning
from tkinter.ttk import Combobox, Treeview
import traceback
from tkinter import ttk
from util import Util
from tkinter import VERTICAL, W, Button, Frame, Label, Scrollbar, StringVar, Toplevel, filedialog
import pandas as pd
from testesEstatisticos import TesteEstatistico
from textoFormatado import TextoFormatado



class JanelaHipoteseNaoParametrico2Grupos(Toplevel):


    def __init__(self, larguraMae, alturaMae, master = None):

        super().__init__(master = master)
        
        self.util = Util()
        self.definirConfiguracoes(larguraMae, alturaMae,rezisableLargura=True,rezisableAltura=True)

        


    def definirConfiguracoes(self, larguraMae, alturaMae,rezisableLargura=True,rezisableAltura=True):
        self.largura = larguraMae
        self.altura = alturaMae
        self.title("Louise - Teste de Hipótese Não Paramétrico para 2 Grupos - Versão "+str(self.util.versao))
        self.iconbitmap('C:\\Users\\alber\\Documents\\LabMax\\Louise\\img\\lamed.ico')
        self.resizable(width=rezisableLargura, height=rezisableAltura)
        self.planilha = None
        self.qtdLinhasPlanilha = None
        self.qtdColunasPlanilha = None
        self.configure(background=self.util.corFundoTela)
        self.x, self.y = self.util.posicaoJanelaCentralizada(self,self.largura,self.altura)
        self.geometry("{}x{}+{}+{}".format(self.util.larguraTela,self.util.alturaTela,self.x,self.y))
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1,weight=1)

        

        #Frame Superior
        self.frameSuperior = Frame(self, 
                                height=int(0.90*self.altura),
                                highlightbackground=self.util.corBorda,
                                highlightthickness=2
                            )
                                

        self.frameSuperior.configure(background=self.util.corFundoTela)
        
        self.labelSelecioneArquivo = Label(self.frameSuperior, 
                             text ="Selecione o arquivo", 
                             font=('Arial',16,'bold')
        )
        self.labelSelecioneArquivo.grid(row=0,
                                        column=0,
                                        sticky='w',
                                        padx=10
                                        )
        self.labelSelecioneArquivo.config(bg=self.util.corFundoTela, fg=self.util.corLetra)

     
        self.labelCaminhoArquivo = Label(self.frameSuperior,
                               font=('Arial',10),
                               width=50,
                              # bg="#d5f0ed"
                            ) 
        
        self.labelCaminhoArquivo.grid(row=0,
                                      column=1,
                                      #sticky='n',
                                      padx=10
                                      )

        self.botaoArquivo = Button(self.frameSuperior,
                                    text="Procurar",
                                    command=lambda: self.procurarArquivo()
                                    )
        
        self.botaoArquivo.grid(row=0,
                               column=2,
                               sticky='nw',
                               padx=10
                               )
        
        self.frameSuperior.grid(row=0, sticky="nenw")

        #Frame Central

        self.frameCentral = Frame(self, 
                                height=self.util.alturaTela,
                                width=self.util.larguraTela,
                                highlightbackground=self.util.corBorda,
                                highlightthickness=2
                            )

        self.frameCentral.configure(background=self.util.corFundoTela)

        self.frameCentral.columnconfigure(0, weight=1)
        self.frameCentral.columnconfigure(1, weight=1)
        self.frameCentral.rowconfigure(0,weight=1)


        #Frame Central Esquerdo

        self.frameCentralE = Frame(self.frameCentral, 
                                height=self.util.alturaTela,
                                width=self.util.larguraTela//2,
                                highlightbackground=self.util.corBorda,
                                highlightthickness=2
                            )
        self.frameCentralE.configure(background=self.util.corFundoTela)
        
        self.frameCentralE.grid(row=0,
                                column=0,
                                sticky="nenwswse")
        
        self.frameCentralE.columnconfigure(0, weight=1)
        self.frameCentralE.rowconfigure(0,weight=1)
        

        self.scrollbary = Scrollbar(self.frameCentralE, orient=VERTICAL)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        #self.style.configure("Treeview",
        #                     background="#black",
        #                     foreground="black",
        #                    rowheight=25,
        #                     fieldbackground="silver"
        #                    )
        
        self.style.configure("Treeview.Heading",
                             background=self.util.corFundoTela,
                             foreground=self.util.corLetra,
                             fieldbackground="red",
                             #rowheight=25,
                             relief="flat"
                             )
        
        
        self.arvore = Treeview(self.frameCentralE,yscrollcommand=self.scrollbary.set,columns=("1","2","3","4"))
        self.arvore['show'] = 'headings'
        self.arvore.column("1", minwidth=10, width=10,  anchor=W)
        self.arvore.column("2", minwidth=10, width=10, anchor=W)
        self.arvore.column("3", minwidth=10, width=10,  anchor=W)
        self.arvore.column("4", minwidth=10, width=10, anchor=W)
        self.arvore.heading("1", text="#")
        self.arvore.heading("2", text="Valor Grupo 1")
        self.arvore.heading("3", text="#")
        self.arvore.heading("4", text="Valor Grupo 2")

        
        self.arvore.grid(row=0,
                        column=0,
                        sticky='NSEW'            
        )
        
      
        self.scrollbary.config(command=self.arvore.yview)
       
        self.scrollbary.grid(row=0,column=1,sticky='NSEW')

        
        #Frame Central Direito
        self.frameCentralD = Frame(self.frameCentral, 
                                height=self.util.alturaTela,
                                width=self.util.larguraTela//2,
                                highlightbackground=self.util.corBorda,
                                highlightthickness=2
                            )
        self.frameCentralD.configure(background=self.util.corFundoTela)

        
        self.frameCentralD.grid(row=0,
                                column=1,
                                sticky="nenwswse")
        
        self.labelSelecioneTeste = Label(self.frameCentralD, 
                                       text ="Selecione o teste", 
                                       font=('Arial',16,'bold') 
                                    )
        self.labelSelecioneTeste.config(bg=self.util.corFundoTela, fg=self.util.corLetra)

        self.labelSelecioneTeste.grid(row=0,
                                    column=0,
                                    sticky='ns'
                                    )
        

        self.tipoTesteNormalidadeEscolhido = StringVar()

        self.comboBoxTipoTesteNormalidade = Combobox(self.frameCentralD, 
                                            textvariable=self.tipoTesteNormalidadeEscolhido
                                            #width=(self.largura//2)
                                       )
        
        self.frameCentralD.columnconfigure(1,weight=1)
        
        
        # Adding combobox drop down list 
        listaTestes  = ['Mann-Whitney', 'Wilcoxon']
        self.comboBoxTipoTesteNormalidade['values'] = listaTestes
        self.comboBoxTipoTesteNormalidade['state']= 'readonly'
        self.comboBoxTipoTesteNormalidade.grid(row = 0, column = 1,sticky='NSEW',padx=10) 
        

        self.botaoTestar = Button(self.frameCentralD, 
                   text="Testar", 
                   command= lambda: self.testar(),
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=('Arial',16,'bold'),
                   height=0,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   wraplength=80
            )
        
        
        self.botaoTestar.grid(row=1,column=0, columnspan=2,  sticky="NSEW")


        self.textoResultado = TextoFormatado(self.frameCentralD)

        self.textoResultado.limpar()
        
        self.frameCentralD.rowconfigure(2,weight=1)
        self.textoResultado.grid(row=2,column=0,sticky="NSEW", columnspan=3)


        self.frameCentral.grid(row=1,sticky="nenwswse") 
            

    def testar(self):
            
        if self.labelCaminhoArquivo.cget("text") == "":
            showwarning(title="Aviso", message="É necessário selecionar o arquivo primeiro.")
            self.botaoArquivo.focus_set()
        elif self.tipoTesteNormalidadeEscolhido.get() == "":
            showwarning(title="Aviso", message="É necessário selecionar o teste primeiro.")
            self.comboBoxTipoTesteNormalidade.focus_set()
        elif self.tipoTesteNormalidadeEscolhido.get() == "Mann-Whitney":
            self.testeMannWhitney2grupos()
        elif self.tipoTesteNormalidadeEscolhido.get() == "Wilcoxon":
            self.testeWilcoxon2grupos()

            
        
    def testeWilcoxon2grupos(self):
        self.textoResultado.limpar()
        te = TesteEstatistico(signi=0.05)
        estatistica, p_value = te.wilcoxon2grupos(self.planilha)
        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "Resultado - "+self.tipoTesteNormalidadeEscolhido.get()+" Nível de Significância "+str(te.nivelSignificancia)+"\n", "h1")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "Hipóteses: \n", "bold")
        self.textoResultado.insert_bullet("end", "H0: Não há diferença significativa \n")
        self.textoResultado.insert_bullet("end", "H1: Há diferença significativa \n")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "Estatística do teste\n", "bold")
        self.textoResultado.insert("end", str(estatistica[0])+"\n")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "p-valor\n", "bold")
        self.textoResultado.insert("end", str(p_value[0])+"\n")
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


    def testeMannWhitney2grupos(self):
        
        self.textoResultado.limpar()
        te = TesteEstatistico(signi=0.05)
        estatistica, p_value = te.mannWhitney2grupos(self.planilha)
        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "Resultado - "+self.tipoTesteNormalidadeEscolhido.get()+" Nível de Significância "+str(te.nivelSignificancia)+"\n", "h1")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "Hipóteses: \n", "bold")
        self.textoResultado.insert_bullet("end", "H0: Não há diferença significativa \n")
        self.textoResultado.insert_bullet("end", "H1: Há diferença significativa \n")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "Estatística do teste\n", "bold")
        self.textoResultado.insert("end", str(estatistica[0])+"\n")
        self.textoResultado.habitarDesabilitar("disabled")

        self.textoResultado.habitarDesabilitar("normal")
        self.textoResultado.insert("end", "p-valor\n", "bold")
        self.textoResultado.insert("end", str(p_value[0])+"\n")
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

    
                 
    def procurarArquivo(self):

        self.focus_set()


        caminhoArquivo = filedialog.askopenfilename(title="Selecione o arquivo", filetypes=[("Excel files", "*.xlsx")])
           
        if caminhoArquivo:
            self.labelCaminhoArquivo.config(text=caminhoArquivo)
            self.processarArquivo(caminhoArquivo)


    def processarArquivo(self,caminho):

        try:
            self.planilha = pd.read_excel(caminho,index_col=None)
            self.qtdLinhasPlanilha, self.qtdColunasPlanilha = self.planilha.shape

            
            if self.qtdColunasPlanilha != 2:
                showwarning(title="Aviso", message="Os dados precisam estar em uma única coluna. Atualmente os dados estão em "+str(self.qtdColunasPlanilha)+' colunas.') 
            else: 
                
                self.carregarDados(self.planilha)
                self.focus_set()
              


        except Exception as e:

            showerror(title='Error', message='Erro ao abrir arquivo.')
            print(traceback.format_exc())


    def carregarDados(self,planilha):

        for i in self.arvore.get_children():
            self.arvore.delete(i)


        for index, row in (planilha.sort_index(ascending=False)).iterrows():
           
            self.arvore.insert(parent='', index=0, values = ((index+1), row.values[0], (index+1), row.values[1]))


     
     