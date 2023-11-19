# Taller_3
Enlace a Youtube con el video de la prueba de la API REST:

https://www.youtube.com/watch?v=BpOR62Po-9M&feature=youtu.be

# Integrantes
-Yachay Tolosa Bello – 202315750

-Kevin Infante Hernández – 201117324​

-John Vicente Moreno Triviño – 202210162

Este repositorio contiene los entregables correspondientes al Taller 3 de la asignatura Ciencia de Datos Aplicada. A continuación, se describe el contenido:

1. El notebook "Taller3-Modelos_Clasificación.ipynb" contiene todo lo relativo al entendimiento y preparación de datos, el desarrollo del modelo base y la búsqueda del mejor modelo mediante pipelines y grids, encapsulando así los modelos generados. En este notebook se dan las explicaciones y respuestas a las cuestiones planteadas en los puntos 1, 2 y 3 del taller.
2. El script "transformersMethods.py" contiene una función simple de transformación de datos vacíos, la cual es consumida por los pipelines de búsqueda de los mejores modelos en el notebook y por la API.
3. La carpeta "Dataset" contiene los conjuntos de datos históricos y futuros utilizados en este ejercicio.
4. La carpeta "Modelos (joblib)" contiene los modelos generados: el modelo base ("churn-v1_Base.joblib") y el mejor modelo basado en XGBoost ("churn-v2_XGB_Best.joblib").
5. La carpeta "API" contiene todos los scripts desarrollados para la implementación de la API REST con dos endpoints, junto con un archivo "Readme" con las instrucciones para su despliegue y un archivo de especificación de requerimientos. El link del video de la API se encuentra al principio del presente archivo, cumpliendo así con lo solicitado en el punto 4 del taller.
6. El notebook "AB-Testing.ipynb" contiene todo lo relativo al proceso del TEST A/B, junto con la explicación de los resultados obtenidos y la respuesta a las preguntas planteadas el punto 5 del taller.
