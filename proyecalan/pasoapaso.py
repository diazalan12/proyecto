from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6 import uic
#from hojadeclases import *
class Dinero():
    def __init__(self,m,p,ppas):
        self.caja_inicial = m
        self.pago_cliente= p
        self.precio_pasajes = ppas
    
    def dinero_de_caja(self,asientos):
        total = self.caja_inicial + (asientos * self.precio_pasajes)
        return total


    def vuelto(self,asientos):
        vuelto_cliente = self.pago_cliente - (self.precio_pasajes * int(asientos))
        return vuelto_cliente


class Vuelto_final(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("turned_f.ui", self)
    #def tt (self):
        
     #   texto = str(self.n_asiento.text())
      #  return texto


class MiDialogo(QDialog):
    def __init__(self,  asientos_larioja):
        super().__init__()
        uic.loadUi("ventana_eliminar.ui", self)
        # Obtén referencias a los checkboxes del archivo UI
        self.checkboxes = [self.disponibilidad_0,self.disponibilidad_1, self.disponibilidad_2,self.disponibilidad_3, self.disponibilidad_4]
        
        # Configura el estado inicial de los checkboxes según los asientos_larioja
        for i in range(len(self.checkboxes)):
            checkbox = self.checkboxes[i]
            estado = asientos_larioja[i]
            checkbox.setEnabled(estado == 'o')  # Invertir el estado

    def obtener_asientos_seleccionados(self):
        return [1 if checkbox.isChecked() else 0 for checkbox in self.checkboxes]

    def tt (self):
        
        texto = str(self.n_asiento.text())
        return texto
    def marcar(self):
        self.disponinilidad1.setEnabled(False)


class Caja_i(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_caja_inicial.ui", self)
        

    
    
class Dialogo_vuelto(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("window_turned.ui", self)
class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pasoapaso.ui" , self)
        #botones y conectividades:
        self.boton_reserva.clicked.connect(self.reserva)
        self.button.clicked.connect(self.mostrar_asientos)
        self.button_deleted.clicked.connect(self.ventana_eliminar) 
        #self.button_boxcash.clicked.connect(self.monto)
        self.b = [self.disponibilidad_0,self.disponibilidad_1, self.disponibilidad_2,self.disponibilidad_3, self.disponibilidad_4]
        ventana_caja = Caja_i()
        ventana_caja.exec()
        self.CajaInicial = ventana_caja.lineDinero.text()
        self.box_cash.setText("caja inicial: " + str(self.CajaInicial))
        for i in range(5):
            self.b[i].setEnabled(False)
    #listas a usar:
    asientos = ['g'] * 5
    asientos_larioja = ['l']*5
    
   
   
   
   
   #ACA ES EL TEMA DE LOS ASIENTOS      
    def mostrar_asientos(self):
        #La Rioja
        if self.radioButton_2.isChecked() and self.radioButton.isChecked(): #esta parte es donde chequea que destino y horario estamos seleccionando
            self.precio_pasaje_LR= 1800
            self.precio_pasajes.setText("$" + str(self.precio_pasaje_LR))
            i=0
            while i < len(self.asientos_larioja): #aca habilitamos y deshabilitamos botones

                #print(self.asientos_larioja[i])
                if self.asientos_larioja[i] == 'l':
                    self.b[i].setEnabled(True)
                    #print (f'habilitando el asiento {i}')
                    
                else:
                    self.b[i].setEnabled(False)
                    #print(f'desabilitando el asiento {i}')
                i = i + 1
            self.asi() 
        #mendoza
        elif self.radioButton_3.isChecked() and self.radioButton.isChecked():
            self.precio_pasaje_mendoza
            i=0
            while i < len(self.asientos):
                #print(self.asientos[i])
                if self.asientos[i] == 'g':
                    self.b[i].setEnabled(True)
                    #print (f'habilitando el asiento {i}')
                else:
                    self.b[i].setEnabled(False)
                    #print(f'desabilitando el asiento {i}')
    
            
                
                i = i + 1
            
    #RESERVA DE ASIENTOS

    def reserva(self):
        x = 0 
        cnt_asientos = 0 
        
        #bucle para verificar que checkbox estan seleccionados y no ir verificando uno por uno
        while x < len(self.asientos_larioja):  
            variable_name = f'disponibilidad_{x}'
            checkbox = getattr(self, variable_name, None) #esto comprueba que el asiento 'disponibilidad_1 o disponibilidad_2 3 4 etc' este disponible
            
            
            if checkbox and checkbox.isChecked():
                #print(f'entrando al lugar de la lista {x}')
                self.asientos_larioja[x] = 'o'                                             
                checkbox.setEnabled(False)
                checkbox.setChecked(False)
                cnt_asientos += 1
                #print(f'El checkbox {variable_name} está marcado')
                print (cnt_asientos)
            
            x = x + 1
        
        window = Dialogo_vuelto()
        if (window.exec()):
            pago_cliente= int(window.line_pago.text())
            dinero = Dinero(int(self.CajaInicial),pago_cliente,self.precio_pasaje_LR)
            self.Vuelto = dinero.vuelto(cnt_asientos)
        #    print(self.Vuelto)
            window_turned =  Vuelto_final()
            window_turned.vuelto_cliente_f.setText('$' + str(self.Vuelto))
            if (window_turned.exec()):

                window_turned.show()                    
        dinero_general = dinero.dinero_de_caja(cnt_asientos)
        self.box_cash.setText(str(dinero_general))
        self.asi()    
    
    
    def ventana_eliminar(self):
        # Crear una instancia de MiDialogo con la lista invertida
        dialogo = MiDialogo(self.asientos_larioja)

        # Si se acepta el diálogo
        if dialogo.exec():
            asientos_seleccionados = dialogo.obtener_asientos_seleccionados()

            # Actualizar la disponibilidad en la ventana principal
            for i in range(len(asientos_seleccionados)):
                if asientos_seleccionados[i]:
                    self.asientos_larioja[i] = 'l'  # Invertir el estado
                    self.b[i].setEnabled(True) # Habilitar el botón

    
    def asi(self):
        b = self.asientos_larioja.count("l")
        self.asientoslibres.setText('dinero:$ '+str(b))






app= QApplication([])
mi_ventana = MiVentana()
mi_ventana.show()
app.exec()

#  def lista_asientos_larioja(self):
#        i=0
#          while i < len(self.asientos_larioja):
#               if self.asientos_larioja[i] == 'l':
#                    self.b[i].setEnabled(True)
                #else:
                #    self.b[i].setEnabled(False)
                #i = i + 1
    #def monto (self):
     #   monto_inicial = self.lineEdit_boxcash.text()
      #  self.box_cash.setText("CAJA: "+ "$" +str(monto_inicial))
       # self.button_boxcash.setEnabled(False)
        #self.lineEdit_boxcash.setEnabled(False)
        #return monto_inicial