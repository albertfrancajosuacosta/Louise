from scipy.stats import shapiro, anderson, ttest_ind


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
    
    def testT2grupos(self,dados):

        dados1 = dados.iloc[:,0:1]
        dados2 = dados.iloc[:,1:2]
            

        return ttest_ind(dados1,dados2)