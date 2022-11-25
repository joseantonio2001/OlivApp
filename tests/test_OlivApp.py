import pytest
from assertpy import assert_that
import os

def test_informes():

    os.system('poe getInformes')

    informesDirect = os.popen("ls").read()
    assert_that(informesDirect).contains('informes')

    informesFiles = os.popen("ls ./informes/*").read()
    assert_that(informesFiles).is_not_empty()
    
