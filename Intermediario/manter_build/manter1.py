from concurrent.futures import ThreadPoolExecutor
from functools import partial
import subprocess


def executar_tarefa(arquivo):
    try:
        retorno = subprocess.Popen(arquivo, shell=True, cwd='caminho_pasta', stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
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

    # Código para executar a tarefa

# Número máximo de threads simultâneas para o primeiro ThreadPoolExecutor
max_threads1 = 1

# Número máximo de threads simultâneas para o segundo ThreadPoolExecutor
max_threads2 = 2

lista_arquivos_leves = ['1', '2', '3']
lista_arquivos_pesados = ['4', '5', '6']

# Criação dos ThreadPoolExecutors
with ThreadPoolExecutor(max_workers=max_threads1) as executor1, \
        ThreadPoolExecutor(max_workers=max_threads2) as executor2:
    
    for arquivo_leve in lista_arquivos_leves:
        tarefa1 = partial(executar_tarefa, arquivo_leve)
        executor1.submit(tarefa1)

    for arquivo_pesado in lista_arquivos_pesados:
        tarefa2 = partial(executar_tarefa, arquivo_pesado)
        executor1.submit(tarefa2)