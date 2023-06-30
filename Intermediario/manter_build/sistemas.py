lista_execusao_assincrona = [
    
    ({'sistema': '02_TestaFrameWorkDTC.bat',
     'tempo_limite': 300},

     {'sistema': 'XML_Importer.bat',
      'tempo_limite': 300,}),

    ({'sistema': '03_TestaWinContas.bat',
      'tempo_limite': 300},

    {'sistema': 'WinLalur.bat',
     'tempo_limite': 30,}), 

    ({'sistema': '04_TestaWinDP.bat',
      'tempo_limite': 300},

     {'sistema': '01_TestaDCComparaEstruturas.bat',
      'tempo_limite': 300,}), 
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