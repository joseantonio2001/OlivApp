# TEST RUNNER

El primer paso para poder testear el código de nuestro proyecto es disponer de un test runner que nos permita detectar errores en este, haciendo uso de una biblioteca de aserciones ([#25](https://github.com/joseantonio2001/OlivApp/issues/25))

## Criterios de elección

Para la elección de nuestro test runner vamos ayudarnos de la información que nos ofrece [snyk Advisor](https://snyk.io/advisor/python). La elección del test runner se basará principalmente en:

 - Rendimiento: necesitamos un testing framework rápido, que no entorpezca el workflow del proyecto a la hora de realizar los test.

## Análisis de Test Runner

Ajustandome a las características de mi proyecto, los criterios de elección establecidos y los indices de popularidad que encontramos en [synk Advisor](https://snyk.io/advisor/python), he analizado los siguientes test-runners:

| Test Runner                                | Descripción                | Observaciones                                                                                                                                             |
|--------------------------------------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [testify](https://pypi.org/project/testify/)   |  Se basa en Unittest; Tiene una sintaxis simple para __fixtures__; Viene con un complemento extensible que ofrece una útil funcionalidad de informes.   |  Para ususarios familiarizados con Unittest resulta fácil acostumbrarse a esta herramienta. Es un test-runner poco popular entre los usuarios de python. Actualmente se considera un proyecto **INACTIVO** |
| [Pytest](https://pypi.org/project/pytest/) | Prestenta información detallada sobre __falling assert__;  __Auto-discovery__  de los módulos que contienen los tests; __Modular fixtures__  para gestionar test de larga duración. Permite ejecutar test en __paralelo__.           |  Actualmente es el test-runner más popular entre los usuarios de python. Es considerado como un proyecto **ACTIVO**, con buena cadencia de actualizaciones |
| [nose2](https://pypi.org/project/nose2/)   | Dispone de gran cantidad de complementos. Se basa en Unittest; __Auto-discovery__  de los módulos que contienen los tests (al igual que Pytest); Permite ejecutar test en __paralelo__   |  Es un test-runner popular entre los usuarios de python (< popular que Pytets). La actividad de nose2 ha disminuido últimente con una menor cadencia de actualizaciones |

Para el proyecto que se está desarrollando se optado por **Pytest** como el test runner más adecuado.

## ¿Pórque Pytest?

Pytest presenta un buen rendimiento, que teniendo en cuenta que a lo largo del proyecto se ejecutarán numerosas veces los tests desarrollados, es un factor importante a tener en cuenta. Además pytest se considera un proyecto activo (en continuo desarrollo), con constantes actualizaciones; Por último al resultar el task runner más popular para python, brinda de abundante documentación en información en foros que facilitarán la comprensión del funcionamiento de la herramienta.
