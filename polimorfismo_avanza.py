class Persona:
    def __init__(self, nombre):
        self.nombre=nombre

    def avanza(self):
        print("ando caminando")

    
class Motocicleta(Persona):
    def __init__(self,nombre):
        super().__init__(nombre)

    def avanza(self):
        print("ando moviendome en motocicleta")


def main():
    persona=Persona("El primo")
    persona.avanza()
    motociclista=Motocicleta("Gargolin")
    motociclista.avanza()

if __name__=="__main__":
    main()