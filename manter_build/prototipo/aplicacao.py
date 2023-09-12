import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QStandardItemModel, QStandardItem
from formPrincipal import Ui_formPrincipal
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt 
import os
from utils import CAMINHO_ARQUIVOS


## https://chat.openai.com/c/f47170ca-41f2-408c-8343-c8176de03314

## Gerar executável: pyinstaller --name="manter_build" --noconfirm --noconsole --onefile --add-data='files;files' --clean aplicacao.py

class ImageLabel(QLabel):
    def __init__(self, image_path):
        super().__init__()
        pixmap = QPixmap(image_path)
        self.setPixmap(pixmap)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Alinhe a imagem no centro


class MainWindow(QMainWindow, Ui_formPrincipal): ## Ui_MainWindow foi a tela que ele criou 
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.model = QStandardItemModel()
        self.tableViewTodos.setModel(self.model)        

         # Adicione as colunas à tabela
        self.model.setHorizontalHeaderLabels(["Sistema", "Build", "Warning", "Hint"])
        self.populate_table()

    def populate_table(self):
      for row in range(4):
            name_item = QStandardItem(f"Item {row + 1}")

            # Crie um item com um QPixmap para exibir a imagem
            
            self.model.appendRow([name_item, self.retorna_imagem(row+1), self.retorna_imagem(row+1), self.retorna_imagem(row+1)])  

      self.tableViewTodos.setColumnWidth(1,60)
      self.tableViewTodos.setColumnWidth(2,60)
      self.tableViewTodos.setColumnWidth(3,60) 

      
    def retorna_imagem(self, index)-> QStandardItem:
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

        image_item = QStandardItem()
        pixmap = QPixmap(caminho_imagem)        
        image_item.setData(pixmap, Qt.DecorationRole)
        image_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
        
        return image_item
            
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()


# from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QStandardItemModel, QStandardItem
# import sys

# class MyApp(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Configurar a interface de usuário a partir do arquivo .ui criado no Qt Designer
#         self.setupUi()

#         # Criar um modelo de dados
#         self.model = QStandardItemModel(self)

#         # Associar o modelo de dados ao QListView
#         self.listView.setModel(self.model)

#         # Adicionar itens ao modelo de dados
#         item1 = QStandardItem("Item 1")
#         item2 = QStandardItem("Item 2")
#         self.model.appendRow(item1)
#         self.model.appendRow(item2)

#     def setupUi(self):
#         # Carregue a interface de usuário criada no Qt Designer
#         # Substitua 'sua_interface.ui' pelo nome do seu arquivo .ui
#         self.loadUi("sua_interface.ui")
        
#         # Encontre o QListView com base no nome definido no Qt Designer
#         self.listView = self.findChild(QListView, "listView")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyApp()
#     window.show()
#     sys.exit(app.exec_())
