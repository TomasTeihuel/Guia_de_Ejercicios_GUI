from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Suma de números")

        self.num1_label = QLabel("Primer número:")
        self.num1_input = QLineEdit()
        self.num2_label = QLabel("Segundo número:")
        self.num2_input = QLineEdit()

        self.sumar_boton = QPushButton("Sumar")
        self.sumar_boton.clicked.connect(self.sumar_numeros)

        self.resultado_label = QLabel("")

        vbox = QVBoxLayout()
        vbox.addWidget(self.num1_label)
        vbox.addWidget(self.num1_input)
        vbox.addWidget(self.num2_label)
        vbox.addWidget(self.num2_input)
        vbox.addWidget(self.sumar_boton)
        vbox.addWidget(self.resultado_label)

        self.setLayout(vbox)

    def sumar_numeros(self):
        num1 = float(self.num1_input.text())
        num2 = float(self.num2_input.text())
        resultado = num1 + num2
        self.resultado_label.setText(f"El resultado es: {resultado}")

if __name__ == '__main__':
    app = QApplication([])
    window = ventana()
    window.show()
    app.exec()
