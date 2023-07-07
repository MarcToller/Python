#####  https://chat.openai.com/c/72b35f1a-7df4-4c8f-a447-2aa27bc3605d


from concurrent.futures import ThreadPoolExecutor
from functools import partial
import subprocess
import os
from datetime import datetime
from sistemas import *
import json
import shutil
import pyautogui



# listas = retorna_listas()
lista_execusao_sincrona = [] # listas[CHAVE_LISTA_SINCRONA]
lista_execusao_assincrona = lista_execusao_assincrona #listas[CHAVE_LISTA_ASSINCRONA]

hora_inicio = datetime.now()
lista_resultados = []
dicionario_sincrono = {}

shutil.rmtree(CAMINHO_PASTA_RESULTADO, ignore_errors=True)

if not os.path.exists(CAMINHO_PASTA_FALHA):
    os.makedirs(CAMINHO_PASTA_FALHA)

def status_saida(linha: str) -> str: 

    if str('-- FAILED') in str(linha):        
      return FALHA_BUILD_MENSAGEM
    elif FALHA_ASSINAR_D in str(linha):        
      return FALHA_ASSINAR_D
   
def executar_arquivo_bat(arquivo: str, tempo_limite: int = 0):
    dicionario_resultado = {}    
    try:     
        dicionario_resultado[CHAVE_SISTEMA] = arquivo
        dicionario_resultado[CHAVE_STATUS] = VALOR_SEM_FALHA 
        dicionario_resultado[CHAVE_TEMPO] = tempo_limite

        caminho_completo_bat = os.path.join(CAMINHO_PASTA_MANTER_BUILD, arquivo) 
        vArquivoTxt = os.path.splitext(arquivo)[0]+'.txt'  
        # vCaminhoArquivoSaida = os.path.join(CAMINHO_PASTA_FALHA, vArquivoTxt)                  

        vinicio = datetime.now()  
        print(f'Arquivo {arquivo} - Início: {vinicio}')

        processo = subprocess.Popen([caminho_completo_bat, '/NaoExecutar'], shell=True, cwd=CAMINHO_PASTA_MANTER_BUILD, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        for linha in processo.stdout:
            vStatus = status_saida(str(linha))
            if vStatus == FALHA_BUILD_MENSAGEM: 
                dicionario_resultado[CHAVE_STATUS] = vStatus
                print('terminate')
                processo.terminate()
            if vStatus == FALHA_ASSINAR_D: 
                dicionario_resultado[CHAVE_STATUS] = vStatus
                lista_resultados.append(dicionario_resultado)                    
                pyautogui.typewrite('goto :Fim')                 
                pyautogui.press('enter')                                 
                print(f'Deu "goto :Fim" na assinatura digital em {arquivo}')   
                break
                #processo.stdin.write('Goto :Fim')  
                #processo.communicate(b'\n')
                # processo.stdin.flush()
                #print(f'Deu "enter" na assinatura digital em {arquivo}')

        processo.wait()        
        
        vfinal = datetime.now() 
        print(f'Arquivo {arquivo} - final: {vfinal}') 
        
        vTotalSegundos = (vfinal - vinicio).total_seconds() 
        dicionario_resultado[CHAVE_TEMPO] = int(vTotalSegundos)
    except subprocess.CalledProcessError:
        print('except1')
        dicionario_resultado[CHAVE_STATUS] = 'Falha Desconhecida' 
        lista_resultados.append(dicionario_resultado)        
        return
    except subprocess.TimeoutExpired:        
        print('except2')
        return
    print(f'Arquivo {arquivo} - passou aqui') 

    # os.remove(vCaminhoArquivoSaida) # arquivos que passaram sem erros posso remover    
    lista_resultados.append(dicionario_resultado)           

# max_threads = 2
# sistemas = ()
if len(lista_execusao_assincrona) > 0:        
    with ThreadPoolExecutor(max_workers=3) as thread_pool_dois_sistemas:   
        for sistemas in lista_execusao_assincrona:            
            thread = partial(executar_arquivo_bat, sistemas.get(CHAVE_SISTEMA), sistemas.get(CHAVE_TEMPO_LIMITE))
            thread_pool_dois_sistemas.submit(thread)              
        
    thread_pool_dois_sistemas.shutdown(wait=True)


if len(lista_execusao_sincrona) > 0:
    with ThreadPoolExecutor(max_workers=1) as thread_pool_sistema_unico:   
        for sistema in lista_execusao_sincrona:
            #if sistema[CHAVE_STATUS] == FALHA_ASSINAR_D:
            #    print(f'Sistema: {sistema[CHAVE_SISTEMA]} executando novamente devido a {FALHA_ASSINAR_D}')
            thread = partial(executar_arquivo_bat, sistema[CHAVE_SISTEMA], sistema[CHAVE_TEMPO_LIMITE])
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
