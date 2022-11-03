#!/usr/bin/python3

from dataclasses import dataclass
from .cosecha_anual import CosechaAnual

@dataclass
class Predictor:

    year: int
    
    cosechas_anteriores: list[CosechaAnual]
    cosecha_pred: CosechaAnual = None
