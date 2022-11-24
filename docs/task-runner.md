# TASK RUNNER

Antes de avanzar con el proyecto es necesario elegir un task runner que se adecúe a las caracteísticas del proyecto, que nos permita automatizar tareas agilizando el desarrollo de este.

## Criterios de elección del task runner

Los requisitos que debe presentar el task runner son: 
 
 - Que resulte una herramientá ágil, fácil de usar y comprender su funcionamiento.
 
 - Herramienta capaz de trabajar con **poetry** (gestor de dependencias del proyecto) con el fin minimizar el número de ficheros que debemos mantener para el proyecto.

## Decisión del task runner

Ajustandome a los criterios redactados en el apartado anterior he analizado los siguientes task runner:

| Gestor de dependencias                  | Descripción                                                                                      |  Observaciones                                                                                           |
|-----------------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [Pypyr](https://github.com/pypyr/pypyr) | script de shell, menos complejo que MAKE. Permite ejecutar tareas secuenciales definidas en yaml | Actualmente se considera como proyecto __ACTIVO__                                                           |
| [Invoke](https://www.pyinvoke.org/)     | inspirado en varias fuentes como make. Proporciona una API limpia y de alto nivel para ejecutar comandos de shell y definir/organizar funciones de tareas desde un archivo tasks.py. | Actualmente se considera como proyecto __ACTIVO__; Es actualmente el task runner más utilizado en python                                                           |
| [Doit](https://pydoit.org/)             | Permite definir fácilmemte tareas, ayudándote a organizar todas las tareas relacionadas con el proyecto de una manera unificada, fácil de usar y reconocible. Permite hacer la creación de tareas y dependencias dinámicamente durante la ejecución. | Actualmente se considera como proyecto __INACTIVO__                                                           |
| [PoethePoet](https://github.com/nat-n/poethepoet) | Permite trabajar conjuntamente con el gestor de dependencias Poetry utilizando al igual que Poetry usa para gestionar dependencias, el fichero pyproject.toml para la definición de tareas | Actualmente se considera como proyecto __ACTIVO__ ; Es actualmente el task runner que mejor se integra a Poetry                                                         |

Para el proyecto que se está desarrollando se optado por **PoethePoet** como el task runner más adecuado.

## ¿Pórque PoethePoet?
PoethePoet se ajusta a los criterios de elección defindos. Además PoethePoet continua actualizándose considerandose así un proyecto activo; Al ser un task runner popular entre los usuarios de python brinda de abundante documentación e información en foros, lo que facilitará la comprensión del funcionamiento de la herramienta. Por último al usar pyproject.toml como fichero de definición de tareas se integra perfectamente a Poetry y permite minimizar el número de ficheros del proyecto.