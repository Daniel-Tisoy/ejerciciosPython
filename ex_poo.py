from math import pi

# --- Clase circulo ---


class Circulo():
    # --- Constructor ---
    ''' el constructor sirve para definir
    parametros básicos en programa'''

    def __init__(self, r=0.0):
        self.radio = r

    # --- Metodos ---
    # Asignar radio
    def asignar_radio(self, r):
        self.radio = r

    # Obtener radio
    def obtener_radio(self):
        return self.radio

    # Calcular perimetro
    def calcular_perimetro(self):
        per = 2*pi*self.radio
        return per

    # Calcular area
    def calcular_area(self):
        area = pi*(self.radio**2)
        return area
