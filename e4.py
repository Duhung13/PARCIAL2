#Cuando el Cliente, solicita un Estudio en la Unidad de Radiología, se le solicitan los siguientes datos: 
# Cédula de Identidad, Edad, Sexo, si pertenece a un seguro y el Tipo de Estudio (uno solo por cliente) que se le va a efectuar. 
# Si la persona pertenece a un seguro se le aplicará un descuento del 80%. 
# Si el cliente es Femenino y mayor de 70 años se le aplicará un 20% de descuento adicional. 
# Si es Masculino y mayor de 80 se le aplicará un 15% de descuento adicional.

class Cliente:
    def __init__(self, cedula, edad, sexo, seguro, tipo_estudio):
        self.cedula = cedula
        self.edad = edad
        self.sexo = sexo
        self.seguro = seguro
        self.tipo_estudio = tipo_estudio

    def calcular_monto(self):
        precios = {
            "Ultrasonido": 8.90,
            "Tomografía": 12.64,
            "Resonancia": 15.60
        }
        monto_base = precios[self.tipo_estudio] + (self.edad * 10)
        descuento = 0

        if self.seguro:
            descuento += 0.80
        if self.sexo == "Femenino" and self.edad > 70:
            descuento += 0.20
        elif self.sexo == "Masculino" and self.edad > 80:
            descuento += 0.15

        monto_neto = monto_base * (1 - descuento)
        return monto_neto

    def mostrar_recibo(self):
        monto_neto = self.calcular_monto()
        print(f"Cédula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Estudios: {self.tipo_estudio}")
        print(f"seguro:{self.seguro}")
        print(f"monto a pagar: {monto_neto:.2f}$")
def main():
    clientes = []
    estadisticas = {
        "Ultrasonido": {"cantidad": 0, "monto_total": 0},
        "Tomografía": {"cantidad": 0, "monto_total": 0},
        "Resonancia": {"cantidad": 0, "monto_total": 0}
    }

    while True:
        cedula = input("Ingrese la cédula de identidad: ")
        edad = int(input("Ingrese la edad: "))
        sexo = input("Ingrese el sexo (Femenino/Masculino): ")
        seguro = input("¿Pertenece a un seguro? (Sí/No): ").lower() == "sí"
        tipo_estudio = input("Ingrese el tipo de estudio (Ultrasonido/Tomografía/Resonancia): ")

        cliente = Cliente(cedula, edad, sexo, seguro, tipo_estudio)
        clientes.append(cliente)
        cliente.mostrar_recibo()

        estadisticas[tipo_estudio]["cantidad"] += 1
        estadisticas[tipo_estudio]["monto_total"] += cliente.calcular_monto()

        continuar = input("¿Desea ingresar otro cliente? (Sí/No): ").lower()
        if continuar != "sí":
            break

    print("\nEstadísticas del Día:")
    for estudio, datos in estadisticas.items():
        print(f"{estudio}: {datos['cantidad']} clientes, Monto Total: {datos['monto_total']:.2f} USD")

if __name__ == "__main__":
    main()