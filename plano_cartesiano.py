#El código es sobre el plano cartesiano y algunas de sus características, 
#como la ubicación en un cuadrante de un punto cartesiano, el vector entre dos puntos
#o la distancia entre dos puntos. 

import math

class Punto:

    def __init__(self, x=0, y=0):
        self.x= x
        self.y= y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def cuadrante(self):
        if self.x >0 and self.y>0:
            print(f'{self} pertenece al primer cuadrante')   
        elif self.x>0 and self.y<0:
            print(f'{self} pertenece al cuarto cuadrante')
        elif self.x<0 and self.y<0:
            print(f'{self} pertenece al tercer cuadrante')
        elif self.x<0 and self.y>0:
            print(f'{self} pertence al segundo cuadrante')
        elif self.x==0 and self.y!= 0:  
            print(f'{self} se encuentra sobre el eje y')
        elif self.x!= 0 and self.y== 0:
            print(f'{self} se encuentra sobre el eje x')
        else:
            print(f'{self} se encuentra en el origen')

    def vector(self, p):
        print(f'el vector que une los puntos {self} y {p} es igual a ({p.x-self.x}, {p.y-self.y})')

    def distancia(self, p):
        mod=math.sqrt((p.x-self.x)**2 + (p.y-self.y)**2)
        print(f'la distancia entre los puntos {self} y {p} es {mod}')
    
#def main():
a=Punto(x=5,y=5)
b=Punto(-5, 10)
a.cuadrante()
b.cuadrante()
a.vector(b)
a.distancia(b)
#if __name__=="__main__":
#    main()