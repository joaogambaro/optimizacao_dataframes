


# caminho da pasta raiz dos testes
import os
from pathlib import Path
path_script= os.path.abspath(__file__)      #caminho deste script
PATH_ROOT = Path(path_script).parent.parent #path da raiz


# caminhos dos diretórios
DADOS_DIR = PATH_ROOT/'dados_tests'
