#####  https://chat.openai.com/c/72b35f1a-7df4-4c8f-a447-2aa27bc3605d


from concurrent.futures import ThreadPoolExecutor
from functools import partial
import subprocess
import os
from datetime import datetime
from sistemas import lista_execusao_assincrona
import json
import shutil


CHAVE_SISTEMA = 'sistema'
CHAVE_STATUS = 'status'
CHAVE_TEMPO = 'tempo'
VALOR_SEM_FALHA = 'Build OK'
CAMINHO_PASTA_MANTER_BUILD = os.path.join(os.environ['DELPHI_SVN'], 'Atalhos', 'Executaveis', 'ManterBuild')
CAMINHO_PASTA_RESULTADO = os.path.join(CAMINHO_PASTA_MANTER_BUILD, 'Resultado')
CAMINHO_PASTA_FALHA = os.path.join(CAMINHO_PASTA_RESULTADO, 'Falhas')
FALHA_BUILD = 'Build FAILED.'
FALHA_BUILD_MENSAGEM = 'Falha no Build'
FALHA_ASSINAR_D = 'Falha ao tentar assinar digitalmente o projeto'
FALHA_TIME_OUT = 'Falha de timeout'

hora_inicio = datetime.now()
lista_resultados = []
lista_execusao_sincrona = []

shutil.rmtree(CAMINHO_PASTA_RESULTADO, ignore_errors=True)

if not os.path.exists(CAMINHO_PASTA_FALHA):
    os.makedirs(CAMINHO_PASTA_FALHA)

def verificar_arquivo_saida(nome_arquivo) -> str:     
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        if FALHA_BUILD in conteudo:
            return FALHA_BUILD_MENSAGEM
        elif FALHA_ASSINAR_D in conteudo:
            return FALHA_ASSINAR_D
        else:
            return FALHA_TIME_OUT

def executar_tarefa(arquivo):
    dicionario_resultado = {}
    try:    
        print(arquivo)     
        dicionario_resultado[CHAVE_SISTEMA] = arquivo
        dicionario_resultado[CHAVE_STATUS] = VALOR_SEM_FALHA        

        caminho_completo = os.path.join(CAMINHO_PASTA_MANTER_BUILD, arquivo) 
        vArquivoTxt = os.path.splitext(arquivo)[0]+'.txt'                
        
        vCaminhoArquivoSaida = os.path.join(CAMINHO_PASTA_FALHA, vArquivoTxt)          

        vinicio = datetime.now()  
        with open(vCaminhoArquivoSaida, 'w') as arquivo_saida:
            subprocess.run([caminho_completo, '/NaoExecutar'], shell=True, cwd=CAMINHO_PASTA_MANTER_BUILD, timeout=150, stdout=arquivo_saida)
        
        vfinal = datetime.now()  

        dicionario_resultado[CHAVE_TEMPO] = (vfinal - vinicio).total_seconds()
    except subprocess.CalledProcessError:
        dicionario_resultado[CHAVE_STATUS] = 'Falha Desconhecida' 
        lista_resultados.append(dicionario_resultado)        
        return
    except subprocess.TimeoutExpired:    
        dicionario_resultado[CHAVE_STATUS] = verificar_arquivo_saida(vCaminhoArquivoSaida)
        lista_resultados.append(dicionario_resultado)                         
        return
        
    os.remove(vCaminhoArquivoSaida)
    
    lista_resultados.append(dicionario_resultado)           

max_threads = 2

#lista_arquivos_pesados = ['04_TestaWinDP.bat', '03_TestaWinContas.bat']
#lista_arquivos_leves = ['02_TestaFrameWorkDTC.bat', '03_TestaWinContas.bat', '04_TestaWinDP.bat', '01_TestaDCComparaEstruturas.bat']
#lista_arquivos_pesados = ['XML_Importer.bat', 'WinLalur.bat']
#lista_arquivos_leves = ['01_TestaDCComparaEstruturas.bat', '02_TestaFrameWorkDTC.bat', '04_TestaWinDP.bat', '03_TestaWinContas.bat']

# Criação dos ThreadPoolExecutors
with ThreadPoolExecutor(max_workers=max_threads) as thread_pool_dois_sistemas:   

    for sistemas in lista_execusao_assincrona:
        thread = partial(executar_tarefa, sistemas['sistema_1'])
        thread_pool_dois_sistemas.submit(thread)  

        if sistemas.get('sistema_2'):
            thread = partial(executar_tarefa, sistemas['sistema_2'])
            thread_pool_dois_sistemas.submit(thread)            
    
thread_pool_dois_sistemas.shutdown(wait=True)


if len(lista_execusao_sincrona) > 0:
    with ThreadPoolExecutor(max_workers=1) as thread_pool_sistema_unico:   
        for sistema in lista_execusao_sincrona:
            thread = partial(executar_tarefa, sistema['sistema_1'])
            thread_pool_sistema_unico.submit(thread)  
        
    thread_pool_sistema_unico.shutdown(wait=True)


os.system('cls')

hora_fim = datetime.now()
tempo_decorrido = (hora_fim - hora_inicio).total_seconds() // 60
print(f'Tempo: {tempo_decorrido} minutos')
for resultado in lista_resultados:    
    print(resultado)

arquivo_json = os.path.join(CAMINHO_PASTA_RESULTADO, 'resultado.json')
with open(arquivo_json, 'w') as arquivo:
    json.dump(lista_resultados, arquivo, indent=4)
#print('Sistemas OK', listaOK)
#print('Falhas: ', listaErros)
