# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

class MinhaClasseWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela bonita')

        self.botao1 = self.fazer_botao('Botão 1')
        self.botao1.clicked.connect(self.slot_marcou_nao_marcou)

        self.botao2 = self.fazer_botao('Botão 2')
        
        self.botao3 = self.fazer_botao('Botão 3')        

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)  


        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

        # menuBar
        self.menu = self.menuBar()
        self.menu_principal = self.menu.addMenu('Menu Principal')

        self.sub_menu1 = self.menu_principal.addAction('Sub Menu 1')
        self.sub_menu1.triggered.connect(self.slot_example) 


        self.sub_menu2 = self.menu_principal.addAction('Sub Menu 2')
        self.sub_menu2.setCheckable(True)  ## menu de marcar/desmarcar é uma ação de marcar e desmarcar
        ## para saber se marcou ou desmarcou, ou seja o evento usamos:
        self.sub_menu2.toggled.connect(self.slot_marcou_nao_marcou)

        ## neste caso o hovered não tem parametro como no toggled (true/false) então temos que passar um slot que adia a execução da função, o mesmo que foi feito no lambda acima mas desta vez sem usar lambda:
        self.sub_menu2.hovered.connect(self.slot_marcou_nao_marcou)        


    @Slot()
    def slot_example(self):
        self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def slot_marcou_nao_marcou(self):
        print('Marcou?', self.sub_menu2.isChecked())

    def fazer_botao(self, TextoBotao):
        btn = QPushButton(TextoBotao)
        btn.setStyleSheet('font-size: 20px;')
        return btn



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MinhaClasseWindow()
    window.show()
    app.exec()  # O loop da aplicação