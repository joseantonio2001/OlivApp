# OlivApp
Software para asesoramiento de venta de aceite a granel.

## Definición del problema
Este proyecto aborda el problema que tienen muchas empresas productoras y comercializadoras de aceite a granel a la hora de pronosticar el momento más idóneo para la venta de su producto con el fin de mejorar su rentabilidad.

Para conocer mejor el problema se ha llevado a cabo una entrevista a un empleado de una cooperativa productora/comercializadora de aceite a granel( empresas a los que está dedicado el proyecto) el cuál nos ha descrito el problema, nos ha planteado cómo se solucionaría este de forma textual (“un sistema que realiza predicciones de cuando el aceite de oliva alcanza su mayor precio en el mercado”) y nos ha explicado aspectos importantes de la industria (“factores que hay que tener en cuenta para generar la predicción, ya que influyen en el precio del aceite de oliva en el mercado”).

## Planteamiento de la solución
El objetivo de la plataforma es que los usuarios (Empresas productoras y a su vez comercializadoras de aceite de oliva a granel: cooperativas oleícolas, almazaras privadas, productores particulares, compradores, agentes comerciales...) tengan una idea lo más aproximada posible sobre que momento del año puede estar en su nivel más alto el precio del aceite de oliva en origen.

El programa descargará una serie de archivos de una web que proporciona todos los datos centralizados (las URLs se encuentran en la sección "En que datos/informes/información se respalda y fundamente la App") para llevar a cabo su predicción. Estos archivos son históricos basados en tablas que recogen los datos de un parámetro deteminado(existencias iniciales, consumo, producción y precipitaciones) en cada mes de un año. Entonces el programa descargará un histórico del año actual de las existencias iniciales, del consumo, de la producción y de las precipitaciones (este parámatro aunque parezca que no pero será importante tenrlo en cuenta ya que influye en la producción de la cosecha) y descargará los mismos históricos pero de los 5/10 años anteriores. A partir de estos documentos el programa comparará los datos (existencias iniciales, consumo, producción y precipitaciones) del año actual con los de años anteriores y a partir de una serie de cálculos obtendrá cual sería el año más parecido al actual y a partir de ahí se basará para realizar su predicción; Esta predicción nos proporcionará en que época/meses del año el coste del aceite de oliva alcanza un mayor precio y por lo tanto sale más rentable su venta.
Así aunque un mes la predicción de la aplicación pueda ser p.ejemplo: "máx. coste del aceite de oliva se conseguirá en Julio", el mes siguiente la aplicaión puede cambiar su predicción debido a que hayan variado los factores que la aplicación evalúa para producir la predicción (por ejemplo las precipitaciones han aumentado y la producción ha bajado por lo que la situación actual se asemeja a la situción del año 2017(por ejemplo) donde el aceite de oliva alcanzo su máximo coste en Febrero, por lo que la predicción de la aplicación será ahora "máx. coste del aceite de oliva se conseguirá en Febrero").

El sistema utilizará la nube ya que el sistema accederá a una base de datos remota donde encotraremos los ficheros que contienen los datos que el sistema tiene en cuenta, y esos ficheros no serán constantes sino que sufrirán cambios (estos cambios los harán los admin del software; Este punto será explicado más abajo), por lo que siempre que se use el sistema, este consultará la nube para en caso de que haya nuevos datos sean cargados correctamente.

## ¿Porque querría una empresa utilizar OlivApp?
Los usuarios (empresas dedicadas a la producción y venta de aceite a granel, como ya hemos nombrado antes) usarían este sistema con el fin de incrementar su rentabilidad ya que si la empresa obtiene una predicción de en que meses el aceite alcanzará su mayor precio en mercado, esta podrá focalizar el mayor número de ventas en esos meses.

## En que datos/informes/información se respalda y fundamente la App
Recabando información de organismos oficiales como el COI (Comité Oleícola Internacional) Ministerio de Agricultura, Consejería de Agricultura, Poolred.

Los datos de existencias iniciales y consumo se obtienen de: https://www.mapa.gob.es/es/agricultura/temas/producciones-agricolas/aceite-oliva-y-aceituna-mesa/Datos_produccion_movimiento_existencias_AICA.aspx , https://www.mapa.gob.es/es/agricultura/temas/producciones-agricolas/informemensualdelasituaciondemercadodelsectordelaceitedeolivayaceitunademesa_julio2022_tcm30-626970.pdf (Boletín del ministerio de agricultura, pesca y alimentación).

Los datos de historial de precios se obtiene de: https://www.oliva.net/poolred/ErrorPOOL.aspx?TipoError=acceso&ReturnUrl=%2fpoolred%2fVendedor%2fPreciosMediosVendedor.aspx (POOLred es un Sistema de Información en origen del aceite de oliva).
PD: Para acceder a los datos de esta web se necesitará una cuenta dada de alta, que poseen las empresas productoras/comercializadoras de aceite de Oliva. A los desarrolladores del proyecto una empresa nos ha facilitado una clave, sin embargo adjuntamos un enlace que hemos creado donde podrás ver todos los datos que nos muestra esta web para validar su credibilidad: https://drive.google.com/drive/folders/1NoHETB7DiNCrkIhI1mxrwzDKXJGJAeNA?usp=sharing .

Los datos de precipitaciones se obtienen de: https://www.seprem.es/boletin/lluvia.pdf (Boletín del ministerio para la transición ecológica y el reto demográfico).
	
Una vez recopilada esta información, un administrador del proyecto a creado archivos por años que consisten en tablas donde se recogen todos estos datos segregados por meses, con el fin de tener los cuatros parámetros (existencias iniciales, producción, precios y precipitaciones) y sus datos en un solo archivo favoreciendo la unificación de datos teniendo asi por ejemplo en el archivo de 2017 los datos de existencias iniciales, producción, historial de precios y precipitaciones y no teniendo para 2017 un archivo Existencias_iniciales_2017, producción_2017, historial_de_precios_2017, precipitaciones_2017. Estas tablas se encontrarán en una base de datos/nube desde la cual el programa obtendrá los datos. Hemos creado un repositorio con estas tablas, puede verlo en este link: https://drive.google.com/drive/folders/1DiNHYz9lYGd2bsPEOehDSwywxTxof0-S?usp=sharing
	
El boletín del estado no emite los datos del mes actual hasta pasados 2 meses, por lo tanto si nos encontramos en Septiembre los últimos datos que tendremos serán los de Julio. Conforme vayan saliendo nuevos boletines el admin actualizará los archivos de tablas en la base de datos/nube añadiendo la siguiente celda/s del año actual con los datos obtenidos del boletín del estado y los links mencionados anteriormente con el fin de que la App tenga en cuenta los cambios.
Por ejemplo: Sale el boletín de Agosto de 2022 (año actual), entonces el admin editará la tabla de 2022 añadiendo una celda para Agosto con los parámetros de existencias iniciales, producción, precios y precipitaciones reflejados en el boletín.

## Lógica de negocio de OlivApp
La lógica de negocio de este sistema se basará en la extracción de información y la realización de predicciones de en que mes/meses el aceite de oliva obtendrá su mayor precio, teniendo en cuenta una serie de parámetros que el sistema evalúa. El modo en que el sistema hará sus predicciones(análisis de históricos, comparación de los datos del año actual con años anteriores, ....) lo encontramos en el punto redactado anteriormente "Planteamiento de la solución".

La lógica de negocio que va a utilizar la predicción consistirá en comparar los parámetros del año actual con el de los 5 años anteriores, entonces una vez calculado el año (de los 5 años anteriores) que más se parezca al actual evaluando los parámetros existencias iniciales, producción, precios y precipitaciones, se podrá predecir que al tener unas condiciones similares el precio máximo del aceite de oliva del año actual se obtendrá aproximadamente el mismo mes donde se dió en aquel año con el que comparte condiciones similares.

Si consultas este enlace podrás ver un ejemplo sencillo de la lógica que utilizará la predicción: https://drive.google.com/file/d/1Ye4p8LAOxUZfaJZf1GKAvwkFomqLv8VE/view?usp=sharing

## Herramientas de desarrollo

 - Gestor de dependencias: [poetry](https://github.com/joseantonio2001/OlivApp/issues/21)

 - Task runner: [PoethePoet](https://github.com/joseantonio2001/OlivApp/issues/22)
 
 
 	Se han desarrollado dos tareas, installPoetry y check en el fichero pyproject.toml que permiten instalar poetry y comprobar la correcta sintaxis de los fuente situados en /olivapp:
 	- **poe poetryInstall** e **poe check**:


	![CORRECTO_FUNCIONAMIENTO](https://user-images.githubusercontent.com/85243896/203502509-07ebc861-a752-4101-a044-d8b12ef543d2.png)

 - Test runner: [Pytest](https://github.com/joseantonio2001/OlivApp/issues/24)

 - Assertion Library: [assertpy](https://github.com/joseantonio2001/OlivApp/issues/25)

	

	Se han desarrollado 4 tests para verificar el correcto funcionamiento sel código implementado; Para ejecutarlos usaremos la orden **poe test**:
	![verificacion test](https://user-images.githubusercontent.com/85243896/204771235-25f6efe6-4ecb-4f71-a79f-a5674a8ffce2.png)

	
