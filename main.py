import numpy as np
# Exercicio1
np.random.seed(5)
arr = np.random.randn(10)
arrM = (arr*100)
arrN = np.floor(arrM)
print(arrN)

# Exercicio2eExercicio3
np.random.seed(1)
mtz= np.random.randint(1,51,size=(4, 4))
print(mtz)
m_linhas = np.mean(mtz, axis=1)
m_colunas = np.mean(mtz, axis=0)

print("Média linhas:")
print(m_linhas)

print("Médias das colunas:")
print(m_colunas)

maiorLinha = np.max(m_linhas)
maiorColuna = np.max(m_colunas)

print("Maior média linhas:", maiorLinha)
print("Maior média colunas:",maiorColuna)

#Exercicio 4
valores, contagens = np.unique(mtz,return_counts=True)
matriz = np.column_stack((valores, contagens))

print(matriz)

duas = valores[np.where(contagens == 2)]
print(duas)