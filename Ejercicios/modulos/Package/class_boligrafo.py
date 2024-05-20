class Boligrafo:
    #Constructor
    def __init__(self, grosor_punta:int, color:str):
        self.color = color
        self.grosor_punta = grosor_punta
        self.capacidad_tinta_maxima = 100
        self.cantidad_tinta = 80

#Método es una función. Referente a la clase.
    def escribir_texto(self, texto:str)->str|int:
        longitud = len(texto)
        if longitud > self.cantidad_tinta:
            retorno = "No hay tinta suficiente"

        else:
            self.cantidad_tinta -= longitud
            retorno = texto

        return retorno

    def recargar(self, cantidad:int):
        if (self.cantidad_tinta + cantidad) > self.capacidad_tinta_maxima:
            self.cantidad_tinta += cantidad
            sobrante = self.cantidad_tinta - self.capacidad_tinta_maxima

            self.cantidad_tinta -= sobrante

            return f"Se recargo la lapicera y sobro {sobrante}"
        else:
            self.cantidad_tinta += cantidad
            return self.cantidad_tinta




