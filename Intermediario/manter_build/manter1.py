from concurrent.futures import ThreadPoolExecutor
from functools import partial
import subprocess
import os

CAMINHO_PASTA = 'C:\\Bin.dtc\\Delphi\\Atalhos\\Executaveis\\ManterBuild'

def executar_tarefa(arquivo):
    try:
        caminho_completo = os.path.join(CAMINHO_PASTA, arquivo)  
        retorno = subprocess.Popen(caminho_completo, shell=True, cwd=CAMINHO_PASTA, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        #retorno = subprocess.call(arquivo, shell=True, cwd=CAMINHO_PASTA) 
    except:
        print(f'erro1 em {arquivo}')
        return

    if retorno.returncode > 0:
        print(f'erro2 em {arquivo}')
        return
    try:
        retorno.wait(timeout=20)
    except subprocess.TimeoutExpired:
        retorno.kill()  
        return
    print(f'passou {arquivo}')  

    # Código para executar a tarefa

# Número máximo de threads simultâneas para o primeiro ThreadPoolExecutor
max_threads1 = 1

# Número máximo de threads simultâneas para o segundo ThreadPoolExecutor
max_threads2 = 2



lista_arquivos_leves = ['01_TestaDCComparaEstruturas.bat', '02_TestaFrameWorkDTC.bat', '03_TestaWinContas.bat', '04_TestaWinDP.bat' ]
lista_arquivos_pesados = ['ContabMillenium.bat', 'WinCaixaNew.bat', 'WinLalur.bat']

# Criação dos ThreadPoolExecutors
with ThreadPoolExecutor(max_workers=max_threads1) as executor1, \
        ThreadPoolExecutor(max_workers=max_threads2) as executor2:
    
    for arquivo_leve in lista_arquivos_leves:
        tarefa1 = partial(executar_tarefa, arquivo_leve)
        executor1.submit(tarefa1)        

    for arquivo_pesado in lista_arquivos_pesados:
        tarefa2 = partial(executar_tarefa, arquivo_pesado)
        executor1.submit(tarefa2)

print('acabou')        