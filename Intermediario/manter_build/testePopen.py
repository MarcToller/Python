import os
import subprocess
import pyautogui

# https://chat.openai.com/c/e0236e67-995b-4484-a95e-ab569e04612a
# https://chat.openai.com/c/e0236e67-995b-4484-a95e-ab569e04612a

PASTA = 'C:\Bin.Separado\Delphi\Atalhos\Executaveis'
CAMINHO = os.path.join(PASTA, 'WinLalur.bat')
ARQ_SAIDA = os.path.join(PASTA, 'saida.txt')

# pyautogui.press



processo = subprocess.Popen(CAMINHO, cwd=PASTA, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# Lê o arquivo de saída em tempo real
with open(ARQ_SAIDA, 'w') as arquivo_saida:
    for linha in processo.stdout:
        #linha_decodificada = linha.decode('utf-8').rstrip()  # Decodifica a linha e remove quebras de linha
        if str('-- FAILED') in str(linha):
            print('encontrou falha de build')
            processo.terminate()       

# Aguarda o término do processo
processo.wait()
print('Terminou')
