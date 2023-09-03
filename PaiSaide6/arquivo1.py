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

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela bonita')

botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

@Slot()
def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')

@Slot()
def slot_marcou_nao_marcou(marcou):
    print('Marcou?', marcou)

    
@Slot()
def executar_hovered(action):    
    def inner():
        slot_marcou_nao_marcou(action.isChecked())
    return inner

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar
menu = window.menuBar()
menu_principal = menu.addMenu('Menu Principal')

sub_menu1 = menu_principal.addAction('Sub Menu 1')
sub_menu1.triggered.connect(lambda: slot_example(status_bar)) ## aqui é como se eu passasse um OnClik, a lambda é como se fosse um método anônimo mas que chama outro método, o slot_example, adiamento de execução..


sub_menu2 = menu_principal.addAction('Sub Menu 2')
sub_menu2.setCheckable(True)  ## menu de marcar/desmarcar é uma ação de marcar e desmarcar
## para saber se marcou ou desmarcou, ou seja o evento usamos:
sub_menu2.toggled.connect(slot_marcou_nao_marcou)

## neste caso o hovered não tem parametro como no toggled (true/false) então temos que passar um slot que adia a execução da função, o mesmo que foi feito no lambda acima mas desta vez sem usar lambda:
sub_menu2.hovered.connect(executar_hovered(sub_menu2))

botao1.clicked.connect(executar_hovered(sub_menu2))



window.show()
app.exec()  # O loop da aplicação