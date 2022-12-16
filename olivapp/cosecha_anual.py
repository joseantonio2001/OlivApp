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


    def get_anio(self) -> int:
        return self.year


    def get_evolucion_precios(self) -> dict:
        return self.evolucion_precios
    
    
    def get_produccion(self) -> dict:
        return self.produccion
    
    
    
    def get_precipitaciones(self) -> dict:
        return self.precipitaciones
    
    
    def get_existencias_iniciales(self) -> dict:
        return self.existencias_iniciales
    
    
    def get_precio_maximo(self) -> float:
        return self.precio_max
 

    def get_mes_prec_máx(self) -> Mes:
        return self.mes_precio_max


    def get_meses_evaluables(self) -> Mes:
        return self.meses_evaluables


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

    with open(input_file, 'r') as f:
        
        lineas = f.readlines()
        
        year = int(lineas[0].split(',')[0])


    for linea in lineas [3:]:
        
        valores = linea.split(',')
        
        if valores[1] != 's/c':
            mes = (Mes[valores[0].upper()]).name
            evolucion_precios[mes] = valores[1]
            existencias_iniciales[mes] = valores[2]
            produccion[mes] = valores[3]
            precipitaciones[mes]  = valores[4]

            meses_evaluables = mes

            if(precio_max < float(evolucion_precios[mes])):
                precio_max = float(evolucion_precios[mes])
                mes_precio_max = mes

    return CosechaAnual(year, evolucion_precios, existencias_iniciales, produccion, precipitaciones, precio_max, mes_precio_max, meses_evaluables)