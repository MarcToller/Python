import sys
from PySide6.QtWidgets import QApplication, QPushButton
app = QApplication(sys.argv) ## argumentos que posso passar de fora da aplicação! 
botao1 = QPushButton('Botão 1') 
botao1.setStyleSheet('font-size: 40px;') 
botao1.show()  # Adiciona o widget na hierarquia e exibe a janela 


botao2 = QPushButton('Botão 2') 
botao2.setStyleSheet('font-size: 40px;') 
botao2.show()  # Adiciona o widget na hierarquia e exibe a janela

# Desta forma ele cria 2 janelas cada uma com um botão, ou seja, a aplicação gerencia essas "telas".. para abriri tudo numa tela só é necessário um outro componente, QMainWindow, um widget de layout suporta outros layouts dentro dele..

app.exec()  # O loop da aplicação