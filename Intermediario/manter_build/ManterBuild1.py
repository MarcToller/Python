#####  https://chat.openai.com/c/72b35f1a-7df4-4c8f-a447-2aa27bc3605d


from concurrent.futures import ThreadPoolExecutor
from functools import partial
import subprocess
import os
from datetime import datetime
from sistemas import *
import json

listas = retorna_listas()
lista_execusao_sincrona = listas[CHAVE_LISTA_SINCRONA]
lista_execusao_assincrona = listas[CHAVE_LISTA_ASSINCRONA]
lista_resultados = []

def status_saida(linha: str) -> str: 

    if str(FALHA_BUILD) in str(linha):        
        return FALHA_BUILD_MENSAGEM
    
    return VALOR_SEM_FALHA
   
def executar_arquivo_bat(dicionario_execucao: dict):
    dicionario_resultado = {}
    try:     
        arquivo = dicionario_execucao[CHAVE_SISTEMA] 
        tempo_ultima_execucao = dicionario_execucao[CHAVE_TEMPO_LIMITE] 

        dicionario_resultado[CHAVE_SISTEMA] = arquivo        
        dicionario_resultado[CHAVE_TEMPO] = tempo_ultima_execucao

        caminho_completo_bat = os.path.join(CAMINHO_PASTA_MANTER_BUILD, arquivo) 

        inicio = datetime.now()  
        print(f'{arquivo} - Início: {inicio}')

        processo = subprocess.Popen([caminho_completo_bat, '/NaoExecutar'], shell=True, cwd=CAMINHO_PASTA_MANTER_BUILD, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        for linha in processo.stdout:
            dicionario_resultado[CHAVE_STATUS] = status_saida(str(linha))

            if dicionario_resultado[CHAVE_STATUS] == FALHA_BUILD_MENSAGEM:                 
                processo.terminate()                
            
        time_out = tempo_ultima_execucao * 2 if tempo_ultima_execucao > 0 else None
        processo.wait(time_out)  

        final = datetime.now() 
        print(f'{arquivo} - final: {final}') 
        
        total_segundos = (final - inicio).total_seconds()

        if (tempo_ultima_execucao > 0) and (total_segundos > tempo_ultima_execucao):
            dicionario_resultado[CHAVE_INFORMACAO_ADICIONAL] = f'Build levou mais que {PERCENTUAL_TEMPO_LIMITE}% do tempo da última execução.'     

        dicionario_resultado[CHAVE_TEMPO] = int(total_segundos)        
    except subprocess.TimeoutExpired:    
        dicionario_resultado[CHAVE_STATUS] = FALHA_TIME_OUT
        dicionario_resultado[CHAVE_INFORMACAO_ADICIONAL] = 'Build levou mais que o dobro do tempo da última execução.'
        lista_resultados.append(dicionario_resultado)                        

    except Exception as e:               
        dicionario_resultado[CHAVE_STATUS] = 'Ocorreu uma falha desconhecida'
        dicionario_resultado[CHAVE_INFORMACAO_ADICIONAL] = 'exception: '+e.__class__.__name__ 
        lista_resultados.append(dicionario_resultado)                        
        
    lista_resultados.append(dicionario_resultado)  

hora_inicio = datetime.now()

with ThreadPoolExecutor(max_workers=1) as execucao_sincrona, ThreadPoolExecutor(max_workers=2) as execucao_assincrona:
    
    if len(lista_execusao_sincrona) > 0:
        for sistema_sincrono in lista_execusao_sincrona:
            tarefa_sincrona = partial(executar_arquivo_bat, sistema_sincrono)
            execucao_sincrona.submit(tarefa_sincrona)        

    if len(lista_execusao_assincrona) > 0:
        for sistema_assincrono in lista_execusao_assincrona:
            tarefa_assincrona = partial(executar_arquivo_bat, sistema_assincrono)
            execucao_assincrona.submit(tarefa_assincrona)

execucao_sincrona.shutdown(wait=True)
execucao_assincrona.shutdown(wait=True)


os.system('cls')

hora_fim = datetime.now()

# tempo_decorrido = (hora_fim - hora_inicio).total_seconds() // 60
# print(f'Tempo: {tempo_decorrido} minutos')

tempo_decorrido = (hora_fim - hora_inicio).total_seconds()
print(f'Tempo: {tempo_decorrido} segundos')

lista_resultados_ordenada = sorted(lista_resultados, key=lambda x: x[CHAVE_TEMPO])

for resultado in lista_resultados_ordenada:    
    print(resultado)

with open(CAMINHO_RESULTADO_JSON, 'w') as arquivo:
    json.dump(lista_resultados_ordenada, arquivo, indent=4)
