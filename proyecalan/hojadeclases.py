class Dinero():
    def __init__(self,m,p,ppas):
        self.caja_inicial = m
        self.pago_cliente= p
        self.precio_pasajes = ppas
    
    def dinero_de_caja(self):
        asientos = self.asientos_larioja.count("o")
        total = self.caja_inicial + (asientos * self.precio_pasajes)
        return total


    def vuelto(self):
        vuelto = self.pago_cliente - self.precio_pasajes
        return vuelto

        


class Destinos():
    def__init__(self,destino,horario):
        Destino = destino
        Horario = horario
        checkbox = getattr(self,Horario,None)
        checkbox1 = getattr(self,Destino,None)
        if checkbox.isChecked() and checkbox1.isChecked():
            self.precio_pasaje_LR= 1800
            self.precio_pasajes.setText("$" + str(self.precio_pasaje_LR))
            i=0
            while i < len(self.asientos_larioja_m): #aca habilitamos y deshabilitamos botones

                #print(self.asientos_larioja_m[i])
                if self.asientos_larioja_m[i] == 'l':
                    self.b[i].setEnabled(True)
                    print (f'habilitando el asiento {i}')
                    
                else:
                    self.b[i].setEnabled(False)
                    print(f'desabilitando el asiento {i}')
                i = i + 1
            self.asi() 
    























while 

s



i = 0
while i < len(self.asientos_larioja_m):
    
    if self.asientos_larioja_m(i) == 'O':
        variable_name = 'checkBox_{i}'
        checkbox = getattr(self,variable_name,None) 
        if checkbox and checkbox.isChecked():
                #print(f'entrando al lugar de la lista {x}')
                self.asientos_larioja_m[i] = 'l'                                             
                checkbox.setEnabled(True)
                checkbox.setChecked(False)

    
    
    
    
    
    
    i += 1
    








