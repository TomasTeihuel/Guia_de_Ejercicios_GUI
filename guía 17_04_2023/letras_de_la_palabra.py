from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class PalabraWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cantidad de letras')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.palabra_label = QLabel('Ingrese una palabra:')
        layout.addWidget(self.palabra_label)

        self.palabra_edit = QLineEdit()
        self.palabra_edit.setPlaceholderText('Palabra')
        layout.addWidget(self.palabra_edit)

        self.cantidad_button = QPushButton('Cantidad de letras')
        self.cantidad_button.clicked.connect(self.mostrar_cantidad)
        layout.addWidget(self.cantidad_button)

    def mostrar_cantidad(self):
        palabra = self.palabra_edit.text()
        cantidad_letras = len(palabra)

        resultado_label = QLabel(f'La palabra tiene {cantidad_letras} letras.')
        layout = self.layout()
        layout.addWidget(resultado_label)

if __name__ == '__main__':
    app = QApplication([])
    window = PalabraWidget()
    window.show()
    app.exec()
