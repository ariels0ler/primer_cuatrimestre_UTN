
from Package.class_boligrafo import *

primer_boligrafo = Boligrafo(10, "rojo")
segundo_boligrafo = Boligrafo(20, "verde")

print(primer_boligrafo.cantidad_tinta)
primer_boligrafo.escribir_texto("hola")
print(primer_boligrafo.cantidad_tinta)


print(primer_boligrafo.recargar(35))

print(primer_boligrafo.cantidad_tinta)

