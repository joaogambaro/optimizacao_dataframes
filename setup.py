
from setuptools import find_packages, setup

#le a versao do pacote
#strFile= "modelo/VERSION"
#_versao=open(strFile,).readline().strip()

#OBS.: é necessário usar readline() (para ler a primeira linha do arquivo)
#e também strip() (para eliminar a leitura da quebra de linha do arquivo)

setup(
    name="optimizacao_dataframe", #1*
    version="1.0.0",
    description="Pacote para auxiliar na optimizacao de dataframes pandas",
    author= "Joao Paulo Gambaro",
    author_email="joaopaulogambaro@gmail.com",
    python_requires= ">=3.10",
    install_requires=['pandas>=1.5.0'],
    packages=find_packages(
        include=['optimizacaoDF*'],
        exclude=['tests','optimizacaoDF/gera_testes.py'],
        ),

)

#OBS:
#1*-> o nome usado para importar o pacote  não é o nome
#     fornecido neste campo. O nome uisado no import é o nome
#     da pasta do pacote
