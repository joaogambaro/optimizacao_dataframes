import unittest
import pandas as pd

import optimizacaoDF.coleta_amostra as amo
from tests.caminhos.paths import DADOS_DIR




class TestFunc(unittest.TestCase):

    # teste 1
    def test_cont_lines(self):

        # camninho para o arquivo
        str_file=DADOS_DIR/"dados_1.csv"

        # número de linhas no arquivo
        n=amo.cont_lines(str_file)

        # numero de linhas no df
        df = pd.read_csv(str_file)
        ndf=df.shape[0]


        # realiza o teste
        self.assertEqual(n,ndf+1,
                 f"numeros diferentes: num.linhas (21), "\
                 f"numero identificado({n})")

    # teste 2
    def test_coleta_amostr_1(self):

        '''
        Com os parametros:
        -> is_rand_sample=True
        -> tamAm: (tipo 'int' maior ou igual a um(coleta n linhas dos dados originais))
        '''

        # caminho para o arquivo
        str_file=DADOS_DIR/"dados_1.csv"
        is_rand_sample=True


        for tamAm in [1,2,5,7,10]:

            # coleta a amostra
            df=amo.coleta_amostr(tamAm,
                str_file,
                is_rand_sample=is_rand_sample)

            # numero de linhas no df
            n=df.shape[0]

            # realiza o teste
            self.assertEqual(n,tamAm,
                f"numeros diferentes: num.linhas esperado (7), "\
                f"numero no df ({n})")



    # teste 3
    def test_coleta_amostr_2(self):

        '''
        Com o parametros:
        -> is_rand_sample=primeiras True
        -> tamAm: (tipo float, entre 0 e 1 (coleta um fração dos dados originais))
        '''

        # camninho para o arquivo
        str_file=DADOS_DIR/"dados_1.csv"
        is_rand_sample=True

        # testa par diversos valores
        for tamAm in [0.1, 0.33, 0.456, 0.6, 0.9, 0.99]:

            # coleta amostra
            df=amo.coleta_amostr(tamAm,
                    str_file,
                    is_rand_sample=is_rand_sample)

            # numero de linhas no df
            n=df.shape[0]

            # realiza o teste
            self.assertEqual(n,int(tamAm*21),
            f"numeros diferentes: num.linhas esperado {int(tamAm*21)}, "\
            f"numero no df ({n})")




# ponto de entrada
if __name__=="__main__":
    unittest.main()
