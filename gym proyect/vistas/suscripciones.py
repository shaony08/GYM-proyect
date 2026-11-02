#import sys
from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton
from conexion.conexion import clientes
from conexion.conexion import buscar_cliente

class Suscripciones(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clientes")
        layout = QVBoxLayout()
        
        #botones para buscar clientes
        self.line_buscar_cliente = QLineEdit()
        self.line_buscar_cliente.setPlaceholderText("Ingrese el nombre del cliente")
        self.btn_buscar = QPushButton("Buscar")
        layout.addWidget(self.line_buscar_cliente)
        layout.addWidget(self.btn_buscar)
        #hace la tabla de los clientes
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(6)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido", "Telefono", "Inicio de suscripción", "Vencimiento de suscripción"])
        #agregamos los widgets al layout
        layout.addWidget(self.line_buscar_cliente)
        layout.addWidget(self.btn_buscar)
        layout.addWidget(self.tabla)
        self.setLayout(layout)

        self.cargar_clientes()
        self.btn_buscar.clicked.connect(self.buscar_clientes)

    def cargar_clientes(self):
        datos = clientes()
        self.tabla.setRowCount(len(datos))

        for fila, registro in enumerate(datos):
            for columna, valor in enumerate(registro):
                self.tabla.setItem(fila, columna, QTableWidgetItem(str(valor)))
                
    #def buscar_cliente(self):
        #nombre = self.line_buscar_cliente.text()
        #datos = buscar_cliente(nombre)
        #print(datos)
        #self.tabla.setRowCount(1)
        #if not datos:
            #print("No se encontró el registro")
            #self.tabla.setRowCount(0)
            #return
        #for columna, valor in enumerate(datos):
            #self.tabla.setItem(0, columna, QTableWidgetItem(str(valor)))
    def buscar_clientes(self):
                nombre = self.line_buscar_cliente.text().strip()
                if not nombre:
                    self.cargar_clientes()
                    return
                datos = buscar_cliente(nombre)
                if datos is None:
                    print("Cliente no encontrado")
                    return
                self.tabla.setRowCount(1)
                for columna, valor in enumerate(datos):
                    self.tabla.setItem(
                        0,
                        columna,
                        QTableWidgetItem(str(valor))
                    )