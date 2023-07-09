import os
import json

## "C:\Bin.Separado\Delphi\Fontes\Principal\Bats\AssinaturaDigital.bat" 


CHAVE_SISTEMA = 'sistema'
CHAVE_STATUS = 'status'
CHAVE_TEMPO = 'tempo_em_segundos'
CHAVE_INFORMACAO_ADICIONAL = 'informacao_adicional'
CHAVE_TEMPO_LIMITE = 'tempo_limite'
CHAVE_LISTA_ARQUIVOS_PESADOS = 'arquivos_pesados'
CHAVE_LISTA_ARQUIVOS_LEVES = 'arquivos_leves'
CHAVE_LISTA_ARQUIVOS_MEDIOS = 'arquivos_medios'
VALOR_SEM_FALHA = 'Build OK'
CHAVE_PERCENTUAL = 'percentual'

#CAMINHO_PASTA_MANTER_BUILD = os.path.join(os.environ['DELPHI_SVN'], 'Atalhos', 'Executaveis', 'ManterBuild')

CAMINHO_PASTA_MANTER_BUILD = 'D:\\Marcelo\\Cursos\\Python\\Intermediario\\manter_build\\arquivos_bat'


FALHA_BUILD = '-- FAILED'              
FALHA_BUILD_MENSAGEM = 'Falha no Build'
FALHA_ASSINAR_D = 'Falha ao tentar assinar digitalmente o projeto'
FALHA_TIME_OUT = 'TimeOut - Build interrompido propositalmente.'
CAMINHO_RESULTADO_JSON = os.path.join(CAMINHO_PASTA_MANTER_BUILD, 'resultado.json')
PERCENTUAL_TEMPO_LIMITE = 30


def carregar_lista_json() -> list:
    
    resultado = []    
    
    if os.path.exists(CAMINHO_RESULTADO_JSON):
       with open(CAMINHO_RESULTADO_JSON, 'r') as arquivo:
           lista_json = json.load(arquivo)
           for dic_arquivo in lista_json:
             dic_resultado = {}
             dic_resultado[CHAVE_SISTEMA] = dic_arquivo[CHAVE_SISTEMA] 
             dic_resultado[CHAVE_TEMPO_LIMITE] = dic_arquivo[CHAVE_TEMPO]
             dic_resultado[CHAVE_PERCENTUAL] = dic_arquivo[CHAVE_PERCENTUAL]             
             #dic_resultado[CHAVE_TEMPO_LIMITE] = dic_arquivo[CHAVE_TEMPO] + ((dic_arquivo[CHAVE_TEMPO] * PERCENTUAL_TEMPO_LIMITE) // 100 ) 
             resultado.append(dic_resultado)        
    
    resultado.append(resultado)    

    return resultado

def carrega_arquivos_pasta_manter_build():
    resultado = []
    for arquivo in os.listdir(CAMINHO_PASTA_MANTER_BUILD):
        
        if os.path.isfile(os.path.join(CAMINHO_PASTA_MANTER_BUILD, arquivo)):
            nome, extensao = os.path.splitext(arquivo) 
            if (nome[0] == '_') or (extensao == '.json') or ('todos' in nome.lower()):
                continue
            resultado.append(arquivo)
    return resultado



def retorna_listas() -> dict:    
    result = {}    

    lista_pesados = []
    lista_leves = []        
    lista_medios = []            

    lista_arquivo_json = carregar_lista_json()
    lista_arquivos_pasta = carrega_arquivos_pasta_manter_build()     
    

    for nome_arquivo in lista_arquivos_pasta:                      

        dic_json = next((dicionario for dicionario in lista_arquivo_json if dicionario.get(CHAVE_SISTEMA) == nome_arquivo), None)        

        if not dic_json:        
            dic_pesados = {}
            dic_pesados[CHAVE_SISTEMA] = nome_arquivo
            dic_pesados[CHAVE_TEMPO_LIMITE] = 0            
            lista_pesados.append(dic_pesados)
        else: 
            percentual = dic_json[CHAVE_PERCENTUAL]

            if percentual <= 10:                  
                lista_leves.append(dic_json)
            elif percentual >= 11 and percentual <= 20:                  
                lista_medios.append(dic_json)
            else:                  
                lista_pesados.append(dic_json)                                 
            
    result[CHAVE_LISTA_ARQUIVOS_LEVES] = sorted(lista_leves, key=lambda x: x[CHAVE_TEMPO_LIMITE])
    result[CHAVE_LISTA_ARQUIVOS_PESADOS] = sorted(lista_pesados, key=lambda x: x[CHAVE_TEMPO_LIMITE], reverse=True)
    result[CHAVE_LISTA_ARQUIVOS_MEDIOS] = sorted(lista_medios, key=lambda x: x[CHAVE_TEMPO_LIMITE])
    return result


lista_pesados = [
  
    {'sistema': 'Pesado1.bat',
     'tempo_limite': 300},
    
    {'sistema': 'Pesado2.bat',
      'tempo_limite': 300},
]


lista_leves = [
  
    {'sistema': 'Leve1.bat',
     'tempo_limite': 300},
    
    {'sistema': 'Leve2.bat',
      'tempo_limite': 300},

    {'sistema': 'Leve3.bat',
     'tempo_limite': 300},
    
    {'sistema': 'Leve4.bat',
      'tempo_limite': 300},

    {'sistema': 'Leve5.bat',
      'tempo_limite': 300},

    {'sistema': 'Leve6.bat',
     'tempo_limite': 300},
    
    {'sistema': 'Leve7.bat',
      'tempo_limite': 300},
]


lista_medios = [
  
    {'sistema': 'Medio1.bat',
     'tempo_limite': 300},
    
    {'sistema': 'Medio2.bat',    
      'tempo_limite': 300},

    {'sistema': 'Medio3.bat',
      'tempo_limite': 300},

]





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