#!/usr/bin/python3

from dataclasses import dataclass
from .meses import Mes

@dataclass
class CosechaAnual:
    """Clase para representar los datos recogidos sobre la cosecha de un año"""

    __year: int

    __evolucion_precios: dict
    __produccion: dict
    __precipitaciones: dict
    __existencias_iniciales: dict

    __precio_maximo: float
    __mes_precio_maximo: Mes
    __meses_evaluables: Mes

    # Constructor personalizado para generar el objeto en base a datos en fichero
    def __init__(self, input_file: str):

        self.__evolucion_precios = dict()
        self.__produccion = dict()
        self.__precipitaciones = dict()
        self.__existencias_iniciales = dict()

        with open(input_file, 'r') as f:
            lineas = f.readlines()

        self.__year = int(lineas[0])


        for linea in lineas [3:]:

            valores = linea.split(' ')
            mes = (Mes[valores[0]]).name
            precio_mes = valores[1]
            produccion = valores[2]
            precipitacion  = valores[3]
            existencias_iniciales = valores[4]

            self.__evolucion_precios[mes] = precio_mes
            self.__produccion[mes] = produccion
            self.__precipitaciones[mes] = precipitacion
            self.__existencias_iniciales[mes] = existencias_iniciales

        self.__precio_maximo = max(self.__evolucion_precios.values())
        mes_max = [k for k, v in self.__evolucion_precios.items() if v == self.__precio_maximo][0]
        self.__mes_precio_maximo = Mes[mes_max]

        self.__meses_evaluables = [m for m in Mes][len(__evolucion_precios)-1]


    def get_evolucion_precios(self) -> dict:
        return self.__evolucion_precios

    def get_produccion(self) -> dict:
        return self.__produccion
    
    def get_precipitaciones(self) -> dict:
        return self.__precipitaciones

    def get_existencias_iniciales(self) -> dict:
        return self.__existencias_iniciales

    def get_precio_maximo(self) -> float:
        return self.__precio_maximo

    def get_mes_precio_maximo(self) -> Mes:
        return self.__mes_precio_maximo

    def get_meses_evaluables(self) -> Mes:
        return self.__meses_evaluables
