

#####  https://chat.openai.com/c/72b35f1a-7df4-4c8f-a447-2aa27bc3605d


import os
import subprocess
import threading
import time;


caminho_pasta = 'C:\Bin.dtc\Delphi\Atalhos\Executaveis\ManterBuild'


def teste(retorno: subprocess.Popen):

    while True:
        time.sleep(10)
        output, _ = retorno.communicate(timeout=20)
        if 'Pressione qualquer tecla para sair'.upper() in str(output).upper():
            retorno.terminate()

    
## thread = threading.Thread()



## for nome_arquivo in os.listdir(caminho_pasta):
##     if nome_arquivo[0] != '_':
#caminho_completo = os.path.join(caminho_pasta, 'ContabMillenium.bat')
#print(caminho_completo)
#retorno = subprocess.Popen('ContabMillenium.bat', shell=True, cwd=caminho_pasta, stdout=subprocess.PIPE, stderr=subprocess.PIPE)        

#retorno = subprocess.Popen(caminho_completo, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)        


#thread = threading.Thread(target=teste(retorno))
#thread.start()
#thread.join()
            
        



# for nome_arquivo in os.listdir(caminho_pasta):
#     if nome_arquivo[0] != '_':
#         caminho_completo = os.path.join(caminho_pasta, nome_arquivo)
#         #print(caminho_completo)
#         retorno = subprocess.Popen(nome_arquivo, shell=True, cwd=caminho_pasta)            
#         retorno.wait()
#         if retorno.returncode > 0:
#               
#             print('Erro de compilação em', nome_arquivo)

for nome_arquivo in os.listdir(caminho_pasta):
    if nome_arquivo == 'ContabMillenium.bat':
        if nome_arquivo[0] != '_':
            caminho_completo = os.path.join(caminho_pasta, nome_arquivo)
            #print(caminho_completo)
            try:
                #retorno = subprocess.call(nome_arquivo, shell=True, cwd=caminho_pasta) 
                retorno = subprocess.Popen(nome_arquivo, shell=True, cwd=caminho_pasta, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
                retorno.communicate()

                thread = threading.Thread(target=teste(retorno))
                thread.start()
                thread.join()

                #retorno.wait()
            except subprocess.CalledProcessError as e:            
                print('Erro de compilação em', nome_arquivo, e)
            


