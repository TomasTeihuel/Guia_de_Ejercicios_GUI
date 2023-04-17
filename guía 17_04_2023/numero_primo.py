from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class PrimoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Validador de números primos')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.numero_label = QLabel('Ingrese un número entero:')
        layout.addWidget(self.numero_label)

        self.numero_edit = QLineEdit()
        self.numero_edit.setPlaceholderText('Número entero')
        layout.addWidget(self.numero_edit)

        self.validar_button = QPushButton('Validar')
        self.validar_button.clicked.connect(self.validar_numero)
        layout.addWidget(self.validar_button)

    def validar_numero(self):
        numero = self.numero_edit.text()
        if not numero.isdigit():
            QMessageBox.warning(self, 'Error', 'Por favor ingrese un número entero.')
            return

        numero = int(numero)
        if numero < 2:
            QMessageBox.warning(self, 'Error', 'El número debe ser mayor o igual a 2.')
            return

        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                QMessageBox.warning(self, 'Resultado', f'{numero} no es un número primo.')
                return

        QMessageBox.information(self, 'Resultado', f'{numero} es un número primo.')

if __name__ == '__main__':
    app = QApplication([])
    window = PrimoWidget()
    window.show()
    app.exec()
