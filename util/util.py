from datetime import datetime
from pathlib import Path


class Util:
     
    def __init__(self):
         super().__init__()

         self.larguraTela = 1000
         self.alturaTela = 900
         self.corFundoTela = "#1e3743"
         self.corLetra = "#ffffff"
         self.corBorda = "#b4cffa"
         self.corFundoResultado = "#D9DDDC"
         self.versao_0_1 = '0.1'
         self.versao_0_5 = '0.5'
         self.versao_1_0 = '1.0'
         self.versao_1_0_1 = '1.0.1'

         self.CAMINHO_IMAGEM = Path(__file__).parent.parent / 'img'

         self.arquivo_imagem = {
            
            'opened-folder': 'icons8_opened_folder_24px.png',
            'curve': 'curve_24px.png',
            'sair': 'exit_24px.png',
            'sobre': 'sobre_24px.png',
            'salvar': 'save_24px.png'
         }

         #self.fotoimagens = []
         #imgpath = Path(__file__).parent / 'img'
         #for key, val in self.arquivo_imagem.items():
         #   _path = imgpath / val
         #   self.fotoimagens.append(ttk.PhotoImage(name=key, file=_path))



    def formatarCabecalho2MaisGrupos(self, qtdGrupos):
        cabecalho = ""
        for c in range(1, qtdGrupos + 1):
            cabecalho += '#\t\tGrupo ' + str(c) + '\t\t'
        cabecalho += '\n'
        return cabecalho

    def formatarLinha2MaisGrupos(self, qtdGrupos, index, row):
        linha = ""
        for c in range(1, qtdGrupos + 1):
            linha += str(index + 1) + '\t' + str(row.values[c-1]) + '\t\t\t'
        linha += '\n'
        return linha

    def salvarResultadosInTxt(self,resultados):
        dataHoraString = str(datetime.now())
        dataHoraString = dataHoraString.replace(':','-').replace('.','-')
        caminho = (Path(__file__).parent.parent.__str__()+"\\Resultado "+dataHoraString+".txt")
        f = open(caminho,"w")
        f.write(resultados)
        f.close()
        return caminho

    def metaDadosPlanilha(self, planilha):
        linha, coluna = planilha.shape
        return linha, coluna 
    
    def metaDadosPlanilha2Grupos(self, planilha):
        linha, coluna = planilha.shape
        tamanhoGrupo1 = (planilha[planilha.columns[0]].shape)[0]
        tamanhoGrupo2 = (planilha[planilha.columns[1]].shape)[0] 
        return linha, coluna, tamanhoGrupo1, tamanhoGrupo2
       
   
         
    def tamanhoTelaDispositivo(self, janela,pL=0.80,pA=0.80):
        largura = janela.winfo_screenwidth()
        altura = janela.winfo_screenheight()
        return int(largura*pL),int(altura*pA)
    
    def posicaoJanelaCentralizada(self, janela,largura, altura):
        
        x = (janela.winfo_screenwidth()//2)-(largura//2)
        y = (janela.winfo_screenheight()//2)-(altura//2)
        return x, y
  

    def tamanhoFrame(self, frame):
        frame.update()
        largura = frame.winfo_reqwidth()
        altura = frame.winfo_reqheight()
        return largura, altura
    

    def converteNivelSignificancia(self, valorOriginal,testeSelecionado):
        if(testeSelecionado == 'Anderson'):
            pass
            if valorOriginal == "1%":
                return 1.
            if valorOriginal == "2.5%":
                return 2.5
            if valorOriginal == "5%":
                return 5.
            if valorOriginal == "10%":
                return 10.
            if valorOriginal == "15%":
                return 15.
        else:    
            if valorOriginal == "1%":
                return 0.01
            if valorOriginal == "2.5%":
                return 0.025
            if valorOriginal == "5%":
                return 0.05
            if valorOriginal == "10%":
                return 0.10
            if valorOriginal == "15%":
                return 0.15
        