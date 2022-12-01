# LIBRERÍA DE ASERCIONES

Una vez seleccionada el test-runner para gestionar los test (__pytest__), necesitamos una librería de aserciones que nos permita trabajar con los tests.

## Criterios de elección

Para la elección de nuestra librería de aserciones vamos ayudarnos de la información que nos ofrece [snyk Advisor](https://snyk.io/advisor/python). La elección de la librería de aserciones se basará principalmente en:

 - Rendimiento: ejecución rápida de los test y de forma sencilla.

 - Frescura: refiriéndonos al estado (actualización) de la herramienta.  

## Análisis de Test Runner

Ajustandome a las características de mi proyecto, los criterios de elección establecidos y los indices de popularidad que encontramos en [synk Advisor](https://snyk.io/advisor/python), he analizado los siguientes test-runners:

| Assertion Library                                | Descripción                | Observaciones                                                                                                                                             |
|--------------------------------------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [grappa](https://pypi.org/project/grappa/)   |  Biblioteca de aserciones expresiva y fácil de usar; Presenta un sistema de informe de errores detallado y de fácil comprensión.   |  Aunque es considerado un software estable, no es un software ampliamente utilizado, por lo que no es muy popular. Actualmente es considerado un proyecto **INCTIVO** |
| [assertpy](https://pypi.org/project/assertpy/) | API para crear test compactos y legibles; Su implementación está basada en AssertJ de Java; Diseñada para aprovevhar al máximo el dinamismo en el tiempo de ejecución de Python |  Es una de las bibliotecas de asserciones más populares entre los usuarios de python, aunque la cadencia de actualizaciones de esta herramienta ha disminuido últimamente. Cabe destacar que (tal como indica su documentación) trabaja mejor con test-runners como pytest (test-runner que se ha seleccionado para este proyecto) |
| [expects](https://pypi.org/project/expects/) | Biblioteca de aserción TDD/BDD expresiva y extensible para Python           |  Actualmente su popularidad es baja entre los usuarios de python. Es considerado como un proyecto **INACTIVO** |

Para el proyecto que se está desarrollando se optado por **assertpy** como el test runner más adecuado.

## ¿Pórque assertpy?

Assertpy presenta multitud de [métodos](https://github.com/assertpy/assertpy#strings) para elaborar tests. Además esta librería trabaja muy bien con pytest (test-runner escogido para nuestro proyecto). Este brinda de abundante documentación e información en foros que facilitarán la comprensión del funcionamiento de la herramienta.