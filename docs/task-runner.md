# TASK RUNNER

Antes de avanzar con el proyecto es necesario elegir un task runner que se adecúe a las caracteísticas del proyecto, que nos permita automatizar tareas agilizando el desarrollo de este.

## Análisis de tasks runners

He analizado varios tasks runners, como (breve descripción de cada uno):

 - [Pypyr](https://github.com/pypyr/pypyr): se presenta como una script de shell, menos complejo que MAKE. Permite ejecutar tareas secuenciales definidas en yaml.

 - [Invoke](https://www.pyinvoke.org/): Está inspirado en varias fuentes como make. Proporciona una API limpia y de alto nivel para ejecutar comandos de shell y definir/organizar funciones de tareas desde un archivo tasks.py.

 - [Doit](https://pydoit.org/): Permite definir fácilmemte tareas, ayudándote a organizar todas las tareas relacionadas con el proyecto de una manera unificada, fácil de usar y reconocible. Permite hacer la creación de tareas y dependencias dinámicamente durante la ejecución.

Con el fin de una optimizar el tiempo he optado por **invoke** como task runner para el desarrollo del proyecto, por su rendimiento y que resulta una herramineta fácil de comprender y usar.




    