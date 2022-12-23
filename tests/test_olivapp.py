import pytest
from assertpy import assert_that
import os

from olivapp.cosecha_anual import CosechaAnual, CosechaAnual_init
from olivapp.predictor import Predictor

DIRECTORIO_INFORMES = './informes/'
CABECERA_INFORMES = 'Mes,Precio Medio Global [€/t],Existencias iniciales,Produccion,Precipitaciones'
MESES = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
POS_MES_PREDICTION = 413

@pytest.fixture
def Predictor_Obj():

    cosechas = os.listdir(DIRECTORIO_INFORMES)
    cosechas.sort()

    cosechas_anteriores = []
    cosecha_actual = 0
    for i in range(len(cosechas)):
        if (i < len(cosechas)-1):
            cosechas_anteriores.append(CosechaAnual_init(DIRECTORIO_INFORMES + cosechas[i]))
        else:
            cosecha_actual = CosechaAnual_init(DIRECTORIO_INFORMES + cosechas[i])

    return Predictor(cosechas_anteriores, cosecha_actual)

#FORMATO DE LOS INFORMES
def test_informes():

    assert_that(os.listdir(DIRECTORIO_INFORMES)).is_not_empty()

    for x in os.listdir(DIRECTORIO_INFORMES):
        assert_that(os.stat(DIRECTORIO_INFORMES + x).st_size).is_not_equal_to(0)
        assert_that(open(DIRECTORIO_INFORMES + x, 'r').read().find(CABECERA_INFORMES)).is_not_equal_to(-1)
        assert_that(len(open(DIRECTORIO_INFORMES + x).readlines())).is_equal_to(15)

