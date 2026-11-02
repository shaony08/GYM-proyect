from PySide6.QtWidgets import QLabel, QTableWidget, QVBoxLayout, QWidget, QTableWidgetItem, QPushButton
from conexion.conexion import (obtener_maquinas_libres, obtener_maquinas_ocupadas, obtener_maquinas_fuera_servicio)

class Maquinas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Máquinas")

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Pantalla de Máquinas"))

        # Botones para filtrar máquinas
        self.btn_maquinas_libres = QPushButton("Máquinas Libres")
        self.btn_maquinas_ocupadas = QPushButton("Máquinas Ocupadas")
        self.btn_maquinas_fuera_servicio = QPushButton("Máquinas Fuera de Servicio")
        #agregamos los botones al layout
        layout.addWidget(self.btn_maquinas_libres)
        layout.addWidget(self.btn_maquinas_ocupadas)
        layout.addWidget(self.btn_maquinas_fuera_servicio)
        
        #tabla para mostrar las máquinas
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Estado", "Problema"])
        
        layout.addWidget(self.table)
        self.setLayout(layout)
        
        #conectamos los botones a sus funciones
        self.btn_maquinas_libres.clicked.connect(self.mostrar_libres)
        self.btn_maquinas_fuera_servicio.clicked.connect(self.mostrar_fuera_servicio)
        self.btn_maquinas_ocupadas.clicked.connect(self.mostrar_ocupadas)
        
    def mostrar_libres(self):
        datos = obtener_maquinas_libres()
        self.llenar_tabla(datos)
        
    def mostrar_ocupadas(self):
        datos = obtener_maquinas_ocupadas()
        self.llenar_tabla(datos)
            
    def mostrar_fuera_servicio(self):
        datos = obtener_maquinas_fuera_servicio()
        self.llenar_tabla(datos)
            
    def llenar_tabla(self,datos):
        self.table.setRowCount(len(datos))
        
        for fila, resgistro in enumerate(datos):
            for columna, valor in enumerate(resgistro):
                self.table.setItem(fila, columna, QTableWidgetItem(str(valor)))