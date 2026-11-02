from PySide6.QtCore import QDate
from PySide6.QtWidgets import QVBoxLayout, QWidget, QLineEdit, QComboBox, QPushButton, QDateEdit, QMessageBox
from conexion.conexion import insertar_cliente


class RegistrarNuevosClientes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registrar nuevos clientes")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # formularios
        self.nombre_input = QLineEdit()
        self.apellido_input = QLineEdit()
        self.telefono_input = QLineEdit()
        self.fecha_inicio_input = QDateEdit(QDate.currentDate())
        self.fecha_fin_input = QDateEdit(QDate.currentDate())

        self.nombre_input.setPlaceholderText("Nombre del cliente")
        self.apellido_input.setPlaceholderText("Apellido del cliente")
        self.telefono_input.setPlaceholderText("Teléfono del cliente")
        self.fecha_inicio_input.setDisplayFormat("yyyy-MM-dd")
        self.fecha_fin_input.setDisplayFormat("yyyy-MM-dd")

        # combobox para seleccionar la suscripcion
        self.cmb_suscripcion = QComboBox()
        self.cmb_suscripcion.addItem("Diario", 1)
        self.cmb_suscripcion.addItem("Semanal", 2)
        self.cmb_suscripcion.addItem("Quincenal", 3)
        self.cmb_suscripcion.addItem("Mensual", 4)
        self.cmb_suscripcion.addItem("VIP", 5)

        # boton para guardar los datos
        self.btn_guardar = QPushButton("Guardar")
        self.btn_guardar.clicked.connect(self.guardar_cliente)

        # agregamos los layouts
        self.layout.addWidget(self.nombre_input)
        self.layout.addWidget(self.apellido_input)
        self.layout.addWidget(self.telefono_input)
        self.layout.addWidget(self.fecha_inicio_input)
        self.layout.addWidget(self.fecha_fin_input)
        self.layout.addWidget(self.cmb_suscripcion)
        self.layout.addWidget(self.btn_guardar)

    def guardar_cliente(self):
        nombre = self.nombre_input.text().strip()
        apellido = self.apellido_input.text().strip()
        telefono = self.telefono_input.text().strip()
        fecha_inicio = self.fecha_inicio_input.date()
        fecha_fin = self.fecha_fin_input.date()
        id_suscripcion = self.cmb_suscripcion.currentData()

        if not nombre or not apellido or not telefono:
            QMessageBox.warning(self, "Datos incompletos", "Completa nombre, apellido y teléfono.")
            return

        if not telefono.isdigit() or len(telefono) < 8:
            QMessageBox.warning(self, "Teléfono inválido", "El teléfono debe tener solo números y al menos 8 dígitos.")
            return

        if fecha_fin < fecha_inicio:
            QMessageBox.warning(self, "Fechas inválidas", "La fecha de fin no puede ser menor que la de inicio.")
            return

        if id_suscripcion is None:
            QMessageBox.warning(self, "Suscripción requerida", "Selecciona una suscripción.")
            return

        fecha_inicio_str = fecha_inicio.toString("yyyy-MM-dd")
        fecha_fin_str = fecha_fin.toString("yyyy-MM-dd")

        insertar_cliente(nombre, apellido, telefono, fecha_inicio_str, fecha_fin_str, id_suscripcion)
        print(f"cliente guardado: {nombre} {apellido} fue guardado con exito")