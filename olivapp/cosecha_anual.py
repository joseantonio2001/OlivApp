#!/usr/bin/python3

from dataclasses import dataclass
from .meses import Mes

@dataclass(frozen=True)
class CosechaAnual:

    year: int

    evolucion_precios: dict
    produccion: dict
    precipitaciones: dict
    existencias_iniciales: dict

    precio_max: float
    mes_precio_max: Mes
    meses_evaluables: Mes
