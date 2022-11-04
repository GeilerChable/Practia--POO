from turtle import color


class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura="calientito", color="rojo"):
        self._llenar_tanque_de_agua(temperatura, color)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura, color):
        print(f"Llenando el tanque con agua {temperatura} de la lavadora de color {color}")

    def _añadir_jabon(self):
        print("Añadiendo jabón al agua")

    def _lavar(self):
        print("Lavando la ropita")
        
    def _centrifugar(self):
        print("Secar la ropa con el centrifugado")


if __name__=="__main__":
    lavadora=Lavadora()
    
    lavadora.lavar()

    Lavadora._llenar_tanque_de_agua(lavadora,'FRIOOOOOO', "rosado")
