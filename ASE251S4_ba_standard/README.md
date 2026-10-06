# Backend Analítico

Este proyecto corresponde a un backend analítico desarrollado en Python, organizado mediante una arquitectura por capas.

El objetivo de esta estructura es separar las responsabilidades del sistema para que el proyecto sea más ordenado, entendible y fácil de mantener.

---

# 1. Estructura del proyecto

```text
app/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── swagger.py
│
├── database/
│   ├── __init__.py
│   ├── mongodb.py
│   └── sqlserver.py
│
├── models/
│
├── repositories/
│   ├── mongodb/
│   │   ├── __init__.py
│   │   └── ejemplo_repository.py
│   │
│   ├── sqlserver/
│   │   ├── __init__.py
│   │   └── ejemplo_repository.py
│   │
│   └── __init__.py
│
├── routes/
│   ├── __init__.py
│   └── ejemplo_routes.py
│
├── schemas/
│   └── __init__.py
│
├── services/
│   ├── analytics/
│   │   ├── __init__.py
│   │   └── ejemplo_service.py
│   │
│   └── __init__.py
│
├── __init__.py
└── main.py

static/
└── swagger.json

tests/

.env.example
.gitignore
README.md
requirements.txt
```

---

# 2. Responsabilidades de cada capa

## `config/`

Contiene la configuración general del proyecto.

Aquí pueden ubicarse archivos relacionados con:

- Configuración de Swagger.
- Variables generales del sistema.
- Configuración del entorno.
- Parámetros de ejecución.

Ejemplo:

```text
config/
├── settings.py
└── swagger.py
```

---

## `database/`

Contiene la configuración de conexión con las bases de datos.

Ejemplo:

```text
database/
├── mongodb.py
└── sqlserver.py
```

Responsabilidad principal:

```text
Administrar las conexiones con las bases de datos.
```

---

## `models/`

Contiene los modelos utilizados por la aplicación.

Su implementación dependerá de las necesidades de cada proyecto.

Puede utilizarse para representar estructuras de datos o entidades del sistema.

---

## `repositories/`

La capa `repositories` se encarga del acceso a los datos.

Aquí deben realizarse las consultas hacia las bases de datos.

La estructura se separa según el motor utilizado:

```text
repositories/
├── mongodb/
└── sqlserver/
```

Responsabilidad principal:

```text
Consultar y devolver información desde la base de datos.
```

Ejemplo:

```python
def get_data():
    # Consulta a la base de datos
    pass
```

La lógica de cálculo o análisis no debe colocarse en esta capa.

---

## `repositories/mongodb/`

Contiene las consultas realizadas a MongoDB.

Ejemplo:

```text
repositories/mongodb/
└── ejemplo_repository.py
```

Cada equipo debe adaptar los nombres de sus archivos según las colecciones que utilice.

---

## `repositories/sqlserver/`

Contiene las consultas realizadas a SQL Server.

Ejemplo:

```text
repositories/sqlserver/
└── ejemplo_repository.py
```

Cada equipo debe adaptar los nombres de sus archivos según las tablas o datos que utilice.

---

## `services/`

La capa `services` contiene la lógica del sistema.

Aquí se procesan los datos obtenidos desde los repositories.

Responsabilidad principal:

```text
Procesar datos y aplicar lógica de negocio.
```

Aquí pueden realizarse:

- Cálculos.
- Conteos.
- Promedios.
- Agrupaciones.
- Comparaciones.
- Transformaciones.
- Indicadores.

---

## `services/analytics/`

Esta carpeta contiene los servicios relacionados con el análisis de datos y los indicadores.

Ejemplo:

```text
services/
└── analytics/
    └── ejemplo_service.py
```

Ejemplo:

```python
def calculate_indicator():
    # Obtener datos desde repository

    # Procesar información

    # Realizar cálculos

    # Retornar resultado

    pass
```

---

## `routes/`

Contiene las rutas o endpoints de la API.

Las rutas reciben las solicitudes HTTP y llaman a los services correspondientes.

Ejemplo:

```python
@blueprint.route("/analytics/ejemplo", methods=["GET"])
def get_indicator():
    result = service.calculate_indicator()
    return result
```

Responsabilidad principal:

```text
Recibir la petición
        ↓
Llamar al Service
        ↓
Retornar la respuesta
```

Las rutas no deben contener consultas directas a la base de datos ni cálculos complejos.

---

## `schemas/`

Puede utilizarse para definir o validar la estructura de los datos.

Puede servir para:

- Validar datos de entrada.
- Definir estructuras de respuesta.
- Validar campos obligatorios.
- Organizar tipos de datos.

Su implementación dependerá de las necesidades del proyecto.

---

## `static/`

Contiene archivos estáticos utilizados por el proyecto.

En este caso:

```text
static/
└── swagger.json
```

El archivo `swagger.json` contiene la documentación de los endpoints de la API.

---

## `tests/`

Contiene las pruebas del proyecto.

Aquí pueden agregarse pruebas para verificar:

- Services.
- Repositories.
- Endpoints.
- Funciones.
- Indicadores.

---

# 3. Flujo de la arquitectura

La aplicación debe seguir principalmente este flujo:

```text
CLIENTE
   ↓
ROUTE
   ↓
SERVICE
   ↓
REPOSITORY
   ↓
DATABASE
```

Cada capa tiene una responsabilidad específica.

---

# 4. Responsabilidad resumida de cada capa

```text
Route
↓
Recibe la petición HTTP.

Service
↓
Procesa la lógica y realiza los cálculos.

Repository
↓
Obtiene los datos desde la base de datos.

Database
↓
Administra la conexión.
```

---

# 5. Ejemplo de flujo

Supongamos que se necesita obtener un indicador.

El flujo podría ser:

```text
GET /analytics/ejemplo
        ↓
ejemplo_routes.py
        ↓
ejemplo_service.py
        ↓
ejemplo_repository.py
        ↓
MongoDB / SQL Server
```

Luego la información regresa:

```text
Base de datos
        ↓
Repository
        ↓
Service
        ↓
Route
        ↓
Respuesta JSON
```

---

# 6. Ejemplo de respuesta JSON

Una respuesta de la API podría tener la siguiente estructura:

```json
{
    "data": {
        "Categoria A": 10,
        "Categoria B": 8,
        "Categoria C": 15
    },
    "indicator": "Ejemplo de indicador"
}
```

El contenido de `data` dependerá del indicador desarrollado por cada equipo.

---

# 7. Swagger

Swagger permite documentar y probar los endpoints de la API desde una interfaz gráfica.

Desde Swagger se puede revisar:

- Método HTTP.
- Ruta.
- Parámetros.
- Código de respuesta.
- Respuesta JSON.
- Descripción del endpoint.

Ejemplo:

```text
GET /analytics/ejemplo
```

---

# 8. Importante sobre los nombres de archivos

Los siguientes nombres:

```text
ejemplo_repository.py
ejemplo_service.py
ejemplo_routes.py
```

son únicamente ejemplos.

No deben copiarse obligatoriamente.

Cada equipo debe nombrar sus archivos de acuerdo con:

- Sus colecciones de MongoDB.
- Sus tablas de SQL Server.
- Sus indicadores.
- Sus módulos.
- La lógica de su proyecto.

Por ejemplo, dos equipos pueden tener estructuras similares pero nombres completamente diferentes.

La arquitectura es común, pero la implementación depende de cada proyecto.

---

# 9. No colocar toda la lógica en un solo archivo

Evitar realizar todo dentro de las rutas.

Por ejemplo, no se recomienda:

```python
@blueprint.route("/analytics/ejemplo")
def ejemplo():

    # conexión
    # consulta
    # procesamiento
    # cálculos
    # respuesta

    pass
```

Esto mezcla demasiadas responsabilidades en un mismo lugar.

Se recomienda separar cada responsabilidad:

```text
Route
  ↓
Service
  ↓
Repository
  ↓
Database
```

Ejemplo:

```text
Route
→ recibe la solicitud

Service
→ procesa la información

Repository
→ consulta los datos

Database
→ administra la conexión
```

---

# 10. Buenas prácticas

Mantener las siguientes recomendaciones:

- Utilizar nombres claros.
- Separar las responsabilidades.
- Evitar duplicar código.
- No realizar consultas directamente desde las rutas.
- Colocar la lógica de análisis en `services`.
- Colocar las consultas en `repositories`.
- Mantener las conexiones en `database`.
- Documentar los endpoints.
- Probar las rutas antes de integrarlas.
- Mantener organizada la estructura del proyecto.
- Evitar archivos demasiado grandes.
- Crear funciones con una responsabilidad clara.
- No almacenar credenciales directamente en el código.

---

# 11. Archivo `.env`

Las credenciales y configuraciones sensibles no deben escribirse directamente dentro del código.

Ejemplo:

```env
MONGO_URI=mongodb://localhost:27017
MONGO_DB=nombre_basedatos

SQL_SERVER=localhost
SQL_DATABASE=nombre_basedatos
SQL_USER=usuario
SQL_PASSWORD=password
```

El archivo real:

```text
.env
```

no debe subirse al repositorio.

Debe agregarse al archivo:

```text
.gitignore
```

Ejemplo:

```text
.env
```

---

# 12. `.env.example`

El archivo:

```text
.env.example
```

sirve como referencia para indicar qué variables necesita el proyecto.

Ejemplo:

```env
MONGO_URI=
MONGO_DB=

SQL_SERVER=
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
```

Este archivo sí puede subirse al repositorio porque no contiene información sensible.

No colocar contraseñas reales dentro de `.env.example`.

---

# 13. Idea principal de la arquitectura

La estructura del proyecto debe ayudar a mantener separado:

```text
Configuración
        ↓
Conexión a datos
        ↓
Consultas
        ↓
Lógica de análisis
        ↓
Endpoints
```

La arquitectura es común para todos los equipos, pero los nombres de archivos, colecciones, tablas, indicadores y lógica deben adaptarse a cada proyecto.

El objetivo no es copiar exactamente los mismos archivos, sino comprender la responsabilidad de cada capa y mantener el proyecto organizado.