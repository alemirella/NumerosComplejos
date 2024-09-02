class NumeroComplejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        return f"{self.real} + {self.imaginario}i"

    def suma(self, otro):
        real = self.real + otro.real
        imaginario = self.imaginario + otro.imaginario
        return NumeroComplejo(real, imaginario)

    def resta(self, otro):
        real = self.real - otro.real
        imaginario = self.imaginario - otro.imaginario
        return NumeroComplejo(real, imaginario)

    def multiplicacion(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return NumeroComplejo(real, imaginario)

    def division(self, otro):
        divisor = otro.real**2 + otro.imaginario**2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / divisor
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / divisor
        return NumeroComplejo(real, imaginario)


# Ejemplo de uso
num1 = NumeroComplejo(4, 5)
num2 = NumeroComplejo(3, -2)

print("Número Complejo 1:", num1)
print("Número Complejo 2:", num2)

suma = num1.suma(num2)
print("Suma:", suma)

resta = num1.resta(num2)
print("Resta:", resta)

multiplicacion = num1.multiplicacion(num2)
print("Multiplicación:", multiplicacion)

division = num1.division(num2)
print("División:", division)
