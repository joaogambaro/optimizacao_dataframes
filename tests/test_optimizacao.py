
import unittest
import pandas as pd

import modulos.analise_resultados as ana
import modulos.optimizacao_dataframe as opt
import pandas as pd

from caminhos.paths import DADOS_DIR


class TestFunc(unittest.TestCase):

    def test_downcast_num(self):

        # carrega os dados
        str_file=DADOS_DIR/"dados_1.csv"
        df = pd.read_csv(str_file)

        # valores esperados para as colunas
        dict_downcast={
            'int_signned': 'signed',
            'int_unsigned': 'unsigned',
            'float': 'float',
            'float_int_signed': 'signed',
            'float_int_unsigned': 'unsigned',
            'float_int_signed_NAN': 'float',
            'string_categorical': None,
            'string_nao_categorical': None
            }


        for col in df.columns:

            # downcast para a coluna col
            downcast = opt.downcast_num(col, df)

            self.assertEqual(downcast,
                             dict_downcast[col],
                             f"String {col}: foi encontrado '{downcast}' é esperado '{dict_downcast[col]}'")


    def test_menor_subtipo_num(self):

        # carrega os dados
        str_file=DADOS_DIR/"dados_1.csv"
        df = pd.read_csv(str_file)

        # valores esperados para as colunas
        dict_subtipo={
            'int_signned': 'int8',
            'int_unsigned': 'uint8',
            'float': 'float32',
            'float_int_signed': 'int8',
            'float_int_unsigned': 'uint8',
            'float_int_signed_NAN': 'float32',
            }

        for col in df.columns:

            # identifica se a coluna armazena valores numéricos
            if df[col].dtype=='int' or df[col].dtype=='float':

                # calcula o menor subtipo
                downcast = opt.downcast_num(col, df)
                subtipo = opt.menor_subtipo_num(col, downcast, df)

                self.assertEqual(subtipo,
                         dict_subtipo[col],
                         f"String {col}: foi encontrado '{subtipo}' "\
                         f"é esperado '{dict_subtipo[col]}'")




    def test_obtem_subtipos_1(self):
        '''
        Com o parametro "can_float_be_int=True"
        '''

        # carrega os dados
        str_file=DADOS_DIR/"dados_1.csv"
        df = pd.read_csv(str_file)

        # valores esperados para as colunas
        dict_sub_esperado={
            'int_signned': 'int8',
            'int_unsigned': 'uint8',
            'float': 'float32',
            'float_int_signed': 'int8',
            'float_int_unsigned': 'uint8',
            'float_int_signed_NAN': 'float32',
            'string_categorical': 'category',
            'string_nao_categorical': 'object'
            }

        # aplica o método
        dict_sub_obtido = opt.obtem_subtipos(df, can_float_be_int=True)

        self.assertEqual(dict_sub_esperado,
                     dict_sub_obtido,
                     f"O dicionário esperado e o retornado não são iguais")



    def test_obtem_subtipos_2(self):

        '''
        Com o parametro "can_float_be_int=False"
        '''

        # carrega os dados
        str_file=DADOS_DIR/"dados_1.csv"
        df = pd.read_csv(str_file)

        # valores esperados para as colunas
        dict_sub_esperado={
            'int_signned': 'int8',
            'int_unsigned': 'uint8',
            'float': 'float32',
            'float_int_signed': 'float32',
            'float_int_unsigned': 'float32',
            'float_int_signed_NAN': 'float32',
            'string_categorical': 'category',
            'string_nao_categorical': 'object'
            }

        # aplica o método
        dict_sub_obtido = opt.obtem_subtipos(df, can_float_be_int=False)

        self.assertEqual(dict_sub_esperado,
                 dict_sub_obtido,
                 f"O dicionário esperado e o retornado não são iguais")







# ponto de entrada
if __name__=="__main__":
    unittest.main()
