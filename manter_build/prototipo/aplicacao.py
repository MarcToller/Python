import sys
from PySide6.QtWidgets import QApplication, QMainWindow 
from PySide6.QtGui import QStandardItemModel, QStandardItem
from formPrincipal import Ui_formPrincipal
from PySide6.QtGui import QPixmap, QPainter, QFont, QColor
from PySide6.QtCore import Qt 
import os
from utilsArquivos import CAMINHO_ARQUIVOS
import random


lista_arquivos_teste1 = ['arquivo1', 'arquivo2', 'arquivo3', 'arquivo4']
lista_arquivos_teste2 = ['arquivo5', 'arquivo6', 'arquivo7', 'arquivo8']

## https://chat.openai.com/c/f47170ca-41f2-408c-8343-c8176de03314

## Gerar executável: pyinstaller --name="manter_build" --noconfirm --noconsole --onefile --add-data='files;files' --clean aplicacao.py

class meuQStandardItem(QStandardItem):
    def __init__(self, text: str = ''):
        super().__init__(text)
        self.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
        self.setSelectable(False)   
        self.setTextAlignment(Qt.AlignCenter)     


class MainWindow(QMainWindow, Ui_formPrincipal): ## Ui_MainWindow foi a tela que ele criou 
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.model = QStandardItemModel()
        self.tableViewTodos.setModel(self.model)  

        self.criar_colunas()        
        self.adicionar_sistemas()        

        self.pushButtonIniciar.clicked.connect(self.editar_item_teste)

    def criar_colunas(self):
        header_sistema = QStandardItem("Sistema")
        header_tipo = QStandardItem("Tipo")              
        header_status = QStandardItem("Status")              
        header_resultado = QStandardItem("Resultado")              
        header_tempo = QStandardItem("Tempo") 
        font = QFont()
        font.setBold(True)

        header_sistema.setFont(font)
        header_tipo.setFont(font)
        header_status.setFont(font)
        header_resultado.setFont(font)
        header_tempo.setFont(font)

        header_sistema.setData(QColor(Qt.red), Qt.ForegroundRole)  # Cor da fonte para a coluna 1
        header_tipo.setData(QColor(Qt.blue), Qt.ForegroundRole)  # Cor da fonte para a coluna 2

        self.model.setHorizontalHeaderItem(0, header_sistema)
        self.model.setHorizontalHeaderItem(1, header_tipo)        
        self.model.setHorizontalHeaderItem(2, header_status)
        self.model.setHorizontalHeaderItem(3, header_resultado)        
        self.model.setHorizontalHeaderItem(4, header_tempo)

        for coluna in range(self.model.columnCount()):  
             if coluna == 3:
                  self.tableViewTodos.setColumnWidth(coluna, 65)            
             elif coluna == 0:
                  self.tableViewTodos.setColumnWidth(coluna, 119)                              


    def editar_item_teste(self):                 
        image_item = self.model.findItems('arquivo5', Qt.MatchFlag.MatchExactly)[0]       
        pixmap1 = QPixmap(os.path.join(CAMINHO_ARQUIVOS, 'cinza.png'))
        pixmap2 = QPixmap(os.path.join(CAMINHO_ARQUIVOS, 'azul.png'))
        pixmap3 = QPixmap(os.path.join(CAMINHO_ARQUIVOS, 'vermelho.png'))        

        width = pixmap1.width() + pixmap2.width() + pixmap3.width()
        height = max(pixmap1.height(), pixmap2.height(), pixmap3.height())
        combined_pixmap = QPixmap(width, height)
        combined_pixmap.fill(Qt.transparent)

        # Desenha as duas imagens na QPixmap combinada
        painter = QPainter(combined_pixmap)
        painter.drawPixmap(0, 0, pixmap1)
        painter.drawPixmap(0, pixmap1.height(), pixmap2)
        painter.drawPixmap(pixmap1.width(), 0, pixmap2)
        painter.drawPixmap(pixmap1.width() + pixmap2.width(), 0, pixmap3)
        painter.end() 

        image_item1 = meuQStandardItem()        
        image_item1.setData(combined_pixmap, Qt.DecorationRole)        
        self.model.setItem(image_item.index().row(), 3, image_item1)
        

    def adicionar_sistemas(self):
        lista_unificada = lista_arquivos_teste1 + lista_arquivos_teste2
        for arquivo in lista_unificada:
            nome_sistema = meuQStandardItem(arquivo)                        
            tempo = meuQStandardItem('0:00')                        
            status = meuQStandardItem('Parado')   
            tipo = meuQStandardItem('Pesado')  
            
            font = QFont()
            font.setBold(True)              
            nome_sistema.setFont(font)             

            self.model.appendRow([nome_sistema, 
                                  tipo, 
                                  status,                                   
                                  self.retorna_imagem(random.randint(1, 4)), 
                                  tempo])  
      
    def retorna_imagem(self, index)-> meuQStandardItem:
        nome_imagem = ''
        if index == 1:
            nome_imagem = 'verde'
        elif index == 2:
            nome_imagem = 'vermelho'
        elif index == 3:
            nome_imagem = 'amarelo'
        elif index == 4:
            nome_imagem = 'cinza'

        caminho_imagem = os.path.join(CAMINHO_ARQUIVOS, nome_imagem+'.png')

        image_item = meuQStandardItem()        
        pixmap1 = QPixmap(os.path.join(CAMINHO_ARQUIVOS, caminho_imagem))
        pixmap2 = QPixmap(os.path.join(CAMINHO_ARQUIVOS, 'verde.png'))
        pixmap3 = QPixmap(os.path.join(CAMINHO_ARQUIVOS, 'vermelho.png'))
        

        width = pixmap1.width() + pixmap2.width() + pixmap3.width()
        height = max(pixmap1.height(), pixmap2.height(), pixmap3.height())
        combined_pixmap = QPixmap(width, height)
        combined_pixmap.fill(Qt.transparent)

        # Desenha as duas imagens na QPixmap combinada
        painter = QPainter(combined_pixmap)
        painter.drawPixmap(0, 0, pixmap1)
        painter.drawPixmap(0, pixmap1.height(), pixmap2)
        painter.drawPixmap(pixmap1.width(), 0, pixmap2)
        painter.drawPixmap(pixmap1.width() + pixmap2.width(), 0, pixmap3)
        painter.end() 
        
        image_item.setData(combined_pixmap, Qt.DecorationRole)        

        return image_item
            
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()