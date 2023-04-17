from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Ingrese una fruta:')
        self.txtFruta = QLineEdit()
        self.btnAgregar = QPushButton('Agregar')
        self.btnAgregar.clicked.connect(self.agregarFruta)
        self.lblListado = QLabel('Frutas agregadas:')
        self.txtListado = QLabel()

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl)
        vbox.addWidget(self.txtFruta)
        hbox = QHBoxLayout()
        hbox.addWidget(self.btnAgregar)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addWidget(self.lblListado)
        vbox.addWidget(self.txtListado)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.frutas = []

    def agregarFruta(self):
        fruta = self.txtFruta.text()
        if fruta:
            self.frutas.append(fruta)
            self.txtFruta.clear()
            self.txtListado.setText('\n'.join(self.frutas))

if __name__ == '__main__':
    app = QApplication([])
    window = Ventana()
    window.show()
    app.exec()
