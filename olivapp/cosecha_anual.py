#!/usr/bin/python3

from dataclasses import dataclass
from .meses import Mes

@dataclass(frozen=True)
class CosechaAnual:

    # Año que representa
    year: int

    # Colecciones de datos mensuales
    evolucion_precios: dict
    produccion: dict
    precipitaciones: dict
    existencias_iniciales: dict
    # Datos anuales
    precio_max: float
    mes_precio_max: Mes
    meses_evalables: Mes
 
