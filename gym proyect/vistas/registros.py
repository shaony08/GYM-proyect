from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton
from conexion.conexion import obtener_asistencias
from conexion.conexion import buscar_asistencias

class Registros(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registro de clientes")

        layout = QVBoxLayout()
        #botón para buscar entrenadores
        '''Todavia falt cambiar el buscar por filtar y que se pueda buscar por fecha, hora, cliente id y nombre del cliente'''
        self.line_buscar_asistencias = QLineEdit()
        self.line_buscar_asistencias.setPlaceholderText("Ingrese el nombre del cliente")
        self.btn_buscar = QPushButton("Buscar")
        #hace la tabla de entrenadores
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["ID", "Fecha", "Hora de entrada", "Cliente ID", "Cliente"])
        layout.addWidget(self.line_buscar_asistencias)
        layout.addWidget(self.btn_buscar)
        layout.addWidget(self.tabla)
        self.setLayout(layout)

        self.cargar_asistencias()
        self.btn_buscar.clicked.connect(self.buscar_asistencias)

    #def buscar_asistencias(self):
        #nombre = self.line_buscar_asistencias.text()
        #datos = buscar_asistencias(nombre)
        #print(datos)
        #self.tabla.setRowCount(1)
        #for columna, valor in enumerate(datos):
            #self.tabla.setItem(0, columna, QTableWidgetItem(str(valor)))
    def buscar_asistencias(self):
            nombre = self.line_buscar_asistencias.text().strip()
            if not nombre:
                self.cargar_asistencias()
                return
            datos = buscar_asistencias(nombre)
            if datos is None:
                print("Asistencia no encontrada")
                return
            self.tabla.setRowCount(1)
            for columna, valor in enumerate(datos):
                self.tabla.setItem(
                    0,
                    columna,
                    QTableWidgetItem(str(valor))
                )

    def cargar_asistencias(self):
        datos = obtener_asistencias()
        self.tabla.setRowCount(len(datos))

        for fila, registro in enumerate(datos):
            for columna, valor in enumerate(registro):
                self.tabla.setItem(fila, columna, QTableWidgetItem(str(valor)))