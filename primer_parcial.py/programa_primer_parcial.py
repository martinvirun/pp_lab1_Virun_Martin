import biblioteca_primer_parcial
from biblioteca_primer_parcial import app_parcial
from biblioteca_primer_parcial import menu_parcial
from biblioteca_primer_parcial import abrir_archivo
import json
jugadores = abrir_archivo("/home/martin/Documentos/programacion_1/dt.json")
lista_jugadores = jugadores["jugadores"]
while (app_parcial(lista_jugadores,menu_parcial()) != 0):
     pass