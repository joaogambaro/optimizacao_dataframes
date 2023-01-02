from pathlib import Path
import os


# caminho absoluto deste script
path_script= os.path.abspath(__file__)
#current_path = os.getcwd()

# path da raiz do projeto
PATH_ROOT = Path(path_script).parent.parent

# caminhos dos diretórios
DADOS_DIR = PATH_ROOT/'dados_tests'
MODULOS_DIR = PATH_ROOT/'modulos'




# ponto de entrada
#if __name__=="__main__":
