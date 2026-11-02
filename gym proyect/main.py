import sys
from PySide6.QtWidgets import QApplication
from vistas.ventana_principal import MainWindow as VentanaPrincipal

def main():
    """
    Inicializa el ciclo de vida de la aplicación y cede
    el control de ejecución al despachador de eventos (Event Loop).
    """
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()