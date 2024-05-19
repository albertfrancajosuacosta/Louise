from scipy.stats import shapiro, anderson, ttest_ind, mannwhitneyu, wilcoxon, kruskal, friedmanchisquare
import numpy as np



class TesteEstatistico():

    def __init__(self, signi=0.05):

        super().__init__()

        self.nivelSignificancia = signi


    def shaporiWilk(self,dados):
        return shapiro(dados) 
        
    
    def anderson(self,dados, teste):    

        resultados = anderson(dados[dados.columns[0]], dist=teste)
        indexCriticoValor = int(np.where(resultados.significance_level==self.nivelSignificancia)[0])        
        return resultados.statistic, resultados.critical_values[indexCriticoValor], self.nivelSignificancia
    
    def testeT2grupos(self,dados):

        dados1 = dados.iloc[:,0:1]
        dados2 = dados.iloc[:,1:2]
            
        return ttest_ind(dados1,dados2)
    
    def mannWhitney2grupos(self,dados):
        
        dados1 = dados.iloc[:,0:1]
        dados2 = dados.iloc[:,1:2]

        return mannwhitneyu(dados1, dados2)

    def wilcoxon2grupos(self,dados):

        dados1 = dados.iloc[:,0:1]
        dados2 = dados.iloc[:,1:2]

        return wilcoxon(dados1, dados2)


    def friedman(self, dados, qtdGrupos):
        gruposLista = []
        for c in range(0, qtdGrupos):
            _grupo = dados.iloc[:, c:c + 1]
            gruposLista.append(_grupo)

        if qtdGrupos == 3:
            return friedmanchisquare(gruposLista[0], gruposLista[1], gruposLista[2])
        if qtdGrupos == 4:
            return friedmanchisquare(gruposLista[0], gruposLista[1], gruposLista[2], gruposLista[3])
        if qtdGrupos == 5:
            return friedmanchisquare(gruposLista[0], gruposLista[1], gruposLista[2], gruposLista[3], gruposLista[4])
        if qtdGrupos == 6:
            return friedmanchisquare(gruposLista[0], gruposLista[1], gruposLista[2], gruposLista[3], gruposLista[4],
                           gruposLista[5])
        if qtdGrupos == 7:
            return friedmanchisquare(gruposLista[0], gruposLista[1], gruposLista[2], gruposLista[3], gruposLista[4],
                           gruposLista[5], gruposLista[6])
        if qtdGrupos == 8:
            return friedmanchisquare(gruposLista[0], gruposLista[1], gruposLista[2], gruposLista[3], gruposLista[4],
                           gruposLista[5], gruposLista[6], gruposLista[7])
        if qtdGrupos == 9:
            return friedmanchisquare(gruposLista[0], gruposLista[1], gruposLista[2], gruposLista[3], gruposLista[4],
                           gruposLista[5], gruposLista[6], gruposLista[7], gruposLista[8])
        if qtdGrupos == 10:
            return friedmanchisquare(gruposLista[0], gruposLista[1], gruposLista[2], gruposLista[3], gruposLista[4],
                           gruposLista[5], gruposLista[6], gruposLista[7], gruposLista[8], gruposLista[9])

    def kruskalWallis(self,dados, qtdGrupos):
        gruposLista = []
        for c in range(0, qtdGrupos):
            _grupo = dados.iloc[:,c:c+1]
            gruposLista.append(_grupo)

        if qtdGrupos==3:
           return kruskal(gruposLista[0], gruposLista[1], gruposLista[2])
        if qtdGrupos == 4:
            return kruskal(gruposLista[0], gruposLista[1], gruposLista[2], gruposLista[3])
        if qtdGrupos == 5:
            return kruskal(gruposLista[0], gruposLista[1], gruposLista[2],gruposLista[3],gruposLista[4])
        if qtdGrupos == 6:
            return kruskal(gruposLista[0], gruposLista[1], gruposLista[2],gruposLista[3],gruposLista[4],gruposLista[5])
        if qtdGrupos == 7:
            return kruskal(gruposLista[0], gruposLista[1], gruposLista[2],gruposLista[3],gruposLista[4],gruposLista[5],gruposLista[6])
        if qtdGrupos == 8:
            return kruskal(gruposLista[0], gruposLista[1], gruposLista[2],gruposLista[3],gruposLista[4],gruposLista[5],gruposLista[6],gruposLista[7])
        if qtdGrupos == 9:
            return kruskal(gruposLista[0], gruposLista[1], gruposLista[2],gruposLista[3],gruposLista[4],gruposLista[5],gruposLista[6],gruposLista[7],gruposLista[8])
        if qtdGrupos == 10:
            return kruskal(gruposLista[0], gruposLista[1], gruposLista[2],gruposLista[3],gruposLista[4],gruposLista[5],gruposLista[6],gruposLista[7],gruposLista[8],gruposLista[9])
