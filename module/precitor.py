#!/usr/bin/python3
from dataclasses import dataclass
from .cosecha_anual import CosechaAnual


"""Clase generadora de predicciones en base a los 5 años anteriores"""
@dataclass
class Predictor():

    year: int
    cosechas_anteriores: list[CosechaAnual] 
    cosecha_pred: CosechaAnual = None

    def gen_prediccion(self):
        # Debe generar un archivo, nombrado como el año que se va a predecir
        # guardar los datos en el formato establecido en los issues
        continue

    def gen_prediccion(self, output_file: str):
        # Debe generar un archivo, nombrado como el argumento output_file
        # guardar los datos en el formato establecido en los issues
        continue

    def cargar_prediccion(self):
        input_file = f'prediccion_{self.year}.csv'
        self.cosecha_pred = CosechaAnual(input_file)

    def cargar_prediccion(self, input_file: str):
        self.cosecha_pred = CosechaAnual(input_file)
