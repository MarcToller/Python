#####  https://chat.openai.com/c/72b35f1a-7df4-4c8f-a447-2aa27bc3605d


from concurrent.futures import ThreadPoolExecutor
from functools import partial
import subprocess
import os
from datetime import datetime
from sistemas import *
import json
import shutil
import psutil



# listas = retorna_listas()
lista_execusao_sincrona = [] # listas[CHAVE_LISTA_SINCRONA]
lista_execusao_assincrona = lista_execusao_assincrona #listas[CHAVE_LISTA_ASSINCRONA]

hora_inicio = datetime.now()
lista_resultados = []
dicionario_sincrono = {}
sistemas_assinatura_digital = []

shutil.rmtree(CAMINHO_PASTA_RESULTADO, ignore_errors=True)

if not os.path.exists(CAMINHO_PASTA_FALHA):
    os.makedirs(CAMINHO_PASTA_FALHA)

def status_saida(linha: str) -> str: 

    if str('-- FAILED') in str(linha):        
        return FALHA_BUILD_MENSAGEM
    elif FALHA_ASSINAR_D in str(linha):        
        return FALHA_ASSINAR_D
    elif (str('assinatura').lower() in str(linha).lower()) or (str('digital').lower() in str(linha).lower()):
        return 'Assinatura Digital'
    else:
        return ''    

def verificar_arquivo_em_execucao():
    arquivo_assinatura = 'AssinaturaDigital.bat'
    for proc in psutil.process_iter(['name']):
        try:
            process_name = proc.info['name']
            if process_name.lower() == arquivo_assinatura.lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False    
   
def executar_arquivo_bat(arquivo: str, tempo_limite: int = 0):
    dicionario_resultado = {}    
    try:     
        dicionario_resultado[CHAVE_SISTEMA] = arquivo
        dicionario_resultado[CHAVE_STATUS] = VALOR_SEM_FALHA 
        dicionario_resultado[CHAVE_TEMPO] = tempo_limite

        caminho_completo_bat = os.path.join(CAMINHO_PASTA_MANTER_BUILD, arquivo) 

        vinicio = datetime.now()  
        print(f'Arquivo {arquivo} - Início: {vinicio}')

        processo = subprocess.Popen([caminho_completo_bat, '/NaoExecutar'], shell=True, cwd=CAMINHO_PASTA_MANTER_BUILD, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        for linha in processo.stdout:
            vStatus = status_saida(str(linha))
            if vStatus == FALHA_BUILD_MENSAGEM: 
                dicionario_resultado[CHAVE_STATUS] = vStatus
                #print('terminate')
                sistemas_assinatura_digital.remove(arquivo)
                processo.terminate()
                break
            
        processo.wait()                
        vfinal = datetime.now() 
        print(f'Arquivo {arquivo} - final: {vfinal}') 
        
        vTotalSegundos = (vfinal - vinicio).total_seconds() 
        dicionario_resultado[CHAVE_TEMPO] = int(vTotalSegundos)
        if vStatus == FALHA_BUILD_MENSAGEM:
            return
    except:
        print('except1')
        dicionario_resultado[CHAVE_STATUS] = 'Falha Desconhecida' 
        lista_resultados.append(dicionario_resultado)        
        sistemas_assinatura_digital.remove(arquivo)
        return
        
    lista_resultados.append(dicionario_resultado)           

if len(lista_execusao_assincrona) > 0:        
    with ThreadPoolExecutor(max_workers=3) as thread_pool_dois_sistemas:   
        for arquivo_bat in lista_execusao_assincrona:  
            sistema = arquivo_bat.get(CHAVE_SISTEMA)  

            ## arquivo_bat.get(CHAVE_TEMPO_LIMITE) 
            thread = partial(executar_arquivo_bat, sistema, 0)
            thread_pool_dois_sistemas.submit(thread)            

        
    thread_pool_dois_sistemas.shutdown(wait=True)


if len(lista_execusao_sincrona) > 0:
    with ThreadPoolExecutor(max_workers=1) as thread_pool_sistema_unico:   
        for arquivo_bat in lista_execusao_sincrona:
            sistema = arquivo_bat.get(CHAVE_SISTEMA)         
            thread = partial(executar_arquivo_bat, sistema, 0)
            thread_pool_sistema_unico.submit(thread)  
        
    thread_pool_sistema_unico.shutdown(wait=True)


#os.system('cls')

hora_fim = datetime.now()
tempo_decorrido = (hora_fim - hora_inicio).total_seconds() // 60
print(f'Tempo: {tempo_decorrido} minutos')

lista_resultados_ordenada = sorted(lista_resultados, key=lambda x: x[CHAVE_TEMPO])

for resultado in lista_resultados_ordenada:    
    print(resultado)

with open(CAMINHO_RESULTADO_JSON, 'w') as arquivo:
    json.dump(lista_resultados_ordenada, arquivo, indent=4)
#print('Sistemas OK', listaOK)
#print('Falhas: ', listaErros)
