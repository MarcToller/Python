import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QStandardItemModel, QStandardItem
from formPrincipal import Ui_formPrincipal
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt 


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
        self.model.setHorizontalHeaderLabels(["Nome", "Imagem"])
        self.populate_table()

    def populate_table(self):
        for row in range(5):
            name_item = QStandardItem(f"Item {row + 1}")

            # Crie um item com um widget personalizado (ImageLabel) para exibir a imagem
            image_item = QStandardItem()
            image_widget = ImageLabel(str("C:\\Users\\Toller\\Desktop\\QUADRADO.png"))
            self.tableViewTodos.setIndexWidget(image_item.index(), image_widget)
            self.model.appendRow([name_item, image_item])
    
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
