from separador import *

print("Separador de planilhas")
nomeArq = str(input("Digite o nome do arquivo a ser organizado(com a extensão também):"))
planilha = abrirPlanilha(nomeArq)
nColuna = int(input("Digite o número da coluna que tem a informação que terá o critério de separação:"))
separarLinhas(planilha, nColuna)
print("Sucesso! Ctrl + C para sair")
