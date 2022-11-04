from tkinter import N


class CasillasLocas:
    def __init__(self,identificador, país):
        self._identificador=identificador
        self._país=país
        self._region=None

    @property

    def region(self):
        return self._region

    @region.setter

    def region(self,region):
        if region in self._país:
            self._region=region
        else:
            raise ValueError(f"la región {region} no es valida en la lista")

casilla=CasillasLocas(123, ["Ciudad de México", "Morelos", "Yucatán"])
print(casilla.region)
casilla.region="Yucatán"
print(casilla.region)
