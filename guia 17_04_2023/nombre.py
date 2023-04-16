import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.lista_personas = []
        self.initUI()

    def initUI(self):
        self.lbl_nombre = QLabel('Nombre:', self)
        self.lbl_apellido = QLabel('Apellido:', self)
        self.txt_nombre = QLineEdit(self)
        self.txt_apellido = QLineEdit(self)

        self.btn_crear_persona = QPushButton('Crear persona', self)
        self.btn_crear_persona.clicked.connect(self.crear_persona)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl_nombre)
        vbox.addWidget(self.txt_nombre)
        vbox.addWidget(self.lbl_apellido)
        vbox.addWidget(self.txt_apellido)
        vbox.addWidget(self.btn_crear_persona)

        self.setLayout(vbox)

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Listado de Personas')
        self.show()

    def crear_persona(self):
        nombre = self.txt_nombre.text()
        apellido = self.txt_apellido.text()

        persona = Persona(nombre, apellido)
        self.lista_personas.append(persona)

        self.txt_nombre.clear()
        self.txt_apellido.clear()

        print('Listado de personas:')
        for persona in self.lista_personas:
            print(f'{persona.nombre} {persona.apellido}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec())
