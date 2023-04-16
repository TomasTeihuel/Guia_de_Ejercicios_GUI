import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import random

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Generador de números aleatorios')
        self.setGeometry(100, 100, 300, 200)
        self.boton = QPushButton('Generar número aleatorio', self)
        self.boton.setGeometry(50, 50, 200, 50)
        self.boton.clicked.connect(self.generar_numero_aleatorio)
        self.etiqueta = QLabel(self)
        self.etiqueta.setGeometry(50, 110, 200, 50)

    def generar_numero_aleatorio(self):
        numero_aleatorio = random.randint(1, 100)
        self.etiqueta.setText(f'Número aleatorio: {numero_aleatorio}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
