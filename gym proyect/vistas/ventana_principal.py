import sys
from PySide6.QtWidgets import QApplication, QTableWidgetItem, QWidget, QHBoxLayout, QMainWindow, QPushButton, QStackedWidget, QVBoxLayout, QWidget, QTableWidget

from vistas.entrenadores import Entrenadores
from vistas.maquinas import Maquinas
from vistas.registros import Registros
from vistas.suscripciones import Suscripciones
from conexion.conexion import registro_de_pagos
from vistas.actuaizar_suscripciones import ActualizarSuscripciones
from vistas.registrar_nuevos_clientes import RegistrarNuevosClientes

class VistaInicio(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resumen semanal")
        self.layout = QVBoxLayout(self)
        
        self.table_historial = QTableWidget()
        self.table_historial.setColumnCount(6)
        self.table_historial.setHorizontalHeaderLabels(
            ["ID", "Monto", "Tipo de pago", "Fecha", "ID del cliente", "Cliente"]
        )
        self.btn_registrar_pago = QPushButton("Registrar nuevo cliente")
        self.btn_actualizar_suscripcion = QPushButton("Actualizar suscripción")
        
        self.btn_actualizar_suscripcion.clicked.connect(self.abrir_actualizar_suscripcion)
        self.btn_registrar_pago.clicked.connect(self.abrir_registrar_pago)
        
        self.layout.addWidget(self.table_historial)
        self.layout.addWidget(self.btn_registrar_pago)
        self.layout.addWidget(self.btn_actualizar_suscripcion)
        
        self.cargar_historial()
    def cargar_historial(self):
        datos = registro_de_pagos()
        print("DATOS:", datos)
        print("TIPO:", type(datos))

        self.table_historial.setRowCount(len(datos))

        for fila, registro in enumerate(datos):
            print("REGISTRO:", registro)
            for columna, valor in enumerate(registro):
                self.table_historial.setItem(
                    fila,
                    columna,
                    QTableWidgetItem(str(valor))
                )
    def abrir_actualizar_suscripcion(self):
        self.actualizar_suscripcion_ventana = ActualizarSuscripciones()
        self.actualizar_suscripcion_ventana.show()

    def abrir_registrar_pago(self):
        self.registrar_pago_ventana = RegistrarNuevosClientes()
        self.registrar_pago_ventana.show()
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CENTRO DE GESTION DE GYM")
        #self.resize(1200, 700)

        container = QWidget()
        main_layout = QHBoxLayout(container)

        sidebar = QWidget()
        sidebar_layout = QVBoxLayout(sidebar)

        self.stacked = QStackedWidget()

        self.pages = [
            ("Inicio", VistaInicio()),
            ("Entrenadores", Entrenadores()),
            ("Máquinas", Maquinas()),
            ("Registros", Registros()),
            ("Suscripciones", Suscripciones()),
        ]

        for nombre, pagina in self.pages:
            self.stacked.addWidget(pagina)

            btn = QPushButton(nombre)
            btn.clicked.connect(lambda checked=False, n=nombre: self.mostrar_pantalla(n))
            sidebar_layout.addWidget(btn)

        main_layout.addWidget(sidebar, 1)
        main_layout.addWidget(self.stacked, 4)
        self.setCentralWidget(container)

    def mostrar_pantalla(self, nombre):
        for i, (titulo, _) in enumerate(self.pages):
            if titulo == nombre:
                self.stacked.setCurrentIndex(i)
                break