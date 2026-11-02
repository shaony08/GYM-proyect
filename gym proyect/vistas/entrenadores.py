from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton
from conexion.conexion import buscar_entrenador, obtener_entrenadores
#from conexion.conexion import buscar_entrenador

class Entrenadores(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Entrenadores")

        layout = QVBoxLayout()
        #botón para buscar entrenadores
        #self.btn_buscar = QPushButton("Buscar Entrenador")
        #self.btn_filtar = QPushButton("Filtrar Entrenadores")
        #layout.addWidget(self.btn_buscar)
        #layout.addWidget(self.btn_filtar)

        #self.btn_buscar.clicked.connect(self.buscar_entrenador)
        #self.btn_filtar.clicked.connect(self.filtrar_entrenadores)
        #boton para buscar entrenadores
        self.line_buscar_nombre = QLineEdit()
        self.line_buscar_nombre.setPlaceholderText("Ingrese el nombre del entrenador")
        self.btn_buscar = QPushButton("Buscar")
        #tabla de entrenadores
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Horario", "Contacto", "Pago"])
        layout.addWidget(self.tabla)
        layout.addWidget(self.line_buscar_nombre)
        layout.addWidget(self.btn_buscar)
        self.setLayout(layout)

        self.cargar_entrenadores()
        self.btn_buscar.clicked.connect(self.buscar_entrenador)

    #def buscar_entrenador(self):
    #    self.buscar_entrenador_ventana = BuscarEntrenador()
    #    self.buscar_entrenador_ventana.show()

    #def filtrar_entrenadores(self):
    #   print("Filtrar entrenadores")

    def cargar_entrenadores(self):
        datos = obtener_entrenadores()
        self.tabla.setRowCount(len(datos))

        for fila, registro in enumerate(datos):
            for columna, valor in enumerate(registro):
                self.tabla.setItem(fila, columna, QTableWidgetItem(str(valor)))
    
    #def buscar_entrenador(self):
        #nombre = self.line_buscar.text()
        #datos = buscar_entrenador(nombre)
        #print(datos)
        #self.tabla.setRowCount(1)
        #if not datos:
            #print("No se encontró el registro")
            #self.tabla.setRowCount(0)
            #return
        #for columna, valor in enumerate(datos):
            #self.tabla.setItem(0, columna, QTableWidgetItem(str(valor)))
    def buscar_entrenador(self):
        nombre = self.line_buscar_nombre.text().strip()
        if not nombre:
            self.cargar_entrenadores()
            return
        datos = buscar_entrenador(nombre)
        if datos is None:
            print("Entrenador no encontrado")
            return
        self.tabla.setRowCount(1)
        for columna, valor in enumerate(datos):
            self.tabla.setItem(
                0,
                columna,
                QTableWidgetItem(str(valor))
            )