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

        


