import random
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QColor

class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle("BotÃ³n colorido")

        self.boton = QPushButton("Presiona", self)
        self.boton.setGeometry(100, 80, 100, 50)
        self.boton.clicked.connect(self.cambiar_color)

    def cambiar_color(self):
        color = QColor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.boton.setStyleSheet("background-color: {}".format(color.name()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())