# Form implementation generated from reading ui file 'produto_form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_produto(object):
    def setupUi(self, produto):
        produto.setObjectName("produto")
        produto.resize(640, 480)
        produto.setMinimumSize(QtCore.QSize(640, 480))
        produto.setMaximumSize(QtCore.QSize(640, 480))
        self.frame_titulo = QtWidgets.QFrame(parent=produto)
        self.frame_titulo.setGeometry(QtCore.QRect(0, 0, 640, 80))
        self.frame_titulo.setMinimumSize(QtCore.QSize(640, 80))
        self.frame_titulo.setMaximumSize(QtCore.QSize(640, 80))
        self.frame_titulo.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.frame_titulo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_titulo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_titulo.setObjectName("frame_titulo")
        self.label_titulo = QtWidgets.QLabel(parent=self.frame_titulo)
        self.label_titulo.setGeometry(QtCore.QRect(0, 0, 640, 80))
        self.label_titulo.setMinimumSize(QtCore.QSize(640, 80))
        self.label_titulo.setMaximumSize(QtCore.QSize(640, 80))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_titulo.setObjectName("label_titulo")
        self.frame_rodape = QtWidgets.QFrame(parent=produto)
        self.frame_rodape.setGeometry(QtCore.QRect(0, 400, 640, 80))
        self.frame_rodape.setMinimumSize(QtCore.QSize(640, 80))
        self.frame_rodape.setMaximumSize(QtCore.QSize(640, 80))
        self.frame_rodape.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.frame_rodape.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_rodape.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_rodape.setObjectName("frame_rodape")
        self.label_msg = QtWidgets.QLabel(parent=self.frame_rodape)
        self.label_msg.setGeometry(QtCore.QRect(0, 0, 640, 80))
        self.label_msg.setMinimumSize(QtCore.QSize(640, 80))
        self.label_msg.setMaximumSize(QtCore.QSize(640, 80))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        self.label_msg.setFont(font)
        self.label_msg.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_msg.setText("")
        self.label_msg.setObjectName("label_msg")
        self.frame_corpo = QtWidgets.QFrame(parent=produto)
        self.frame_corpo.setGeometry(QtCore.QRect(0, 80, 640, 320))
        self.frame_corpo.setMinimumSize(QtCore.QSize(640, 320))
        self.frame_corpo.setMaximumSize(QtCore.QSize(640, 320))
        self.frame_corpo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_corpo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_corpo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_corpo.setObjectName("frame_corpo")
        self.lineEdit_nome = QtWidgets.QLineEdit(parent=self.frame_corpo)
        self.lineEdit_nome.setGeometry(QtCore.QRect(130, 70, 250, 20))
        self.lineEdit_nome.setMinimumSize(QtCore.QSize(250, 20))
        self.lineEdit_nome.setMaximumSize(QtCore.QSize(250, 20))
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.lineEdit_preco = QtWidgets.QLineEdit(parent=self.frame_corpo)
        self.lineEdit_preco.setGeometry(QtCore.QRect(130, 110, 100, 20))
        self.lineEdit_preco.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_preco.setMaximumSize(QtCore.QSize(100, 20))
        self.lineEdit_preco.setObjectName("lineEdit_preco")
        self.label = QtWidgets.QLabel(parent=self.frame_corpo)
        self.label.setGeometry(QtCore.QRect(70, 70, 49, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_corpo)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 49, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_buscar = QtWidgets.QLineEdit(parent=self.frame_corpo)
        self.lineEdit_buscar.setGeometry(QtCore.QRect(130, 20, 100, 20))
        self.lineEdit_buscar.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_buscar.setMaximumSize(QtCore.QSize(100, 20))
        self.lineEdit_buscar.setObjectName("lineEdit_buscar")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_corpo)
        self.label_3.setGeometry(QtCore.QRect(70, 20, 49, 16))
        self.label_3.setObjectName("label_3")
        self.bt_inserir = QtWidgets.QPushButton(parent=self.frame_corpo)
        self.bt_inserir.setGeometry(QtCore.QRect(70, 180, 90, 50))
        self.bt_inserir.setMinimumSize(QtCore.QSize(90, 50))
        self.bt_inserir.setMaximumSize(QtCore.QSize(90, 50))
        self.bt_inserir.setStyleSheet("background-color: rgb(220, 255, 174);")
        self.bt_inserir.setObjectName("bt_inserir")
        self.bt_editar = QtWidgets.QPushButton(parent=self.frame_corpo)
        self.bt_editar.setGeometry(QtCore.QRect(180, 180, 90, 50))
        self.bt_editar.setMinimumSize(QtCore.QSize(90, 50))
        self.bt_editar.setMaximumSize(QtCore.QSize(90, 50))
        self.bt_editar.setStyleSheet("background-color: rgb(255, 252, 207);")
        self.bt_editar.setObjectName("bt_editar")
        self.bt_buscar = QtWidgets.QPushButton(parent=self.frame_corpo)
        self.bt_buscar.setGeometry(QtCore.QRect(280, 180, 90, 50))
        self.bt_buscar.setMinimumSize(QtCore.QSize(90, 50))
        self.bt_buscar.setMaximumSize(QtCore.QSize(90, 50))
        self.bt_buscar.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.bt_buscar.setObjectName("bt_buscar")
        self.bt_excluir = QtWidgets.QPushButton(parent=self.frame_corpo)
        self.bt_excluir.setGeometry(QtCore.QRect(390, 180, 90, 50))
        self.bt_excluir.setMinimumSize(QtCore.QSize(90, 50))
        self.bt_excluir.setMaximumSize(QtCore.QSize(90, 50))
        self.bt_excluir.setStyleSheet("background-color: rgb(255, 116, 116);")
        self.bt_excluir.setObjectName("bt_excluir")

        self.retranslateUi(produto)
        QtCore.QMetaObject.connectSlotsByName(produto)

    def retranslateUi(self, produto):
        _translate = QtCore.QCoreApplication.translate
        produto.setWindowTitle(_translate("produto", "Form"))
        self.label_titulo.setText(_translate("produto", "Controle de Produtos"))
        self.label.setText(_translate("produto", "Nome:"))
        self.label_2.setText(_translate("produto", "Preço:"))
        self.label_3.setText(_translate("produto", "Buscar:"))
        self.bt_inserir.setText(_translate("produto", "Inserir"))
        self.bt_editar.setText(_translate("produto", "Editar"))
        self.bt_buscar.setText(_translate("produto", "Buscar"))
        self.bt_excluir.setText(_translate("produto", "Excluir"))
