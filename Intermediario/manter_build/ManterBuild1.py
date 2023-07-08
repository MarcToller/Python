#####  https://chat.openai.com/c/72b35f1a-7df4-4c8f-a447-2aa27bc3605d


from concurrent.futures import ThreadPoolExecutor
from functools import partial
import subprocess
import os
from datetime import datetime
from sistemas import *
import json

# listas = retorna_listas()
lista_execusao_sincrona = [] # listas[CHAVE_LISTA_SINCRONA]
lista_execusao_assincrona = lista_execusao_assincrona #listas[CHAVE_LISTA_ASSINCRONA]

hora_inicio = datetime.now()
lista_resultados = []

def status_saida(linha: str) -> str: 

    if str(FALHA_BUILD) in str(linha):        
        return FALHA_BUILD_MENSAGEM
    
    return ''
   
def executar_arquivo_bat(arquivo: str, tempo_ultima_execucao: int = 0):
    dicionario_resultado = {}    
    try:     
        dicionario_resultado[CHAVE_SISTEMA] = arquivo
        dicionario_resultado[CHAVE_STATUS] = VALOR_SEM_FALHA 
        dicionario_resultado[CHAVE_TEMPO] = tempo_ultima_execucao

        caminho_completo_bat = os.path.join(CAMINHO_PASTA_MANTER_BUILD, arquivo) 

        inicio = datetime.now()  
        print(f'Arquivo {arquivo} - Início: {inicio}')

        processo = subprocess.Popen([caminho_completo_bat, '/NaoExecutar'], shell=True, cwd=CAMINHO_PASTA_MANTER_BUILD, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        for linha in processo.stdout:
            vStatus = status_saida(str(linha))
            if vStatus == FALHA_BUILD_MENSAGEM: 
                dicionario_resultado[CHAVE_STATUS] = vStatus                
                processo.terminate()                
            
        time_out = tempo_ultima_execucao * 2 if tempo_ultima_execucao > 0 else None
        processo.wait(time_out)  

        final = datetime.now() 
        print(f'Arquivo {arquivo} - final: {final}') 
        
        total_segundos = (final - inicio).total_seconds() 
        if total_segundos > tempo_ultima_execucao:
            dicionario_resultado[CHAVE_INFORMACAO_ADICIONAL] = f'Build levou mais que {PERCENTUAL_TEMPO_LIMITE}% do tempo da última execução.'     
        dicionario_resultado[CHAVE_TEMPO] = int(total_segundos)        
    except subprocess.TimeoutExpired:    
        dicionario_resultado[CHAVE_STATUS] = 'TimeOut - Build interrompido propositelmente.'
        dicionario_resultado[CHAVE_INFORMACAO_ADICIONAL] = 'Build levou mais que o dobro do tempo da última execução.'
        lista_resultados.append(dicionario_resultado)                
        return

    except Exception as e:               
        dicionario_resultado[CHAVE_STATUS] = 'Ocorreu uma falha desconhecida'
        dicionario_resultado[CHAVE_INFORMACAO_ADICIONAL] = 'exception: '+e.__class__.__name__ 
        lista_resultados.append(dicionario_resultado)                
        return
        
    lista_resultados.append(dicionario_resultado)           

if len(lista_execusao_assincrona) > 0:        
    with ThreadPoolExecutor(max_workers=3) as thread_pool_dois_sistemas:   
        for arquivo_bat in lista_execusao_assincrona:  
            sistema = arquivo_bat.get(CHAVE_SISTEMA)  
            tempo_ultima_execucao = arquivo_bat.get(CHAVE_TEMPO) 

            thread = partial(executar_arquivo_bat, sistema, tempo_ultima_execucao)
            thread_pool_dois_sistemas.submit(thread) 
        
    thread_pool_dois_sistemas.shutdown(wait=True)

if len(lista_execusao_sincrona) > 0:
    with ThreadPoolExecutor(max_workers=1) as thread_pool_sistema_unico:   
        for arquivo_bat in lista_execusao_sincrona:
            sistema = arquivo_bat.get(CHAVE_SISTEMA)         
            thread = partial(executar_arquivo_bat, sistema)
            thread_pool_sistema_unico.submit(thread)  
        
    thread_pool_sistema_unico.shutdown(wait=True)


os.system('cls')

hora_fim = datetime.now()
tempo_decorrido = (hora_fim - hora_inicio).total_seconds() // 60
print(f'Tempo: {tempo_decorrido} minutos')

lista_resultados_ordenada = sorted(lista_resultados, key=lambda x: x[CHAVE_TEMPO])

for resultado in lista_resultados_ordenada:    
    print(resultado)

with open(CAMINHO_RESULTADO_JSON, 'w') as arquivo:
    json.dump(lista_resultados_ordenada, arquivo, indent=4)
