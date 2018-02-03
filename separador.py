from openpyxl import workbook
from openpyxl import load_workbook

def abrirPlanilha(nomeArquivo):
    planilha = load_workbook(nomeArquivo)
    planilha = planilha.active()
    return tuple(planilha.rows)

def separarLinhas(matrizPlanilha, colunaVer):
    categorias = []
    competidores = []
    for linha in matrizPlanilha:
        if not linha[colunaVer] in categorias:
            categorias.append(linha[colunaVer])
            competidores.append([])
        competidores[categorias.index(linha[colunaVer])].append(linha)
    for categoria in competidores:
        planilhaNova = workbook.Workbook()
        planilhaNovaAtiva = planilhaNova.active()
        for competidor in competidores:
            planilhaNovaAtiva.append(competidor)
        nomeArq = categorias[competidores.index(categoria)] + ".xlsx"
        print(nomeArq+"criado!")
        planilhaNova.save(nomeArq)