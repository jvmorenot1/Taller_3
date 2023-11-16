# API Taller_3

Instrucciones de despliegue:

1. Instalar virtualenv: `pip install virtualenv`

2. Crear el entorno: `python3 -m venv env`

3. Activar el entorno: `source env/bin/activate`

4. Instalar dependencias: `pip install -r requirements.txt`

5. Iniciar el servidor: `uvicorn main:app --reload`

6. Probar el servicio usando una herramienta como Postman:
**Servicio "Predict"**
    * URL: 127.0.0.1:8000/{version_modelo}/explain
**Servicio "Explain"**
    * URL: 127.0.0.1:8000/{version_modelo}/explain?num_features={num_features}
    En num_features se puede especificar la cantidad de variables que se espera obtener para la explicación del resultado. Este parámetro es opcional, y su valor por defecto es 3.
**Ejemplo cuerpo**

```
POST /predict HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json

[
	{
		"gender": "Female",
	    "SeniorCitizen": 0,
	    "Partner": "Yes",
	    "Dependents": "No",
	    "tenure": 1,
	    "PhoneService": "No",
	    "MultipleLines": "No phone service",
	    "InternetService": "DSL",
	    "OnlineSecurity": "No",
	    "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 29.85000,
        "TotalCharges": 29.85000
	},
	{
		"gender": "Female",
	    "SeniorCitizen": 0,
	    "Partner": "Yes",
	    "Dependents": "No",
	    "tenure": 1,
	    "PhoneService": "Yes",
	    "MultipleLines": "No phone service",
	    "InternetService": "DSL",
	    "OnlineSecurity": "No",
	    "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 29.85000,
        "TotalCharges": 29.85000
	}
]
```