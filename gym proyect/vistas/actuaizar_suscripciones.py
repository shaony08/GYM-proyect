from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton
from conexion.conexion import buscar_cliente

class ActualizarSuscripciones(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Actualizar Suscripciones")
        self.layout_boton_buscar = QHBoxLayout()
        self.layout_principal = QVBoxLayout()
        #layout para mostrar los datos del cliente en horizontal
        self.buscar_por_nombre = QLineEdit()
        self.buscar_por_nombre.setPlaceholderText("Ingrese el nombre del cliente")
        self.btn_buscar = QPushButton("Buscar")
        #
        self.monto_input = QLineEdit()
        self.tipo_pago_input = QLineEdit()
        self.tipo_suscripcion_input = QLineEdit()
        self.monto_input.setPlaceholderText("Monto")
        self.tipo_pago_input.setPlaceholderText("Tipo de pago") 
        self.tipo_suscripcion_input.setPlaceholderText("Tipo de suscripción") 
        #agregamos los layouts
        self.layout_boton_buscar.addWidget(self.buscar_por_nombre)
        self.layout_boton_buscar.addWidget(self.btn_buscar)
        self.layout_principal.addLayout(
            self.layout_boton_buscar
            )
        self.layout_principal.addWidget(self.monto_input)
        self.layout_principal.addWidget(self.tipo_pago_input)
        self.layout_principal.addWidget(self.tipo_suscripcion_input)
        self.setLayout(self.layout_principal)
        
        self.btn_realizar_pago = QPushButton("Realizar pago")
        self.layout_principal.addWidget(self.btn_realizar_pago)
        self.setLayout(self.layout_principal)
        
        self.btn_buscar.clicked.connect(self.buscar_clientes)
        
    def buscar_clientes(self):
        nombre = self.buscar_por_nombre.text()
        datos = buscar_cliente(nombre)
        print(f"Datos del cliente: {datos}")
        
        if datos:
            self.id_cliente = datos[0]
            self.tipo_suscripcion_input.setText(
                str(datos[2])
            )
