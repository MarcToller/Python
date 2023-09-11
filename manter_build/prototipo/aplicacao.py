import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from formPrincipal import Ui_formPrincipal


class MainWindow(QMainWindow, Ui_formPrincipal): ## Ui_MainWindow foi a tela que ele criou 
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

         # Encontrar o QListView com base no nome definido no Qt Designer
        self.listView = self.findChild(QListWidget, "listViewTodos")
        self.modeloListView = QStandardItemModel(self)
        self.modeloListView.setHorizontalHeaderLabels(["Coluna 1", "Coluna 2"])  # Defina os rótulos das colunas

        item1 = [QStandardItem("Item 1, Coluna 1"), QStandardItem("Item 1, Coluna 2")]
        item2 = [QStandardItem("Item 2, Coluna 1"), QStandardItem("Item 2, Coluna 2")]

        self.modeloListView.appendRow(item1)
        self.modeloListView.appendRow(item2)

        # Associar o modelo de dados ao QListView
        self.listViewTodos.setModel(self.modeloListView)    
    
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
