from scipy.stats import shapiro, anderson


class TesteEstatistico():

    def __init__(self, signi=0.05):

        super().__init__()

        self.nivelSignificancia = signi


    def shaporiWilk(self,dados):
        return shapiro(dados) 
        
    
    def anderson(self,dados, teste):    
          
        resultados = anderson(dados[dados.columns[0]], dist=teste)
        
        est = resultados[0]
        criticoValor = resultados[1][2]
        significanciaNivel  = resultados[2][2]

        return est, criticoValor, significanciaNivel