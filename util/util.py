

class Util:
     
    def __init__(self):
         super().__init__()

         self.larguraTela = 1000
         self.alturaTela = 900
         self.corFundoTela = "#1e3743"
         self.corLetra = "#ffffff"
         self.corBorda = "#b4cffa"
         self.corFundoResultado = "#D9DDDC"
         self.versao_0_1 = 0.1
         self.versao_0_5 = 0.5


   
         
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
        