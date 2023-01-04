
'''
Funções que ja foram usadas em módulo:

--uso_memoria
--porc_reducao
--resultados_em_df


'''

import pandas as pd



def uso_memoria(df):
    
    '''retona a mémória ocupada por em dataframe em 
    magabites(Mb)'''
    
    # memória usada em bytes
    men_uso_b = df.memory_usage(deep=True).sum()

    # converte bytes para megabites
    mem_uso_mb = men_uso_b / 1024 ** 2 

    return(mem_uso_mb)



def resultados_em_df(df_original, df_convertido):
    
    '''Organiza os subtipos de uma df antes e depois 
    do processo de optimização em um dataframe. O dataframe
    contém duas colunas uma com os tipos das variáveis antes 
    do processo e outra com os tipos das variáveis depois do
    do processo'''

    #Ordena as colunas dos dataframes
    df_original=df_original[df_convertido.columns]
    
    # index: df original
    l_ori_index=list(df_original.dtypes.index)
    l_ori_index.append("uso_mem_MB")

    # tipos: df original
    l_orig_tipos=list(df_original.dtypes.values)
    l_orig_tipos.append(uso_memoria(df_original))

    # tipos: df alterado
    l_mud_tipos=list(df_convertido.dtypes.values)
    l_mud_tipos.append(uso_memoria(df_convertido))


    df=pd.DataFrame({'sem_mud':l_orig_tipos, 'com_mud':l_mud_tipos}, index=l_ori_index)
    
    #l=[l_ori_index, l_orig_tipos, l_mud_tipos]
    #return(l)

    return(df)




def porc_reducao(df_original, df_convertido):
    '''
    calcula a porcentagem de redução doconcumo de memória 
    devido a optiização do dataframe
    '''

    # uso de memória
    mem_original = uso_memoria(df_original)
    mem_convertido = uso_memoria(df_convertido)

    # porcentagem na redução
    return(1- mem_convertido/mem_original)

    







