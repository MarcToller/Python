import os
import json

## "C:\Bin.Separado\Delphi\Fontes\Principal\Bats\AssinaturaDigital.bat" 


CHAVE_SISTEMA = 'sistema'
CHAVE_STATUS = 'status'
CHAVE_TEMPO = 'tempo_em_segundos'
CHAVE_INFORMACAO_ADICIONAL = 'informacao_adicional'
CHAVE_TEMPO_LIMITE = 'tempo_limite'
CHAVE_LISTA_SINCRONA = 'lista_sincrona'
CHAVE_LISTA_ASSINCRONA = 'lista_assincrona'
VALOR_SEM_FALHA = 'Build OK'

#CAMINHO_PASTA_MANTER_BUILD = os.path.join(os.environ['DELPHI_SVN'], 'Atalhos', 'Executaveis', 'ManterBuild')

CAMINHO_PASTA_MANTER_BUILD = 'D:\\Marcelo\\Cursos\\Python\\Intermediario\\manter_build\\arquivos_bat'


FALHA_BUILD = '-- FAILED'              
FALHA_BUILD_MENSAGEM = 'Falha no Build'
FALHA_ASSINAR_D = 'Falha ao tentar assinar digitalmente o projeto'
FALHA_TIME_OUT = 'TimeOut - Build interrompido propositalmente.'
CAMINHO_RESULTADO_JSON = os.path.join(CAMINHO_PASTA_MANTER_BUILD, 'resultado.json')
PERCENTUAL_TEMPO_LIMITE = 30


def retorna_listas() -> dict:    
    lista_sincrona = []
    lista_assincrona = []        
    result = {}
    adicionar_lista_assincrona = False

    if os.path.exists(CAMINHO_RESULTADO_JSON):
        with open(CAMINHO_RESULTADO_JSON, 'r') as arquivo:
            lista_arquivo = json.load(arquivo)
            for dic_arquivo in lista_arquivo:
              dic_assic = {}
              dic_assic[CHAVE_SISTEMA] = dic_arquivo[CHAVE_SISTEMA] 
              dic_assic[CHAVE_TEMPO_LIMITE] = dic_arquivo[CHAVE_TEMPO] + ((dic_arquivo[CHAVE_TEMPO] * PERCENTUAL_TEMPO_LIMITE) // 100 ) 
              lista_assincrona.append(dic_assic)

    arquivos = [arquivo 
                for arquivo in os.listdir(CAMINHO_PASTA_MANTER_BUILD)
                  if os.path.isfile(os.path.join(CAMINHO_PASTA_MANTER_BUILD, arquivo))]

    for nome_arquivo in arquivos:
        
        _, extensao = os.path.splitext(nome_arquivo)  

        if extensao == '.json':
            continue

        adicionar_lista_assincrona = True       
        if len(lista_assincrona) > 0:
            adicionar_lista_assincrona = not any(dicionario[CHAVE_SISTEMA] == nome_arquivo for dicionario in lista_assincrona)            

        if adicionar_lista_assincrona and (nome_arquivo[0] != '_'):        
            dic_sincrono = {}
            dic_sincrono[CHAVE_SISTEMA] = nome_arquivo
            dic_sincrono[CHAVE_TEMPO_LIMITE] = 0
            lista_sincrona.append(dic_sincrono)

    result[CHAVE_LISTA_ASSINCRONA] = lista_assincrona
    result[CHAVE_LISTA_SINCRONA] = lista_sincrona    
    return result


lista_execusao_assincrona = [
    
    {'sistema': '02_TestaFrameWorkDTC.bat',
     'tempo_limite': 300},
    
    {'sistema': '03_TestaWinContas.bat',
      'tempo_limite': 300},

    {'sistema': '04_TestaWinDP.bat',
      'tempo_limite': 300},

    {'sistema': '01_TestaDCComparaEstruturas.bat',
      'tempo_limite': 300,}, 
      
    {'sistema': '05_TestaContabMillenium.bat',
      'tempo_limite': 300},

    {'sistema': '06_TestaDCComparaEstruturasImoveis.bat',
      'tempo_limite': 300,}, 

    {'sistema': 'XML_Importer.bat',
      'tempo_limite': 300,},

]     

xxxxx = [
    
    {'sistema': 'XML_Importer.bat',
      'tempo_limite': 300,},

    {'sistema': 'GestaCon.bat',
      'tempo_limite': 300,},       

    {'sistema': 'GestImov.bat',
      'tempo_limite': 300},

    {'sistema': 'GestImovServidor.bat',
      'tempo_limite': 300,},       
      
    {'sistema': 'WinLalur.bat',
     'tempo_limite': 30,}, 
]     




lista_execusao_assincrona2 = [
    
    {'sistema_1': '02_TestaFrameWorkDTC.bat',
     'timeout_1': 10,
     'sistema_2': 'XML_Importer.bat',
     'timeout_2': 10,},

    {'sistema_1': '03_TestaWinContas.bat',
     'timeout_1': 10,
     'sistema_2': 'WinLalur.bat',
     'timeout_2': 10,}, 

    {'sistema_1': '04_TestaWinDP.bat',
     'timeout_1': 10,
     'sistema_2': '01_TestaDCComparaEstruturas.bat',
     'timeout_2': 10,}, 
]     


#lista_arquivos_leves = ['02_TestaFrameWorkDTC.bat', '03_TestaWinContas.bat', '04_TestaWinDP.bat', '01_TestaDCComparaEstruturas.bat']
#lista_arquivos_pesados = ['XML_Importer.bat', 'WinLalur.bat']


lista_execusao_assincrona1 = [
    {'sistema_1': 'WinDP.bat',
     'timeout_1': 10,
     'sistema_2': '04_TestaWinDP.bat',
     'timeout_2': 10,},

    {'sistema_1': 'WinContas.bat',
     'timeout_1': 10,
     'sistema_2': '03_TestaWinContas.bat',
     'timeout_2': 10,},

    {'sistema_1': 'DataMoney.bat',
     'timeout_1': 10,
     'sistema_2': 'DCAgendadorTarefas.bat',
     'timeout_2': 10,},

    {'sistema_1': 'WinLivros.bat',
     'timeout_1': 10,
     'sistema_2': '02_TestaFrameWorkDTC.bat',
     'timeout_2': 10,},

    {'sistema_1': 'ContabMillenium.bat',
     'timeout_1': 10,
     'sistema_2': '05_TestaContabMillenium.bat',
     'timeout_2': 10,},

    {'sistema_1': 'WinCaixaNew.bat',
     'timeout_1': 10,
     'sistema_2': 'DCMentor.bat',
     'timeout_2': 10,},

    {'sistema_1': 'WinPatrimonio.bat',
     'timeout_1': 10,
     'sistema_2': 'NuvemDataCempro.bat',
     'timeout_2': 10,},
    
    {'sistema_1': 'XML_Importer.bat',
     'timeout_1': 10,
     'sistema_2': 'XML_ImporterSVC.bat',
     'timeout_2': 10,},
    
    {'sistema_1': 'DCComparaEstruturasImoveis.bat',
     'timeout_1': 10,
     'sistema_2': '06_TestaDCComparaEstruturasImoveis',
     'timeout_2': 10,},

    {'sistema_1': 'DCComparaEstruturas.bat',
     'timeout_1': 10,
     'sistema_2': '01_TestaDCComparaEstruturas.bat',
     'timeout_2': 10,},

    {'sistema_1': 'GestaCon.bat',
     'timeout_1': 10,
     'sistema_2': 'GestaConServidor.bat',
     'timeout_2': 10,},

    {'sistema_1': 'GestImov.bat',
     'timeout_1': 10,
     'sistema_2': 'GestImovServidor.bat',
     'timeout_2': 10,},

    {'sistema_1': 'WinLalur.bat',
     'timeout_1': 10,
     'sistema_2': '',
     'timeout_2': 10,},
]     
#print(*lista_sistemas1)