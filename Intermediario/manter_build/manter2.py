#####  https://chat.openai.com/c/72b35f1a-7df4-4c8f-a447-2aa27bc3605d


from concurrent.futures import ThreadPoolExecutor
from functools import partial
import subprocess
import os
from datetime import datetime
from sistemas import lista_sistemas
import json
import shutil


CHAVE_SISTEMA = 'sistema'
CHAVE_STATUS = 'status'
CHAVE_TEMPO = 'tempo'
VALOR_SEM_FALHA = 'Build OK'
CAMINHO_PASTA =  os.path.join(os.environ['DELPHI_SVN'], 'Atalhos', 'Executaveis', 'ManterBuild')

hora_inicio = datetime.now()
lista_resultados = []

def verificar_arquivo_saida(nome_arquivo) -> str:    
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        if 'Build FAILED.' in conteudo:
            return 'Falha no Build'
        elif 'Falha ao tentar assinar digitalmente o projeto' in conteudo:
            return 'Falha ao tentar assinar digitalmente o projeto'
        else:
            return 'Falha de timeout'

def executar_tarefa(arquivo):
    dicionario_resultado = {}
    try:    
        print(arquivo)     
        dicionario_resultado[CHAVE_SISTEMA] = arquivo
        dicionario_resultado[CHAVE_STATUS] = VALOR_SEM_FALHA        

        caminho_completo = os.path.join(CAMINHO_PASTA, arquivo)          
        
        
        vArquivoTxt = os.path.splitext(arquivo)[0]+'.txt'
        vCaminhoArquivoSaida = os.path.join(CAMINHO_PASTA, 'resultado', 'falhas')          

        #shutil.rmtree(vCaminhoArquivoSaida)

        if not os.path.exists(vCaminhoArquivoSaida):
            os.makedirs(vCaminhoArquivoSaida)

        vCaminhoArquivoSaida = os.path.join(vCaminhoArquivoSaida, vArquivoTxt)          

        vinicio = datetime.now()  
        with open(vCaminhoArquivoSaida, 'w') as arquivo_saida:
            subprocess.run([caminho_completo, '/NaoExecutar'], shell=True, cwd=CAMINHO_PASTA, timeout=150, stdout=arquivo_saida)
        
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

max_threads1 = 2

#lista_arquivos_pesados = ['04_TestaWinDP.bat', '03_TestaWinContas.bat']
#lista_arquivos_leves = ['02_TestaFrameWorkDTC.bat', '03_TestaWinContas.bat', '04_TestaWinDP.bat', '01_TestaDCComparaEstruturas.bat']
#lista_arquivos_pesados = ['XML_Importer.bat', 'WinLalur.bat']
#lista_arquivos_leves = ['01_TestaDCComparaEstruturas.bat', '02_TestaFrameWorkDTC.bat', '04_TestaWinDP.bat', '03_TestaWinContas.bat']

# Criação dos ThreadPoolExecutors
with ThreadPoolExecutor(max_workers=max_threads1) as executor1:   

    for sistemas in lista_sistemas:
        tarefa1 = partial(executar_tarefa, sistemas['sistema_1'])
        executor1.submit(tarefa1)  
        if sistemas.get('sistema_2'):
            tarefa1 = partial(executar_tarefa, sistemas['sistema_2'])
            executor1.submit(tarefa1)            
    
executor1.shutdown(wait=True)
#executor2.shutdown(wait=True)       

os.system('cls')

hora_fim = datetime.now()
tempo_decorrido = (hora_fim - hora_inicio).total_seconds() / 60
print(f'Tempo: {tempo_decorrido} minutos')
for resultado in lista_resultados:    
    print(resultado)

arquivo_json = caminho_completo = os.path.join(CAMINHO_PASTA, 'resultado', 'resultado.json')
with open(arquivo_json, 'w') as arquivo:
    json.dump(lista_resultados, arquivo, indent=4)
#print('Sistemas OK', listaOK)
#print('Falhas: ', listaErros)
