from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class PalabraWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Palabra al revés')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.palabra_label = QLabel('Ingrese una palabra:')
        layout.addWidget(self.palabra_label)

        self.palabra_edit = QLineEdit()
        self.palabra_edit.setPlaceholderText('Palabra')
        layout.addWidget(self.palabra_edit)

        self.reversa_button = QPushButton('Al revés')
        self.reversa_button.clicked.connect(self.mostrar_reversa)
        layout.addWidget(self.reversa_button)

    def mostrar_reversa(self):
        palabra = self.palabra_edit.text()
        palabra_reversa = palabra[::-1]

        resultado_label = QLabel(f'Palabra al revés: {palabra_reversa}')
        layout = self.layout()
        layout.addWidget(resultado_label)

if __name__ == '__main__':
    app = QApplication([])
    window = PalabraWidget()
    window.show()
    app.exec()
