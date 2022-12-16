#!/usr/bin/python3

from dataclasses import dataclass
from .meses import Mes

@dataclass(frozen=True)
class CosechaAnual:

    # Año que representa
    year: int

    # Colecciones de datos mensuales
    evolucion_precios: dict
    existencias_iniciales: dict
    produccion: dict
    precipitaciones: dict
    # Datos anuales
    precio_max: float
    mes_precio_max: Mes
    meses_evaluables: Mes






# Inicializador de la clase Cosecha Anual

def CosechaAnual_init(input_file: str):

    year = int()
    evolucion_precios = dict()
    existencias_iniciales = dict()
    produccion = dict()
    precipitaciones = dict()
    precio_max = float()
    mes_precio_max = str()
    meses_evaluables = str()

    with open('./informes/'+ input_file, 'r') as f:
        
        lineas = f.readlines()
        
        year = int(lineas[0].split(',')[0])


    for linea in lineas [3:]:
        
        valores = linea.split(',')
        mes = (Mes[valores[0].upper()]).name
        evolucion_precios[mes] = valores[1]
        existencias_iniciales[mes] = valores[2]
        produccion[mes] = valores[3]
        precipitaciones[mes]  = valores[4]

        if evolucion_precios[mes] != 's/c':
            meses_evaluables = mes

            if(precio_max < float(evolucion_precios[mes])):
                precio_max = float(evolucion_precios[mes])
                mes_precio_max = mes

    return CosechaAnual(year, evolucion_precios, existencias_iniciales, produccion, precipitaciones, precio_max, mes_precio_max, meses_evaluables)