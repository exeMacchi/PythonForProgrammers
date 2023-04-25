from abc import ABC, abstractmethod
import math

class GeometricFigure(ABC):
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
    
    @abstractmethod
    def calculate_area():
        pass
    
    @abstractmethod
    def calculate_perimeter():
        pass


class Triangle(GeometricFigure):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)
    
    def calculate_area(self):
        s = (self._side1 + self._side2 + self._side3) / 2
        area = math.sqrt(s * (s - self._side1) * 
                             (s - self._side2) * 
                             (s - self._side3))
        return area 
    
    def calculate_perimeter(self):
        return (self._side1 + self._side2 + self._side3)


class Rectangle(GeometricFigure):
    def __init__(self, height1, height2, base3, base4):
        super().__init__(height1, height2, base3)
        self.__base4 = base4

    def calculate_area(self):
        return self._side1 * self.__base4

    def calculate_perimeter(self):
        return 2 * (self._side1 + self.__base4)
    
    def mostrar_lados(self):
        print(self._side1, self._side2, self._side3, self.__base4)
        
