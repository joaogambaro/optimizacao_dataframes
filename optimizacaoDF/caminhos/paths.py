from pathlib import Path
import os


# caminho absoluto deste script
path_script= os.path.abspath(__file__)
#current_path = os.getcwd()

# path da raiz do projeto
PATH_ROOT = Path(path_script).parent.parent
