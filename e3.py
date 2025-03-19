class Vehiculo:
    def __init__(self, marca, modelo):  
        self.marca = marca
        self.modelo = modelo

    def description(self):
        return f"{self.marca}, Modelo: {self.modelo}"

class Coche(Vehiculo): ### se le hizo una correccion porque el metodo inin del vehiculo estaba mal definido 
    def __init__(self, marca, modelo):  
        super().__init__(marca, modelo)  
        self.ruedas = 4

mi_coche = Coche("Toyota", "Corolla") 
print(mi_coche.description())