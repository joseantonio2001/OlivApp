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
        return self.precio_maximo
 

    def get_mes_prec_máx(self) -> Mes:
        return self.mes_precio_max


    def get_meses_evaluables(self) -> Mes:
        return self.meses_evaluables


