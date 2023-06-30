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
CHAVE_TEMPO_LIMITE = 'tempo_limite'
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
dicionario_sincrono = {}

shutil.rmtree(CAMINHO_PASTA_RESULTADO, ignore_errors=True)

if not os.path.exists(CAMINHO_PASTA_FALHA):
    os.makedirs(CAMINHO_PASTA_FALHA)

def status_arquivo_saida(nome_arquivo) -> str:     
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        if FALHA_BUILD in conteudo:
            return FALHA_BUILD_MENSAGEM
        elif FALHA_ASSINAR_D in conteudo:
            return FALHA_ASSINAR_D
        else:
            return FALHA_TIME_OUT

def executar_arquivo_bat(arquivo: str, tempo_limite: int):
    dicionario_resultado = {}    
    try:     
        dicionario_resultado[CHAVE_SISTEMA] = arquivo
        dicionario_resultado[CHAVE_STATUS] = VALOR_SEM_FALHA 
        dicionario_resultado[CHAVE_TEMPO] = tempo_limite

        caminho_completo_bat = os.path.join(CAMINHO_PASTA_MANTER_BUILD, arquivo) 
        vArquivoTxt = os.path.splitext(arquivo)[0]+'.txt'  
        vCaminhoArquivoSaida = os.path.join(CAMINHO_PASTA_FALHA, vArquivoTxt)          


        vinicio = datetime.now()  
        print(f'Arquivo {arquivo} - Início: {vinicio}')

        with open(vCaminhoArquivoSaida, 'w') as arquivo_saida:
            subprocess.run([caminho_completo_bat, '/NaoExecutar'], shell=True, cwd=CAMINHO_PASTA_MANTER_BUILD, timeout=tempo_limite, stdout=arquivo_saida)
        
        vfinal = datetime.now() 
        print(f'Arquivo {arquivo} - final: {vfinal}') 
        
        vTotalSegundos = (vfinal - vinicio).total_seconds() 
        dicionario_resultado[CHAVE_TEMPO] = int(vTotalSegundos)
    except subprocess.CalledProcessError:
        dicionario_resultado[CHAVE_STATUS] = 'Falha Desconhecida' 
        lista_resultados.append(dicionario_resultado)        
        return
    except subprocess.TimeoutExpired:    
        vStatus = status_arquivo_saida(vCaminhoArquivoSaida)

        ## se deu falha de assinatura digital ele vai executar novamente em instancia única abaixo
        if vStatus == FALHA_ASSINAR_D: 
            dicionario_sincrono[CHAVE_SISTEMA] = arquivo           
            dicionario_sincrono[CHAVE_TEMPO_LIMITE] = tempo_limite
            dicionario_sincrono[CHAVE_STATUS] = FALHA_ASSINAR_D 
            os.remove(vCaminhoArquivoSaida)
            lista_execusao_sincrona.append(dicionario_sincrono)
            return

        dicionario_resultado[CHAVE_STATUS] = vStatus
        lista_resultados.append(dicionario_resultado)                         
        return
        
    os.remove(vCaminhoArquivoSaida) # arquivos que passaram sem erros posso remover    
    lista_resultados.append(dicionario_resultado)           

# max_threads = 2
# sistemas = ()
for sistemas in lista_execusao_assincrona:            
    with ThreadPoolExecutor(max_workers=2) as thread_pool_dois_sistemas:   
        thread = partial(executar_arquivo_bat, sistemas[0].get(CHAVE_SISTEMA), sistemas[0].get(CHAVE_TEMPO_LIMITE))
        thread_pool_dois_sistemas.submit(thread)  

        if sistemas[1].get(CHAVE_SISTEMA):
            thread1 = partial(executar_arquivo_bat, sistemas[1].get(CHAVE_SISTEMA), sistemas[1].get(CHAVE_TEMPO_LIMITE))
            thread_pool_dois_sistemas.submit(thread1)            
        
    thread_pool_dois_sistemas.shutdown(wait=True)


if len(lista_execusao_sincrona) > 0:
    with ThreadPoolExecutor(max_workers=1) as thread_pool_sistema_unico:   
        for sistema in lista_execusao_sincrona:
            if dicionario_sincrono[CHAVE_STATUS] == FALHA_ASSINAR_D:
                print(f'Sistema {sistema[CHAVE_SISTEMA]} executando novamente devido a {FALHA_ASSINAR_D}')
            thread = partial(executar_arquivo_bat, sistema[CHAVE_SISTEMA], sistema[CHAVE_TEMPO_LIMITE])
            thread_pool_sistema_unico.submit(thread)  
        
    thread_pool_sistema_unico.shutdown(wait=True)


#os.system('cls')

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
