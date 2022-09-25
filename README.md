## OlivApp
Software para asesoramiento de venta de aceite a granel.

## Definición del problema
Este proyecto aborda el problema que tienen muchas empresas productoras y comercializadoras de aceite a granel a la hora de pronosticar el momento más idóneo para la venta de su producto con el fin de mejorar su rentabilidad.

Para conocer el mejor el problema se ha llevado a cabo una entrevista a un empleado de una cooperativa productora/comercializadora de aceite a granel( empresas a los que está dedicado el proyecto) el cuál nos ha descrito el problema, nos ha planteado cómo se solucionaría este de forma textual (“un sistema que realiza predicciones de cuando el aceite de oliva alcanza su mayor precio en el mercado”) y nos ha explicado aspectos importantes de la industria (“factores que hay que tener en cuenta para generar la predicción, ya que influyen en el precio del aceite de oliva en el mercado”).

## Cuales serían los usuarios/empresas que utilizarían este software
Empresas productoras y a su vez comercializadoras de aceite de oliva a granel (cooperativas oleícolas, almazaras privadas, productores particulares, compradores, agentes comerciales...).

## Planteamiento de la solución
El objetivo de la plataforma es que los usuarios tengan una idea lo más aproximada posible sobre que momento del año puede estar en su nivel más alto el precio del aceite de oliva en origen.

El programa descargará una serie de archivos de la nube para llevar a cabo su predicción. Estos archivos son históricos basados en tablas que recogen los datos de un parámetro deteminado(existencias iniciales, consumo, producción y precipitaciones) en cada mes de un año. Entonces el programa descargará un histórico del año actual de las existencias iniciales, del consumo, de la producción y de las precipitaciones (este parámatro aunque parezca que no pero será importante tenrlo en cuenta ya que influye en la producción de la cosecha) y descargará los mismos históricos pero de los 5/10 años anteriores. A partir de estos documentos el programa comparará los datos (existencias iniciales, consumo, producción y precipitaciones) del año actual con los de años anteriores y a partir de una serie de cálculos obtendrá cual sería el año más parecido al actual y a partir de ahí se basará para realizar su predicción; Esta predicción nos proporcionará en que época/meses del año el coste del aceite de oliva alcanza un mayor precio y por lo tanto sale más rentable su venta.
Así aunque un mes la predicción de la aplicación pueda ser p.ejemplo: "máx. coste del aceite de oliva se conseguirá en Julio", el mes siguiente la aplicaión puede cambiar su predicción debido a que hayan variado los factores que la aplicación evalúa para producir la predicción (por ejemplo las precipitaciones han aumentado y la producción ha bajado por lo que la situación actual se asemeja a la situción del año 2017(por ejemplo) donde el aceite de oliva alcanzo su máximo coste en Febrero, por lo que la predicción de la aplicación será ahora "máx. coste del aceite de oliva se conseguirá en Febrero").

El sistema utilizará la nube ya que el sistema accederá a una base de datos remota donde encotraremos los ficheros que contienen los datos que el sistema tiene en cuenta, y esos ficheros no serán constantes sino que sufrirán cambios (estos cambios los harán los admin del software; Este punto será explicado más abajo), por lo que siempre que se use el sistema, este consultará la nube para en caso de que haya nuevos datos sean cargados correctamente.

## ¿Porque querría una empresa utilizar OlivApp?
Los usuarios (empresas dedicadas a la producción y venta de aceite a granel, como ya hemos nombrado antes) usarían este sistema con el fin de incrementar su rentabilidad ya que si la empresa obtiene una predicción de en que meses el aceite alcanzará su mayor precio en mercado, esta podrá focalizar el mayor número de ventas en esos meses.

## En que datos/informes/información se respalda y fundamente la App
Recabando información de organismos oficiales como el COI (Comité Oleícola Internacional) Ministerio de Agricultura, Consejería de Agricultura, Poolred.

Los datos de existencias iniciales y consumo se obtienen de: 
	https://www.mapa.gob.es/es/agricultura/temas/producciones-agricolas/aceite-oliva-y-aceituna-mesa/Datos_produccion_movimiento_existencias_AICA.aspx
	https://www.mapa.gob.es/es/agricultura/temas/producciones-agricolas/informemensualdelasituaciondemercadodelsectordelaceitedeolivayaceitunademesa_julio2022_tcm30-626970.pdf
	(Boletín del ministerio de agricultura, pesca y alimentación).
Los datos de historial de precios se obtiene de:
	https://www.oliva.net/poolred/ErrorPOOL.aspx?TipoError=acceso&ReturnUrl=%2fpoolred%2fVendedor%2fPreciosMediosVendedor.aspx (POOLred es un Sistema de Información en origen del aceite de oliva).
	PD: Para acceder a los datos de esta web se necesitará una cuenta dada de alta, que poseen las empresas productoras/comercializadoras de aceite de Oliva. A los desarrolladores del proyecto una empresa nos ha facilitado una clave, sin embargo adjuntamos un enlace que hemos creado donde podrás ver todos los datos que nos muestra esta web para validar su credibilidad: https://drive.google.com/drive/folders/1NoHETB7DiNCrkIhI1mxrwzDKXJGJAeNA?usp=sharing
Los datos de precipitaciones se obtienen de: 
	https://www.seprem.es/boletin/lluvia.pdf (Boletín del ministerio para la transición ecológica y el reto demográfico).
	
Una vez recopilada esta información, un administrador del proyecto a creado archivos por años que consisten en tablas donde se recogen todos estos datos segregados por meses, con el fin de tener los cuatros parámetros (existencias iniciales, producción, precios y precipitaciones) y sus datos en un solo archivo favoreciendo la unificación de datos teniendo asi por ejemplo en el archivo de 2017 los datos de existencias iniciales, producción, historial de precios y precipitaciones y no teniendo para 2017 un archivo Existencias_iniciales_2017, producción_2017, historial_de_precios_2017, precipitaciones_2017. Estas tablas se encontrarán en una base de datos/nube desde la cual el programa obtendrá los datos. Hemos creado un repositorio con estas tablas, puede verlo en este link: https://drive.google.com/drive/folders/1DiNHYz9lYGd2bsPEOehDSwywxTxof0-S?usp=sharing
	
El boletín del estado no emite los datos del mes actual hasta pasados 2 meses, por lo tanto si nos encontramos en Septiembre los últimos datos que tendremos serán los de Julio. Conforme vayan saliendo nuevos boletines el admin actualizará los archivos de tablas en la base de datos/nube añadiendo la siguiente celda/s del año actual con los datos obtenidos del boletín del estado y los links mencionados anteriormente con el fin de que la App tenga en cuenta los cambios.
Por ejemplo: Sale el boletín de Agosto de 2022 (año actual), entonces el admin editará la tabla de 2022 añadiendo una celda para Agosto con los parámetros de existencias iniciales, producción, precios y precipitaciones reflejados en el boletín.

## Lógica de negocio de OlivApp
La lógica de negocio de este sistema se basará en la extracción de información y la realización de predicciones de en que mes/meses el aceite de oliva obtendrá su mayor precio, teniendo en cuenta una serie de parámetros que el sistema evalúa. El modo en que el sistema hará sus predicciones(análisis de históricos, comparación de los datos del año actual con años anteriores, ....) lo encontramos en el punto redactado anteriormente "Planteamiento de la solución".

La lógica de negocio que va a utilizar la predicción consistirá en comparar los parámetros del año actual con el de los 5 años anteriores, entonces una vez calculado el año (de los 5 años anetriores) que más se parezca al actual evaluando los parámetros existencias iniciales, producción, precios y precipitaciones, se podrá predecir que al tener unas condiciones similares el precio máximo del aceite de oliva del año actual se obtendrá aproximadamente el mismo mes donde se dió en aquel año con el que comparte condiciones similares.

Haciendo un ejemplo muy simple (solo evaluando el mes de Enero y dos años atrás; El sistema evaluará 5 años atrás y todos los meses hasta el mes que nos encontremos pero por simplicidad realizaremos hasta enero) de como realizaría el sistema los cálculos:
				2022 (Año Actual)		2021 (precio máx del aceite se alcanzó en Marzo)		2020 (precio máx del aceite se alcanzó en Agosto)
				Enero				Enero                                                         Enero
Existencias iniciales		3				2	-> 3 - 2 = 1						5	-> 3 - 5 = 2			//Calculos del valor
Producción			6				8	-> 6 - 8 = 2						3	-> 6 - 3 = 3			//actual con el de ese año en valor absoluto	
Precio Aceite de Oliva		8				9	-> 8 - 9 = 1						5	-> 8 - 5 = 3
Precipitaciones		4				1	-> 4 - 2 = 3						2	-> 4 - 2 = 2	
 										 = 7								 = 8			//Suma de la diferencia
 Vemos que el año 2021 muestra una menor diferencia con 2022 que 2020 (sus valores tienen una menor diferencia con los valores de 2022 que los de 2020) por lo tanto la predicción del sistema será la siguiente: "Por su similitud con los datos del 2021 en 2022 el precio máximo del aceite de oliva en el mercado se alcanzará aproximadamente en Marzo".

