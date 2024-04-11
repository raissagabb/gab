class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def calcular_area(self):
        s = self.calcular_perimetro() / 2
        area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
        return area


triangulo = Triangulo(3, 4, 5)
print("Perímetro do triângulo:", triangulo.calcular_perimetro())
print("Área do triângulo:", triangulo.calcular_area())