# TEST RUNNER

El primer paso para poder testear el código de nuestro proyecto es disponer de un test runner que nos permita detectar errores en este, haciendo uso de una biblioteca de aserciones ([#25](https://github.com/joseantonio2001/OlivApp/issues/25))

## Criterios de elección

Para la elección de nuestro test runner vamos ayudarnos de la información que nos ofrece [snyk Advisor](https://snyk.io/advisor/python). La elección del test runner se basará principalmente en:

 - Rendimiento: necesitamos un testing framework rápido, que no entorpezca el workflow del proyecto a la hora de realizar los test.

 - Observaciones y puntuación en snyk Advisor

## Análisis de Test Runner

Ajustandome a las características de mi proyecto, los criterios de elección establecidos y los indices de popularidad que encontramos en [synk Advisor](https://snyk.io/advisor/python), he analizado los siguientes test-runners:

| Test Runner                                | Descripción                | Puntuación en Snyk                | Observaciones                                                                                                                                             |
|--------------------------------------------|----------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [unitTest](https://pypi.org/project/unittest/)   |  Se basa en JUnit de Java; Es un marco de pruebas integrado en Python. Dado que viene con el lenguaje Python, no hay módulos adicionales para instalar, y la mayoría de los desarrolladores lo usan para comenzar a aprender sobre las pruebas.   | **37/100** |  Para ususarios familiarizados con JUnit (Java) resulta fácil acostumbrarse a esta herramienta. Es un test-runner cuya popularidad ha disminuido bastanta últimamente entre los usuarios de python. Requiere de la creación de una clase para definir tests. Actualmente se considera un proyecto **INACTIVO** |
| [Pytest](https://pypi.org/project/pytest/) | Prestenta información detallada sobre __falling assert__;  __Auto-discovery__  de los módulos que contienen los tests; __Modular fixtures__  para gestionar test de larga duración. Permite ejecutar test en __paralelo__.           | **97/100** |  Actualmente es el test-runner más popular entre los usuarios de python. Es considerado como un proyecto **ACTIVO**, con buena cadencia de actualizaciones. A diferencia de UnitTest, este no requiere de la creación de una clase para definir tests, los test se definen mediante funciones. Presenta un rendimiento mayor al de unitTest |
| [nose2](https://pypi.org/project/nose2/)   | Dispone de gran cantidad de complementos. Se basa en Unittest; __Auto-discovery__  de los módulos que contienen los tests (al igual que Pytest); Permite ejecutar test en __paralelo__   | **85/100** |  Es un test-runner popular entre los usuarios de python (< popular que Pytets). La actividad de nose2 ha disminuido últimente con una menor cadencia de actualizaciones. Los tests se definen en funciones. Presenta un rendimiento similar al de Pytest. |

Para el proyecto que se está desarrollando se optado por **Pytest** como el test runner más adecuado.

## ¿Pórque Pytest?

Pytest presenta un buen rendimiento, que teniendo en cuenta que a lo largo del proyecto se ejecutarán numerosas veces los tests desarrollados, es un factor importante a tener en cuenta. Además pytest se considera un proyecto activo (en continuo desarrollo), con constantes actualizaciones; Por último al resultar el task runner más popular para python, brinda de abundante documentación en información en foros que facilitarán la comprensión del funcionamiento de la herramienta.
