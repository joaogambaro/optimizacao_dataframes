
'''
Obs: as duas funções ja foram usadas no módulo e estão funcionando

'''


import random
import pandas as pd



def cont_lines(filename):
    '''conta o número de linhas em um arquivo

    Input:
    filename: caminho do arquivo
    '''
    n = 0
    for line in open(filename):
        n += 1
    return(n)






def coleta_amostr(tamAm, filename, is_rand_sample=False):
    '''Coleta uma amostra de tamanho 'tamAm' de um arquivo
    sem ter que ler todo o arquivo.

    Inputs:
    tamAm: tamanho da amostra desejada. Pode ser um valor interiro positivo
        ou um número fracionário entre 0 e 1 (sem considerar o 1). Para tamAm inteiro o tamanho
        da amostra é o número fornecido.Para 0<tamAm<1 o tamanho da amostra
        é uma fração da numero de linhsa totais no arquivo
    filename: caminho do arquivo
    is_rand_sample: quando True as linhas coletadas são selecionadas
        aleatóriamente nos arquivos. Qando False são selecioandas as primeiras
        linhas.

    IMPORTANTE: o método para gerar uma amostra pela escolha
    aleatória de linhas falha quando no arquivo existem linhas
    vazias. Isto acontece pois o método "cont_lines" retorna um
    valor errado e assim a amostra gerada no final não tem o número
    de elemento desejado. Nestes casos é melhor usar is_rand_sample=False.
    '''

    # num. de linhas no arquivo
    n=cont_lines(filename)

    # quando o número é float(tamAm é uma porcentagem das linhas totais)
    if tamAm-int(tamAm)!=0:
        tamAm = int(tamAm*n)


    # os dados são esolhidos aleatóriamente no arquivo
    if is_rand_sample:

        # linhas do arquivo para nao carregar
        l= range(1,n) #1*
        lista_skip = random.sample(l,n-tamAm-1)

        return(pd.read_csv(filename,
                       low_memory=False,
                       skiprows=lista_skip) #2*
          )
        #1* o range deve ir de 1 até n. A função range inclui o limite
        #   inferior e exclui o limite superior, mas não é preciso
        #   considerar n+1, pq para a contagem de linha a primeira
        #   linha e a 1 (e não a 0)
        #2* 'skiprows' é a lista com linhas que devem ser descosideradas
        #    A numeração para desconsiderar a linhas começa em 0(linha
        #    com nomes das colunas) e vai até n-1 (onde n é o numero
        #    total de linhas no arquivo)

    # os dados escolhidos são as n primeiras linhas do arquivo
    else:
        return(pd.read_csv(filename,
                       low_memory=False,
                       nrows=tamAm)
          )
