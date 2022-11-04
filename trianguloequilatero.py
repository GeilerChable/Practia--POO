class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

class Equilatero(Triangulo):
    def __init__(self, lado):
        super().__init__(lado,lado,lado)


if __name__=="__main__":
    triangulo=Triangulo(lado1=3, lado2=5, lado3=10)
    print(f"el perimetro del triángulo es {triangulo.perimetro()}")

    equilatero=Equilatero(lado=19)
    print(f"el perimetro del triángulo equilatero es: {equilatero.perimetro()}")