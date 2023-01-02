
'''
Obs: as duas funções ja foram usadas no módulo e estão funcionando

'''


import random
import pandas as pd



def cont_lines(filename):
    '''conta o número delinhas em um arquivo'''
    n = 0
    for line in open(filename):
        n += 1
    return(n)






def coleta_amostr(tamAm, filename):
    '''Coleta uma amostra de tamanho 'tamAm' de um arquivo
    sem ter que ler todo o arquivo
    '''
    n=cont_lines(filename)
    
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
