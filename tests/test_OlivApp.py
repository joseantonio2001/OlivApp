import pytest
from assertpy import assert_that
import os

from olivapp.cosecha_anual import CosechaAnual
from olivapp.preditor import Predictor

def test_informes():

    os.system('poe getInformes')

    informesDirect = os.popen("ls").read()
    assert_that(informesDirect).contains('informes')

    informesFiles = os.popen("ls ./informes/").read()
    assert_that(informesFiles).is_not_empty()
    

def test_CosechaAnualBuilder():

    informesFiles = os.popen("ls ./informes/").read()
    infome = informesFiles.split('\n')

    ano = CosechaAnual(infome[0])

    valor_ano = informesFiles.split('.')

    assert_that(int(valor_ano[0])).is_equal_to(ano.get_anio())

    informesDirect = os.popen("cat ./informes/" + infome[0] + ' | grep enero').read()
    datosAno = informesDirect.split(',') #[0] -> Mes, [1] -> Precio, [2] -> Existencias Inic., [3] -> Producción, [4] -> Precipitaciones

    assert_that(ano.get_evolucion_precios()['ENERO']).is_equal_to(datosAno[1])
    assert_that(ano.get_existencias_iniciales()['ENERO']).is_equal_to(datosAno[2])
    assert_that(ano.get_produccion()['ENERO']).is_equal_to(datosAno[3])
    assert_that(ano.get_precipitaciones()['ENERO']).is_equal_to(datosAno[4])


def test_PredictorBuilder():
    informesFiles = os.popen("ls ./informes/").read()
    informNames = informesFiles.split('\n')

    cosechas_anteriores=[]
    for i in range(len(informNames)-1):
        if i < len(informNames)-2:
            cosechas_anteriores.append(CosechaAnual(informNames[i]))
        else:
            cosecha_actual = CosechaAnual(informNames[i])

    prediccion = Predictor(cosechas_anteriores, cosecha_actual)
    
    assert_that(prediccion).is_not_none()
    assert_that(prediccion.get_cosecha_actual()).is_instance_of(CosechaAnual)
    assert_that(prediccion.get_cosechas_anteriores()).is_type_of(list)
    for cosecha in prediccion.get_cosechas_anteriores():
        assert_that(cosecha).is_instance_of(CosechaAnual) 
