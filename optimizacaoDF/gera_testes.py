

import pandas as pd
import coleta_amostra as amo
from caminhos.paths import DADOS_DIR

def test_cont_lines():

    # camninho para o arquivo
    str_file=DADOS_DIR/"dados_1.csv"

    # número de linhas no arquivo
    n=amo.cont_lines(str_file)

    print("n", n)
    # realiza o teste
    #self.assertEqual(n,21,
    #         f"numeros diferentes: num.linhas (21), "\
    #         f"numero identificado({n})")


# ponto de entrada
if __name__=="__main__":
    test_cont_lines()
