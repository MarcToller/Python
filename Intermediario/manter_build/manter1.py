from concurrent.futures import ThreadPoolExecutor
from functools import partial
import subprocess
import os
from datetime import datetime

data_inicio = datetime.timestamp

listaOK = []
CAMINHO_PASTA = 'C:\Bin.separado\Delphi\Atalhos\Executaveis\ManterBuild'

def executar_tarefa(arquivo):
    try:        
        caminho_completo = os.path.join(CAMINHO_PASTA, arquivo)          
        #retorno = subprocess.run([caminho_completo, '/NaoExecutar'], shell=True, cwd=CAMINHO_PASTA, timeout=300) 
        #retorno = subprocess.run([caminho_completo, '/NaoExecutar'], shell=True, cwd=CAMINHO_PASTA, capture_output=True, text=True) 
        retorno = subprocess.run([caminho_completo, '/NaoExecutar'], shell=True, cwd=CAMINHO_PASTA) 
        #retorno = subprocess.Popen(caminho_completo, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        #retorno = subprocess.call([caminho_completo, 'NaoExecutar'], shell=True, cwd=CAMINHO_PASTA, timeout=300)     
        #retorno = subprocess.call([caminho_completo, '/NaoExecutar'], shell=False, cwd=CAMINHO_PASTA, timeout=30)         
    except subprocess.CalledProcessError:
        print(f'erro1 em {arquivo}')
        return
    except subprocess.TimeoutExpired:
        print(f'erro2 em {arquivo}')
        return

    if retorno.returncode > 0:
        print(f'erro3 em {arquivo}')
        return
    listaOK.append(arquivo)    
    #try:
     
    #except subprocess.TimeoutExpired:
    #    retorno.kill()  
    #    return
    #print(f'passou {arquivo}')  

    # Código para executar a tarefa

# Número máximo de threads simultâneas para o primeiro ThreadPoolExecutor
max_threads1 = 1

# Número máximo de threads simultâneas para o segundo ThreadPoolExecutor
max_threads2 = 2


lista_arquivos_pesados = ['04_TestaWinDP.bat', '03_TestaWinContas.bat']
#lista_arquivos_leves = ['01_TestaDCComparaEstruturas.bat', '02_TestaFrameWorkDTC.bat', '03_TestaWinContas.bat', '04_TestaWinDP.bat' ]
#lista_arquivos_pesados = ['ContabMillenium.bat', 'WinCaixaNew.bat', 'WinLalur.bat']
lista_arquivos_leves = ['01_TestaDCComparaEstruturas.bat', '02_TestaFrameWorkDTC.bat' ]

# Criação dos ThreadPoolExecutors
with ThreadPoolExecutor(max_workers=max_threads1) as executor1, \
        ThreadPoolExecutor(max_workers=max_threads2) as executor2:
    
    for arquivo_leve in lista_arquivos_leves:
        tarefa1 = partial(executar_tarefa, arquivo_leve)
        executor1.submit(tarefa1)        

    for arquivo_pesado in lista_arquivos_pesados:
        tarefa2 = partial(executar_tarefa, arquivo_pesado)
        executor2.submit(tarefa2)

#executor1.shutdown(wait=True)
#executor2.shutdown(wait=True)       

data_fim = datetime.timestamp

#os.system('cls')
print('acabou')
#delta = (data_inicio - data_fim).total_seconds()
#print('Tempo:', delta)
print(listaOK)