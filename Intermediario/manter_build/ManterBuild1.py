#####  https://chat.openai.com/c/72b35f1a-7df4-4c8f-a447-2aa27bc3605d


from concurrent.futures import ThreadPoolExecutor
from functools import partial
import subprocess
import os
from datetime import datetime
from sistemas import *
import json

listas = retorna_listas()
# lista_executaveis_pesados = lista_pesados
# lista_executaveis_leves = lista_leves
# lista_executaveis_medios = lista_medios

lista_executaveis_pesados = listas[CHAVE_LISTA_ARQUIVOS_PESADOS]
lista_executaveis_leves = listas[CHAVE_LISTA_ARQUIVOS_LEVES]
lista_executaveis_medios = listas[CHAVE_LISTA_ARQUIVOS_MEDIOS]
lista_resultados = []

def configurar_lista(lista) -> list:
    tempo_total = 0    

    for sistema in lista:
        tempo_total += sistema[CHAVE_TEMPO]

    tempo_total = round(tempo_total, 0)       
              
    lista_resultados_ordenada = sorted(lista, key=lambda x: x[CHAVE_TEMPO])

    for dic_resultado in lista_resultados_ordenada:
        tempo_sistema = dic_resultado[CHAVE_TEMPO]
        percentual = (tempo_sistema * 100) / tempo_total
        dic_resultado[CHAVE_PERCENTUAL] = round(percentual, 0)    
    
    if tempo_total > 60:
        tempo = f'{round(tempo_total//60, 2)} minutos'    
    else:
        tempo = f'{tempo_total} segundos'    

    lista_resultados_ordenada.insert(0, {CHAVE_TEMPO_TOTAL: str(tempo)})    

    #print(f'Tempo: {tempo}')
    return lista_resultados_ordenada


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
        #dicionario_resultado[CHAVE_PERCENTUAL] = dicionario_execucao[CHAVE_PERCENTUAL]

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

        if (tempo_ultima_execucao > 0):
            tempo_alerta_percentual = tempo_ultima_execucao + round(tempo_ultima_execucao * PERCENTUAL_TEMPO_LIMITE / 100, 0)
            if  (total_segundos > tempo_alerta_percentual):
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

with ThreadPoolExecutor(max_workers=1) as execucao_pesados, ThreadPoolExecutor(max_workers=3) as execucao_leves,      ThreadPoolExecutor(max_workers=1) as execucao_medios:
    
    if len(lista_executaveis_pesados):
        for sistema_pesado in lista_executaveis_pesados:
            tarefa_pesados = partial(executar_arquivo_bat, sistema_pesado)
            execucao_pesados.submit(tarefa_pesados)        

    if len(lista_executaveis_leves) > 0:
        for sistema_leve in lista_executaveis_leves:
            tarefa_leves = partial(executar_arquivo_bat, sistema_leve)
            execucao_leves.submit(tarefa_leves)    

    execucao_leves.shutdown(wait=True) 

    if len(lista_executaveis_medios) > 0:
        for sistema_medio in lista_executaveis_medios:
            tarefa_medios = partial(executar_arquivo_bat, sistema_medio)
            execucao_medios.submit(tarefa_medios)  

execucao_pesados.shutdown(wait=True)
execucao_medios.shutdown(wait=True)

# os.system('cls')

hora_fim = datetime.now()

tempo_total_segundos = (hora_fim - hora_inicio).total_seconds()

lista_resultados_ordenada = configurar_lista(lista_resultados)

for resultado in lista_resultados_ordenada:    
    print(resultado)

with open(CAMINHO_RESULTADO_JSON, 'w') as arquivo:
    json.dump(lista_resultados_ordenada, arquivo, indent=4)
