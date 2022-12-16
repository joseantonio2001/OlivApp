#!/usr/bin/python3

from dataclasses import dataclass
from .cosecha_anual import CosechaAnual
from .meses import Mes

class Predictor:

    year: int
            
    cosechas_anteriores: list
    cosecha_actual: CosechaAnual = None

    # Constructor personalizado para cargar las cosechas
    def __init__(self, cosechas_anteriores: list, cosecha_actual: CosechaAnual):

        self.__year = cosecha_actual.get_anio()
        self.__cosechas_anteriores = cosechas_anteriores
        self.__cosecha_actual = cosecha_actual


    def get_prediction(self) -> str:
        
        diff = self.__diferencia(self.__cosechas_anteriores[0])  
        similar_year = self.__cosechas_anteriores[0].get_anio()

        i=0
        for ano in self.__cosechas_anteriores:
            if(self.__diferencia(ano) < diff):                                      #   El precio máximo del aceite de oliva de una campaña se obtiene a partir                                 
                diff = self.__diferencia(ano)                                       # de los datos recopilados en el año anterior, por ello una vez encontrado el 
                if(ano.get_anio() == self.__cosecha_actual.get_anio()-1):           # año que más se asimila al año actual, podemos determinar el mes de la campaña     
                    similar_year = self.__cosecha_actual                            # siguiente donde se añcanzará un mayor precio en el mercado
                else:
                    similar_year = self.__cosechas_anteriores[i+1]
            i+=1

        return self.__to_string(similar_year)

    def __diferencia(self, cosecha: CosechaAnual) -> float:

        diferencia = 0.0
        for mes in Mes:
            diferencia = (diferencia + abs(float(self.__cosecha_actual.get_evolucion_precios()[mes.name]) - float(cosecha.get_evolucion_precios()[mes.name])) +
                        abs(float(self.__cosecha_actual.get_existencias_iniciales()[mes.name]) - float(cosecha.get_existencias_iniciales()[mes.name])) +
                        abs(float(self.__cosecha_actual.get_produccion()[mes.name]) - float(cosecha.get_produccion()[mes.name])) +
                        abs(float(self.__cosecha_actual.get_precipitaciones()[mes.name]) - float(cosecha.get_precipitaciones()[mes.name])))


            if(mes.name == self.__cosecha_actual.get_meses_evaluables()):
                break

        return round(diferencia,2)

    def __to_string(self, similar_year: CosechaAnual) -> str:
        output = ('# OLIVAPP - Predicción sobre el mayor costo del aceite de oliva en el mercado para la próxima campaña de ' + str(self.__cosecha_actual.get_anio()+1) + '\n\n' +
                '   Mediante una comparación por similitud de datos mensuales, se ha detectado que los datos de la campaña de ' + str(similar_year.get_anio() - 1) + ' son los que más se asemejan a los datos de las campaña actual (' + str(similar_year.get_anio()) + '), por lo que se prevee que '+
                'en la siguiente campaña el aceite de oliva alcanzará su mayor precio en mercado en el mes de ' + str(similar_year.get_mes_prec_máx()) + '\n')
            
        return output