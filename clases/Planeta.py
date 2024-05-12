class Planeta():
    """
    Clase que representa un planeta que orbita alrededor de una estrella. Un planeta es un cuerpo con masa menor que 13 Mjup (masas de Júpiter) que orbita una estrella. 
    Los atributos principales de un planeta son:
    
    Atributos:
    - nombre: El nombre del planeta.
    - estrella_protegida: La estrella alrededor de la cual orbita el planeta.
    - masaplanetaria: La masa del planeta en masas de Júpiter.
    - radio: El radio del planeta.
    - a: El semieje mayor de la órbita del planeta.
    - i: La inclinación de la órbita del planeta.
    - e: La excentricidad de la órbita del planeta.
    - periastron: El argumento del periastron del planeta.
    """
    def __init__(self, nombre, estrella_protegida, masaplanetaria, radio, a, i, e, periastron):
        self._nombre= nombre
        self._estrella_protegida= estrella_protegida
        self._masaplanetaria= masaplanetaria
        self._radio= radio
        self._a= a # semieje mayor
        self._i= i # inclinación de la orbita
        self._e= e # excentricidad
        self._w= periastron # argumento del periastron
        
    def periodo_rotacion_kepleriana(self,g):
        """
        Calcula y devuelve el periodo de rotación kepleriano del planeta.
        
        Parámetros:
        - g: La constante gravitacional.
        
        Retorna:
        - El periodo de rotación kepleriano del planeta como un número de punto flotante.
        """
        if self._masaplanetaria != 0 and self._a != 0:
            return float(2*np.pi*np.sqrt((self._a**3)/(g*self._masaplanetaria)))
        else:
            return 0
        
    def __str__(self):
        """
        Proporciona un str con la información del planeta
        Parámetros:
        - nombre: El nombre del planeta.
        - estrella_protegida: La estrella alrededor de la cual orbita el planeta.
        - masaplanetaria: La masa del planeta en masas de Júpiter.
        - radio: El radio del planeta.
        - a: El semieje mayor de la órbita del planeta.
        - i: La inclinación de la órbita del planeta.
        - e: La excentricidad de la órbita del planeta.
        - periastron: El argumento del periastron del planeta.
        returns:

        - una frase con los datos del planeta
        """
        return print("El planeta ", self._nombre," tiene una masa de "
                     ,self._masaplanetaria," [Mjup] con un radio de "
                     ,self._radio," orbita la estrella "
                     ,self._estrella_protegida," con un semieje mayor de ",self._a, " , una inclinación de ", self._i, " y una excentricidad de ", self._e, ". con un periastron de ",self._w)
    def diametro_pl(self):
        """
        Calcula el diametro del planeta

        Returns:
            -  Diametro del planeta
        """
        return self._radio*2
    
class PlanetaExoplanetario(Planeta):
    """
    Clase que representa un planeta exoplanetario, es decir, un planeta con una estrella anfitriona que no es el Sol.
    Hereda de la clase Planeta.
    """

    def metodo_descubrimiento(self, metodo):
        """
        Determina el método de primer descubrimiento del planeta exoplanetario, si por ”imagen directa”, ”velocidad radial” o ”transito”.

        Returns:
            str: El nombre del método de descubrimiento.

        """
        self.metodo_descubrimiento = metodo
        
        #Si el planeta es un tránsito, informa adicionalmente su parámetro de impacto 'b' :
        if self.metodo_descubrimiento == "Primary Transit":
            #Si el radio de la estrella es 0, no podemos calcular b, dado que se indefine.
            if (self._estrella_protegida)._radioestrella == 0:
                self.metodo_descubrimiento = "Transito, pero falta información para calcular el parámetro de impacto b"
                return self.metodo_descubrimiento
            #Si no es 0, entonces calculamos b
            else:
                b = self._a * np.cos(np.radians(self._i)) * (1 - self._e ** 2) / ((self._estrella_protegida)._radioestrella * (1 + self._e * np.sin(np.radians(self._w))))
                self.metodo_descubrimiento = f"Transito, con parámetro de impacto b: {b}"
                return self.metodo_descubrimiento
         
        #De no ser Tránsito, solamente devolvemos el nombre del método.
        elif self.metodo_descubrimiento == "Radial Velocity":
            self.metodo_descubrimiento = "Velocidad Radial"
            return self.metodo_descubrimiento
        
        elif self.metodo_descubrimiento == "Imaging":
            self.metodo_descubrimiento = "Imagen Directa"
            return self.metodo_descubrimiento
        
        else:
            self.metodo_descubrimiento = "Otro método"
            return self.metodo_descubrimiento
    
    def tatooine(self):
        """
        Determina si el planeta es similar a Tatooine, es decir, si orbita alrededor de una estrella binaria.

        Returns:
            str: Un mensaje indicando si el planeta es similar a Tatooine o no.
        """
        #Si el nombre indica más de una letra, en consecuencia, es similar a Tatooine, dado que esto nos indica que se encuentra orbitando 2 estrellas.
        if "A" and "B" in self._nombre:
            return "Es similar a Tatooine"
        #Si no, no es similar a Tatooine.
        else:
            return "No es similar a Tatooine, ya que solo cuenta con una estrella"
        
    
