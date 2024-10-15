from PyQt5.QtWidgets import ( # type: ignore
    QApplication, QWidget, QGridLayout, QLabel, QFrame, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QColor # type: ignore
from PyQt5.QtCore import Qt # type: ignore
import sys
import detector

class VentanaConPartes(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle("Ventana con Partes de Tamaño Determinado")
        self.showFullScreen()  # Mostrar a pantalla completa
        
        # Crear el layout de la rejilla
        grid_layout = QGridLayout()
        
        # Crear las partes de la ventana
        self.crear_parte_con_botones(grid_layout, 0, 0, 3, 3, "Parte 1", QColor(255, 0, 0))  # Rojo, ocupa 3x3
        self.crear_parte(grid_layout, 0, 3, 3, 2, "Parte 2", QColor(0, 255, 0))  # Verde, ocupa 3x2
        self.crear_parte(grid_layout, 3, 0, 2, 3, "Parte 3", QColor(0, 0, 255))  # Azul, ocupa 2x3
        self.crear_parte(grid_layout, 3, 3, 2, 2, "Parte 4", QColor(255, 255, 0))  # Amarillo, ocupa 2x2
        
        # Establecer el layout en la ventana
        self.setLayout(grid_layout)
    
    def crear_parte(self, layout, fila, columna, row_span, col_span, texto, color):
        # Crear un widget para cada parte con borde
        parte = QFrame()
        parte.setFrameShape(QFrame.Box)  # Establecer forma de marco de caja
        parte.setFrameShadow(QFrame.Sunken)  # Añadir sombra para que parezca un borde
        
        # Establecer el color de fondo
        parte.setStyleSheet(f"background-color: {color.name()};")
        
        # Crear una etiqueta para identificar la parte
        etiqueta = QLabel(texto, parte)
        etiqueta.setAlignment(Qt.AlignCenter)
        
        # Crear un layout para la parte y añadir la etiqueta
        parte_layout = QGridLayout()
        parte_layout.addWidget(etiqueta)
        parte.setLayout(parte_layout)
        
        # Añadir el widget al layout principal con el tamaño ajustado
        layout.addWidget(parte, fila, columna, row_span, col_span)
    
    def crear_parte_con_botones(self, layout, fila, columna, row_span, col_span, texto, color):
        # Crear un widget para la parte con borde
        parte = QFrame()
        parte.setFrameShape(QFrame.Box)  # Establecer forma de marco de caja
        parte.setFrameShadow(QFrame.Sunken)  # Añadir sombra para que parezca un borde
        
        # Establecer el color de fondo
        parte.setStyleSheet(f"background-color: {color.name()};")
        
        # Crear una etiqueta para identificar la parte
        etiqueta = QLabel(texto, parte)
        etiqueta.setAlignment(Qt.AlignCenter)
        
        # Crear los botones
        boton1 = QPushButton("Camara a color", parte)
        boton2 = QPushButton("Camara a binario", parte)
        
        # Conectar los botones a funciones
        boton1.clicked.connect(self.boton1_clicked)
        boton2.clicked.connect(self.boton2_clicked)
        
        # Crear un layout horizontal para los botones
        botones_layout = QHBoxLayout()
        botones_layout.addWidget(boton1)  # Añadir el primer botón
        botones_layout.addWidget(boton2)  # Añadir el segundo botón
        
        # Crear un layout vertical para la parte y añadir la etiqueta y los botones
        parte_layout = QVBoxLayout()
        parte_layout.addWidget(etiqueta)
        parte_layout.addLayout(botones_layout)  # Añadir los botones
        
        # Establecer el layout en la parte
        parte.setLayout(parte_layout)
        
        # Añadir el widget al layout principal con el tamaño ajustado
        layout.addWidget(parte, fila, columna, row_span, col_span)
    
    # Funciones para los botones
    def boton1_clicked(self):
        QMessageBox.information(self, "Botón 1", "Botón 1 fue presionado")

    def boton2_clicked(self):
        QMessageBox.information(self, "Botón 1", "Botón 1 fue presionado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaConPartes()
    ventana.show()
    sys.exit(app.exec_())
