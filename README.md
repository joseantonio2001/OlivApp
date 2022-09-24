## OlivApp
Software para asesoramiento de venta de aceite a granel.

## Definición del problema
Este proyecto aborda el problema que tienen muchas empresas productoras y comercializadoras de aceite a granel a la hora de pronosticar el momento más idóneo para la venta de su producto con el fin de mejorar su rentabilidad.

## Cuales serían los usuarios/empresas que utilizarían este software
Empresas productoras y a su vez comercializadoras de aceite de oliva a granel (cooperativas oleícolas, almazaras privadas, productores particulares, compradores, agentes comerciales...).

## Planteamiento de la solución
El objetivo de la plataforma es que los usuarios tengan una idea lo más aproximada posible sobre que momento del año puede estar en su nivel más alto el precio del aceite de oliva en origen.

El programa descargará una serie de archivos de la nube para llevar a cabo su predicción. Estos archivos son históricos basados en tablas que recogen los datos de un parámetro deteminado(existencias iniciales, consumo, producción y precipitaciones) en cada mes de un año. Entonces el programa descargará un histórico del año actual de las existencias iniciales, del consumo, de la producción y de las precipitaciones (este parámatro aunque parezca que no pero será importante tenrlo en cuenta ya que influye en la producción de la cosecha) y descargará los mismos históricos pero de los 5/10 años anteriores. A partir de estos documentos el programa comparará los datos (existencias iniciales, consumo, producción y precipitaciones) del año actual con los de años anteriores y a partir de una serie de cálculos obtendrá cual sería el año más parecido al actual y a partir de ahí se basará para realizar su predicción; Esta predicción nos proporcionará en que época/meses del año el coste del aceite de oliva alcanza un mayor precio y por lo tanto sale más rentable su venta.
Así aunque un mes la predicción de la aplicación pueda ser p.ejemplo: "máx. coste del aceite de oliva se conseguirá en Julio", el mes siguiente la aplicaión puede cambiar su predicción debido a que hayan variado los factores que la aplicación evalúa para producir la predicción (por ejemplo las precipitaciones han aumentado y la producción ha bajado por lo que la situación actual se asemeja a la situción del año 2017(por ejemplo) donde el aceite de oliva alcanzo su máximo coste en Febrero, por lo que la predicción de la aplicación será ahora "máx. coste del aceite de oliva se conseguirá en Febrero").

## ¿Porque querría una empresa utilizar OlivApp?
Los usuarios (empresas dedicadas a la producción y venta de aceite a granel, como ya hemos nombrado antes) usarían este sistema con el fin de incrementar su rentabilidad ya que si la empresa obtiene una predicción de en que meses el aceite alcanzará su mayor precio en mercado, esta podrá focalizar el mayor número de ventas en esos meses.

## En que datos/informes/información se respalda y fundamente la App
Recabando información de organismos oficiales como el COI (Comité Oleícola Internacional) Ministerio de Agricultura, Consejería de Agricultura, Poolred.

## Lógica de negocio de OlivApp
La lógica de negocio de este sistema se basará en la estracción de información y la realización de predicciones de en que mes/meses el aceite de oliva a granel obtendrá su mayor precio, teniendo en cuenta una serie de parámetros que el sistema evalua. El modo en que el sistema hará sus predicciones(análisis de históricos, comparación de los datos del año actual con años anteriores, ....) lo encontramos en el punto redactado anteriormente "Planteamiento de la solución".
