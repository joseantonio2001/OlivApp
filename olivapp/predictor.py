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
        similar_year = self.__cosechas_anteriores[0]

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

        cosecha_act_norm = self.__normalizated(self.__cosecha_actual)
        cosecha_x_normalizated = self.__normalizated(cosecha)

        diferencia = 0.0
        for x in range(len(cosecha_act_norm)):
            diferencia = diferencia + abs(cosecha_act_norm[x] - cosecha_x_normalizated[x])

        return round(diferencia,2)

    def __normalizated(self, cosecha: CosechaAnual) -> list:
        
        normalizated_data = []

        for m in Mes:
            normalizated_data.append(self.__normalization_f(cosecha.get_evolucion_precios()[m.name]))
            normalizated_data.append(self.__normalization_f(cosecha.get_existencias_iniciales()[m.name]))
            normalizated_data.append(self.__normalization_f(cosecha.get_produccion()[m.name]))
            normalizated_data.append(self.__normalization_f(cosecha.get_precipitaciones()[m.name]))

            if(m.name == self.__cosecha_actual.get_meses_evaluables()):
                break

        return normalizated_data

    def __normalization_f(self, value: str) -> float:
        
        value = float(value)
        value_max = 5000
        value_min = 0
        
        normalizated_value = (value - value_min) / (value_max - value_min)

        return round(normalizated_value,4)

    def __to_string(self, similar_year: CosechaAnual) -> str:

        output = ('# OLIVAPP - Predicción sobre el mayor costo del aceite de oliva en el mercado para la próxima campaña de ' + str(self.__cosecha_actual.get_anio()+1) + '\n\n' +
                '   Mediante una comparación por similitud de datos mensuales, se ha detectado que los datos de la campaña de ' + str(similar_year.get_anio() - 1) + ' son los que más se asemejan a los datos de las campaña actual (' + str(self.__cosecha_actual.get_anio()) + '), por lo que se prevee que '+
                'en la siguiente campaña el aceite de oliva alcanzará su mayor precio en mercado en el mes de ' + str(similar_year.get_mes_prec_máx()) + '\n')
            
        return output