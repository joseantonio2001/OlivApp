#!/usr/bin/python3

from dataclasses import dataclass
from meses import Mes

#@dataclass(frozen=True)
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

   
    # Constructor personalizado para generar el objeto en base a datos en fichero
    def __init__(self, input_file: str):

        self.__evolucion_precios = dict()
        self.__existencias_iniciales = dict()
        self.__produccion = dict()
        self.__precipitaciones = dict()
        self.__precio_maximo = float()


        with open(input_file, 'r') as f:
            
            lineas = f.readlines()
            
            self.__year = int(lineas[0].split(',')[0])


        for linea in lineas [3:]:
            
            valores = linea.split(',')
            mes = (Mes[valores[0].upper()]).name
            precio_mes = valores[1]
            existencias_iniciales = valores[2]
            produccion = valores[3]
            precipitacion  = valores[4]

            self.__evolucion_precios[mes] = precio_mes
            self.__existencias_iniciales[mes] = existencias_iniciales
            self.__produccion[mes] = produccion
   

        for m in Mes:

            if self.__evolucion_precios[m.name] != 's/c':
                self.__meses_evaluables = m.name

                if(self.__precio_maximo < float(self.__evolucion_precios[m.name])):
                   self.__precio_maximo = float(self.__evolucion_precios[m.name])
                   self.__mes_precio_maximo = m.name
            
            else:
                break
                
        
    
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
 
