# LIBRERÍA DE ASERCIONES

Una vez seleccionada el test-runner para gestionar los test (__pytest__), necesitamos una librería de aserciones que nos permita trabajar con los tests.

## Criterios de elección

Para la elección de nuestra librería de aserciones vamos ayudarnos de la información que nos ofrece [snyk Advisor](https://snyk.io/advisor/python). La elección de la librería de aserciones se basará principalmente en:

 - Rendimiento: ejecución rápida de los test.

 - Frescura: refiriéndonos al estado (actualización) de la herramienta.  

 - TDD: enfocada en cómo escribir el código y cómo debería funcionar (al contrario de BBD que hace hincapié en por qué debes escribir ese código y cómo se debería comportar).

## Análisis de librería de aserciones

Ajustandome a las características de mi proyecto, los criterios de elección establecidos y los indices de popularidad que encontramos en [synk Advisor](https://snyk.io/advisor/python), he analizado los siguientes test-runners:

| Assertion Library                                | Descripción                | Puntuación en Snyk                | Observaciones                                                                                                                                             |
|--------------------------------------------|----------------------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [grappa](https://pypi.org/project/grappa/)   |  Biblioteca de aserciones expresiva y fácil de usar; Presenta un sistema de informe de errores detallado y de fácil comprensión.   |  **51/100** |  Aunque es considerado un software estable, no es un software ampliamente utilizado, por lo que no es muy popular. Actualmente es considerado un proyecto **INCTIVO** |
| [assertpy](https://pypi.org/project/assertpy/) | API para crear test compactos y legibles; Su implementación está basada en AssertJ de Java; Diseñada para aprovevhar al máximo el dinamismo en el tiempo de ejecución de Python |  **66/100** |  Es una de las bibliotecas de asserciones más populares entre los usuarios de python, aunque la cadencia de actualizaciones de esta herramienta ha disminuido últimamente. Cabe destacar que (tal como indica su documentación) trabaja mejor con test-runners como **pytest** (test-runner que se ha seleccionado para este proyecto) |
| [expects](https://pypi.org/project/expects/) | Biblioteca de aserción TDD/BDD expresiva y extensible para Python           | **51/100** |  Actualmente su popularidad es baja entre los usuarios de python. Es considerado como un proyecto **INACTIVO** |

Aunque todas las librerias que se han analizado presentan un rendimiento similar, la frescura y las observaciones y puntuación que nos ofrece snyk nos ha hecho decantarnos por **assertpy** como libreria de aserciones más adecuada para este proyecto.

## ¿Pórque assertpy?

Assertpy presenta multitud de [métodos](https://github.com/assertpy/assertpy#strings) para elaborar tests. Además esta librería trabaja muy bien con pytest (test-runner escogido para nuestro proyecto). Este brinda de abundante documentación e información en foros que facilitarán la comprensión del funcionamiento de la herramienta.