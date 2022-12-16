import pytest
from assertpy import assert_that
import os

from olivapp.cosecha_anual import CosechaAnual, CosechaAnual_init
from olivapp.predictor import Predictor

def test_informes():

    os.system('gdown --folder 1WzypEZh_fa3ZNmTZ4_KMfGVAbuBO95xR -O informes')

    informesDirect = os.popen("ls").read()
    assert_that(informesDirect).contains('informes')

    informesFiles = os.popen("ls ./informes/").read()
    assert_that(informesFiles).is_not_empty()
    

def test_CosechaAnualBuilder():

    informesFiles = os.popen("ls ./informes/").read()
    infome = informesFiles.split('\n')

    ano = CosechaAnual_init(infome[0])

    valor_ano = informesFiles.split('.')

    assert_that(int(valor_ano[0])).is_equal_to(ano.get_anio())

    informesDirect = os.popen("cat ./informes/" + infome[0] + ' | grep enero').read()
    datosAno = informesDirect.split(',') #[0] -> Mes, [1] -> Precio, [2] -> Existencias Inic., [3] -> Producción, [4] -> Precipitaciones

    assert_that(ano.get_evolucion_precios()['ENERO']).is_equal_to(datosAno[1])
    assert_that(ano.get_existencias_iniciales()['ENERO']).is_equal_to(datosAno[2])
    assert_that(ano.get_produccion()['ENERO']).is_equal_to(datosAno[3])
    assert_that(ano.get_precipitaciones()['ENERO']).is_equal_to(datosAno[4])


@pytest.fixture
def build_Predictor():

    informesFiles = os.popen("ls ./informes/").read()
    informNames = informesFiles.split('\n')

    cosechas_anteriores=[]
    for i in range(len(informNames)-1):
        if i < len(informNames)-2:
            cosechas_anteriores.append(CosechaAnual_init(informNames[i]))
        else:
            cosecha_actual = CosechaAnual_init(informNames[i])

    return Predictor(cosechas_anteriores, cosecha_actual)


def test_PredictorBuilder(build_Predictor):

    prediccion = build_Predictor
    
    assert_that(prediccion).is_not_none()
    assert_that(prediccion.get_cosecha_actual()).is_instance_of(CosechaAnual)
    assert_that(prediccion.get_cosechas_anteriores()).is_type_of(list)
    for cosecha in prediccion.get_cosechas_anteriores():
        assert_that(cosecha).is_instance_of(CosechaAnual) 


def test_Prediction(build_Predictor):

    prediccion = build_Predictor

    year_comparate = prediccion.get_prediction().split('datos de la campaña de ')[1].split(' ')[0]

    year_prediction = CosechaAnual
    for i in range(len(prediccion.get_cosechas_anteriores())):
        if prediccion.get_cosechas_anteriores()[i].get_anio() == int(year_comparate):
            if prediccion.get_cosechas_anteriores()[i].get_anio() == prediccion.get_cosechas_anteriores()[len(prediccion.get_cosechas_anteriores())-1].get_anio():
                year_prediction = prediccion.get_cosecha_actual()
            else:
                year_prediction = prediccion.get_cosechas_anteriores()[i+1]
            break

    mes_prediction = prediccion.get_prediction().split('mercado en el mes de ')[1].split('\n')[0]

    assert_that(year_prediction.get_mes_prec_máx()).is_equal_to(mes_prediction)
