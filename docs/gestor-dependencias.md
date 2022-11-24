# GESTOR DE DEPENDENCIAS

Antes de avanzar con el proyecto es necesario elegir un gestor de depenedencias que nos permita automatizar el proceso de instalación y mantentenimiento de las versiones utilizadas. 

## Criterios de elección del gestor de dependencias

El principal requisito que debe cumplir el gestor de dependencias es que siga los estándares de python. PEP es el conjunto de estándares de python, y concretamente para la elección del gestor de dependencias se seguirá el estándar [PEP 518](https://peps.python.org/pep-0518/), el cual especifica los requisitos mínimos del sistema de compilación para proyectos python.

* Criterios mínimos:

 - Uso de un fichero (**pyproject.toml** es la que PEP 518 indica que sigue las mejores prácticas) para almacenar las dependencias del sistema de compilación.

 - Debe generar un fichero .lock, que garantize que las dependencias sigan fijadas a las versiones que se han establecido.

 - Debe ofrecer buen rendimiento, en cuanto a velocidades de instalación, compilación, ...

 - Debe ser una herramienta fácil de usar y de entender. 

## Decisión de gestores de dependencias

Ajustandome a los criterios redactados en el apartado anterior he analizado los siguientes gestores de dependencias:

| Gestor de dependencias    | fichero de dependencias    | fichero .lock | Observaciones                                                                                           |
|---------------------------|----------------------------|---------------|---------------------------------------------------------------------------------------------------------|
| Pipenv                    | Pipfile                    | Pipfile.lock  | Instalaciones lentas; No usa pyproject.toml                                                             |
| Poetry                    | pyproject.toml             | poetry.lock   | Buen rendimiento (> rendimiento que Pipenv)                                                             |
| Hatch                     | pyproject.toml             |       ✓       | Funciona junto con conda para ayudar a instalar dependencias. Más difícil de entender su funcionamiento |

Para el proyecto que se está desarrollando se optado por **Poetry** como el gestor de dependencias más adecuado.

## ¿Pórque Poetry?

El motivo principal es que esta herramienta se ajusta perfectamente al estándar PEP 518. Además brinda de gran cantidad de documentaión de calidad que facilita el aprendizaje de la herramienta, presenta un buen rendimiento, con gran velocidad de instalación y resultando una herramienta ágil y con esta herramienta no tienes que preocuparte por el entorno virtual.

    

    
