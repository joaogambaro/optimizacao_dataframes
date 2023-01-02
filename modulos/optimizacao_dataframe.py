
'''
Métodos testados

transfoma_colunas
muda_tipos
obtem_subtipos
'''



import pandas as pd


#-----------------------------------------
# retornam informações sobre as colunas
#-------------------------------------------

def int_is_signed(col,df):
    '''Identifica se um inteiro e do tipo 'signed' ou 'unsigned'''

    if df[col].min() >= 0:
        return(False)
    else:
        return(True)


def float_is_integer(col,df):
    '''Identifica se um float pode ser escrito como 'int' '''

    # identifica se um numero float pode ser escrito como int
    func= lambda x: False if pd.isna(x) or (abs(x-int(x)))>0 else True

    # Obs: se o valor for Nan o número não ppode ser escrito como
    # inteiro, porque Nan sempre é do tipo float. Esta identificação
    # está incluida na funcao lambda acima

    # número de elementos na coluna
    tam = df[col].size

    # numero de elementos que podem ser escritos como int
    num_int=df[col].apply(func).sum()

    if num_int==tam:
        return(True)
    else:
        return(False)


def object_is_categorial(col,df):
    '''Identifica se um tipo 'object' pode ser escrito com 'categorical'''

    n_valores_unicos = len(df[col].unique())
    n_linhas = len(df[col])

    # identifica se 'n_valores_unicos' é menos que 50% de 'n_linhas'
    if n_valores_unicos / n_linhas < 0.5:
        return(True)
    else:
        return(False)



#---------------------------------------------------------------
# Funções para calculos do menor subtipo numérico
#---------------------------------------------------------------

def downcast_num(col, df):

    '''Retorna o tipo de 'downcast' para ser usado na funcao
    pd.to_numeric para uma variável numérica. Os tipos de
    retorno possíveis são os tipos permitidas para a função
    pd.to_numeric:

    - signed: para int signed
    - unsigned: para int unsigned
    - float: para float

    OBS: uma variável 'float' pode ser escrita com 'int' neste caso
    o retorno para o float deve ser 'signed' ou 'unsigned'

    Output:
    None: a variável não é numerica
    signed: downcast é int com sinal
    unsigned: downcast é int com sem sinal
    float: downcast é float
    '''

    # valor retornado para o tipo 'object'
    downcast=None

    # coluna tipo 'int'
    if(df[col].dtype=='int'):

        # 'signed' ou 'unsigned'
        if(int_is_signed(col,df)):
            downcast='signed'
        else:
            downcast='unsigned'


    # coluna tipo 'float'
    elif(df[col].dtype=='float'):

        # pode ser escrito como 'int'
        if(float_is_integer(col,df)):

            # 'signed' ou 'unsigned'
            if(int_is_signed(col,df)):
                downcast='signed'
            else:
                downcast='unsigned'

        # não pode ser escrito com 'int'
        else:
            downcast='float'

    return(downcast)



def menor_subtipo_num(col, downcast, df):
    '''
    encontra o menor subtipo para variáveis numéricas
    a partir de um tipo (downcast)
    '''
    
    # encontra o menor tipo
    df_convertida = df[[col]]\
                    .apply(pd.to_numeric,downcast=downcast)

    # menor tipo
    return(str(df_convertida.dtypes.values[0]))




#-----------------------------------------------------------------------
# Retorna um dicionário com os tipos de variáveis para optimização
#----------------------------------------------------------------------

def obtem_subtipos(df, can_float_be_int=False):

    '''Retorna um dicionário com os tipos e subtipos de
    variáveis para optimização:

     int8, int32, int64
     uint8, uint32, uint64
     float32, float64
     categorical

    Input:
    can_float_int: indica se é possível fazer a busca pelo menor tipo onde
       float sem casas decimais representativas podem ser consideradas inteiros.
       Quando colocado True, a optimização pode ser maior pois os tipos minimos de
       Algumas colunas podem se menores, mas o valor True causa problamas quando
       quando na amostra não existem numeros Nan e na dados totais existem, nestes
       casas será identifica numeros int como menor tipo mas nos depararemos com
       valores Nan(que são float) nos dados completos e isto gerá um de leitura.
       Nestes casos o ideal é uzar can_float_int=False.

    Obs: as variáveis que não entram não podem ter seus tamanhos
    reduzidos
    '''

    dic_min_type={}
    for col in df.columns:


        if df[col].dtype=='int':

            # encontra o menor subtipo
            downcast= downcast_num(col, df)
            dic_min_type[col]=menor_subtipo_num(col, downcast, df)


        elif df[col].dtype=='float':

            # calcula downcast
            if can_float_be_int:
                downcast = downcast_num(col, df)
            else:
                downcast = 'float'

            # encontra o menor subtipo
            dic_min_type[col]=menor_subtipo_num(col, downcast, df)


        elif df[col].dtype=='O':

            # identifica se pode ser ecrito como 'categorical'
            if(object_is_categorial(col,df)):
                dic_min_type[col]='category'
            else:
                dic_min_type[col]='object'

    return(dic_min_type)



#--------------------------------------------------------------------
#   Muda os tipo de um dataframe na memória
#--------------------------------------------------------------------

def tranforma_tipos(df,dict_, inplace=False):
    '''Muda os tipos de um dataframe para subtidos

    Input:
    dict_: dicionário com as mudançãs para cada coluna
    inplace: identifica se alteração deve ser feita no próprio 'df'
        informado como input, ou se deve ser feita em uma cópia que será
        retornada com output da função
    '''

    if(inplace):
        for key in dict_:
            df[key]= df[key].astype(dict_[key])

    else:
        df_copy= df.copy()
        for key in dict_:
            df_copy[key]= df_copy[key].astype(dict_[key])

        return(df_copy)


def object_to_float(df,dict_, inplace=False):

    '''Transforma colunas do tipo 'objetos' em colunas do tipo 'float'
    por meio de operações predefinidas

    Input:
    dict_: dicionário com as transformações que devem ser feitas em cada coluna
    inplace: identifica se a alteração deve ser feita no próprio 'df'
        informado como input, ou se deve ser feita em uma cópia que será
        retornada com output da função
    '''

    if(inplace):
        for key in dict_:
            df[key] = df[key].apply(dict_[key]).astype('float')

    else:
        df_copy= df.copy()
        for key in dict_:
            df_copy[key] = df_copy[key].apply(dict_[key]).astype('float')


        return(df_copy)
