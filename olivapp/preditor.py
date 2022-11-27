#!/usr/bin/python3

from dataclasses import dataclass
from .cosecha_anual import CosechaAnual

class Predictor:

    year: int
            
    cosechas_anteriores: list
    cosecha_actual: CosechaAnual = None

    # Constructor personalizado para cargar las cosechas
    def __init__(self, cosechas_anteriores: list, cosecha_actual: CosechaAnual):

        self.__year = cosecha_actual.get_anio()
        self.__cosechas_anteriores = cosechas_anteriores
        self.__cosecha_actual = cosecha_actual

    def get_anio(self) -> int:
        return self.__year

    def get_cosechas_anteriores(self) -> list:
        return self.__cosechas_anteriores

    def get_cosecha_actual(self) -> CosechaAnual:
        return self.__cosecha_actual
