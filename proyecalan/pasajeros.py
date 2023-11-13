from PyQt6.QtWidgets import QApplication, QMainWindow 
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("PROYECALAN/unititled.ui", self)

        self.destino.toggled.connect(self.larioja)  
    def larioja (self):
        self.mediodia.toggled.connect(self.larioja)  
        if self.mediodia.isChecked():
            self.mediodia.stateChanged.connect(self.larioja)
            self.siesta.stateChanged.connect(self.larioja)
            self.noche.stateChanged.connect(self.larioja)


















app = QApplication([])
mi_ventana = MiVentana()
mi_ventana.show()
app.exec()