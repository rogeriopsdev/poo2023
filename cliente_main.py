import sys
from PyQt6.QtWidgets import  QApplication, QWidget
from PyQt6 import uic
from cliente_form import Ui_cliente

class Cliente_main(QWidget):
    def __init__(self):
        super().__init__()
        self.ui =uic.loadUi('cliente_form.ui',self)
        self.show()

if __name__=='__main__':
    janela = QApplication(sys.argv)
    app = Cliente_main()
    sys.exit(janela.exec())

