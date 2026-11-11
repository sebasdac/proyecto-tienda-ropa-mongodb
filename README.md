# Proyecto Tienda de Ropa con MongoDB

## Descripción

Este proyecto consiste en una base de datos para una tienda de ropa utilizando MongoDB.

La idea principal es poder guardar y manejar información relacionada con los usuarios, las marcas, las prendas disponibles y las ventas realizadas.

En el **Proyecto 1**, el archivo `database/database.js` incluye ejemplos para insertar datos, actualizar información, eliminar registros y realizar diferentes consultas sobre las ventas y el inventario.

En el **Proyecto 2**, se agregó una API REST con Python y Flask para consultar y modificar las mismas colecciones desde Postman. La API utiliza una estructura por capas, trabaja con MongoDB y protege sus endpoints mediante autenticación con Bearer Token.

## Tecnologías utilizadas

- MongoDB
- JavaScript (script original de base de datos)
- Python
- Flask
- PyMongo
- PyJWT (tokens de autenticación)
- Postman
- GitHub
- Markdown

## Estructura del proyecto

```text
proyecto-tienda-ropa-mongodb/
│
├── database/
│   └── database.js
│
├── API/
│   ├── app/
│   │   ├── controllers/
│   │   │   ├── usuarios.py
│   │   │   ├── marcas.py
│   │   │   ├── prendas.py
│   │   │   └── ventas.py
│   │   ├── models/
│   │   │   ├── usuario.py
│   │   │   ├── marca.py
│   │   │   ├── prenda.py
│   │   │   └── venta.py
│   │   ├── services/
│   │   │   ├── mongo_service.py
│   │   │   └── seguridad.py
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   └── reportes.py
│   │   └── __init__.py
│   ├── postman/
│   │   └── Tienda_Ropa_API.postman_collection.json
│   ├── .env.example
│   ├── requirements.txt
│   ├── README.md
│   └── run.py
│
├── .gitignore
└── README.md
```

La API está dividida en modelos, controladores, servicios y rutas. No incluye una interfaz gráfica: las peticiones se realizan con Postman u otro cliente HTTP.

## Colecciones

La base de datos utiliza las siguientes colecciones:

- `usuarios`
- `marcas`
- `prendas`
- `ventas`

---

## Ejemplo de la colección usuarios

Esta colección guarda información básica de los usuarios o clientes de la tienda.

```json
{
  "nombre": "Carlos Ramirez",
  "correo": "carlos@gmail.com",
  "telefono": "8888-8888"
}
```

---

## Ejemplo de la colección marcas

Esta colección guarda las marcas que se manejan en la tienda.

```json
{
  "nombre": "Nike",
  "pais": "Estados Unidos"
}
```

---

## Ejemplo de la colección prendas

Esta colección guarda la información de las prendas disponibles en la tienda.

```json
{
  "nombre": "Camiseta Oversize",
  "categoria": "Camiseta",
  "marca": "Nike",
  "talla": "M",
  "color": "Negro",
  "precio": 15000,
  "stock": 20
}
```

---

## Ejemplo de la colección ventas

Esta colección guarda la información de las ventas realizadas.

```json
{
  "fecha": "2026-10-01",
  "cliente": "Carlos Ramirez",
  "producto": "Camiseta Oversize",
  "marca": "Nike",
  "cantidad": 2,
  "total": 30000
}
```

---

## Operaciones realizadas en MongoDB (Proyecto 1)

En el archivo `database.js` se realizan diferentes operaciones para cada colección.

Las operaciones utilizadas son:

- `insertOne` para insertar un documento.
- `insertMany` para insertar varios documentos.
- `updateOne` para actualizar información.
- `deleteOne` para eliminar un documento.

## Consultas realizadas en el Proyecto 1

El proyecto también incluye las consultas solicitadas para trabajar con la información de las ventas.

1. Obtener la cantidad de prendas vendidas por fecha.
2. Obtener la cantidad de prendas vendidas en una fecha específica.
3. Obtener la lista de marcas que tienen al menos una venta.
4. Obtener las prendas vendidas y calcular la cantidad restante en stock.
5. Obtener las 5 marcas más vendidas y su cantidad de ventas.

## Base de datos

El nombre de la base de datos utilizada es:

```text
tiendaRopa
```

Es importante escribir el nombre exactamente así, ya que MongoDB considera `tiendaRopa` y `tienda-ropa` como bases de datos diferentes.

---

# Proyecto 2: API REST con Flask y MongoDB

## Objetivo

Desarrollar una API que permita realizar operaciones CRUD (crear, consultar, actualizar y eliminar) sobre cada colección de la tienda. También permite obtener los tres reportes solicitados y utiliza autenticación por token para proteger las peticiones.

## Instalación y ejecución

**Requisitos:** Python, MongoDB Server en ejecución, MongoDB Shell (`mongosh`) y Postman.

1. Descargar o clonar el repositorio.
2. Iniciar MongoDB localmente en `mongodb://localhost:27017/`.
3. Si la base de datos está vacía, cargar el script original desde la raíz del repositorio:

   ```powershell
   mongosh "mongodb://127.0.0.1:27017" --file ".\database\database.js"
   ```

   **Atención:** el script original contiene inserciones y modificaciones; no ejecutarlo repetidamente sobre datos ya cargados, porque puede producir duplicados.

4. Entrar en la carpeta de la API y preparar el entorno virtual en Windows (PowerShell):

   ```powershell
   cd API
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

5. Crear `API/.env` a partir de `API/.env.example`. Configurar las variables (los valores de usuario, contraseña y secreto deben ser propios):

   ```dotenv
   MONGO_URI=mongodb://localhost:27017/
   MONGO_DB=tiendaRopa
   API_USERNAME=admin
   API_PASSWORD=tu-contrasena-local
   JWT_SECRET=una-clave-larga-y-aleatoria
   PORT=5000
   ```

   El archivo `.env` no debe subirse a GitHub.

6. Ejecutar la API desde la carpeta `API`:

   ```powershell
   python run.py
   ```

La dirección local de la API es **`http://127.0.0.1:5000`**.

## Autenticación con Bearer Token

Antes de usar los endpoints de usuarios, marcas, prendas, ventas o reportes, es necesario obtener un token. El único endpoint público es el de inicio de sesión.

### Iniciar sesión

- **Método:** `POST`
- **URL:** `http://127.0.0.1:5000/api/v1/login`
- **Body** (`raw` → `JSON`):

```json
{
  "usuario": "admin",
  "contrasena": "tu-contrasena-local"
}
```

Respuesta exitosa de ejemplo:

```json
{
  "access_token": "<token_generado_por_la_api>",
  "token_type": "Bearer",
  "expires_in": 7200
}
```

Para las demás peticiones, configurar en Postman **Authorization → Bearer Token** y usar el valor de `access_token`. También se puede enviar el encabezado:

```http
Authorization: Bearer <token_generado_por_la_api>
```

La colección de Postman incluida en el proyecto almacena automáticamente el token cuando el Login responde correctamente.

## Endpoints de usuarios

Permiten administrar los datos de los clientes o usuarios de la tienda.

| Operación | Método | URL |
|---|---|---|
| Consultar todos | GET | `/api/v1/usuarios` |
| Consultar por ID | GET | `/api/v1/usuarios/{id}` |
| Insertar | POST | `/api/v1/usuarios` |
| Actualizar | PUT | `/api/v1/usuarios/{id}` |
| Eliminar | DELETE | `/api/v1/usuarios/{id}` |

**Ejemplo para insertar (`POST /api/v1/usuarios`):**

```json
{
  "nombre": "Cliente de prueba",
  "correo": "prueba@example.com",
  "telefono": "8888-1111"
}
```

**Ejemplo para actualizar (`PUT /api/v1/usuarios/{id}`):**

```json
{
  "nombre": "Nombre actualizado"
}
```

## Endpoints de marcas

Permiten administrar las marcas de prendas disponibles en la tienda.

| Operación | Método | URL |
|---|---|---|
| Consultar todas | GET | `/api/v1/marcas` |
| Consultar por ID | GET | `/api/v1/marcas/{id}` |
| Insertar | POST | `/api/v1/marcas` |
| Actualizar | PUT | `/api/v1/marcas/{id}` |
| Eliminar | DELETE | `/api/v1/marcas/{id}` |

**Ejemplo para insertar (`POST /api/v1/marcas`):**

```json
{
  "nombre": "Marca Prueba",
  "pais": "Costa Rica"
}
```

**Ejemplo para actualizar (`PUT /api/v1/marcas/{id}`):**

```json
{
  "nombre": "Nombre actualizado"
}
```

## Endpoints de prendas

Permiten consultar y administrar el inventario de ropa, incluyendo precio, talla, color y stock.

| Operación | Método | URL |
|---|---|---|
| Consultar todas | GET | `/api/v1/prendas` |
| Consultar por ID | GET | `/api/v1/prendas/{id}` |
| Insertar | POST | `/api/v1/prendas` |
| Actualizar | PUT | `/api/v1/prendas/{id}` |
| Eliminar | DELETE | `/api/v1/prendas/{id}` |

**Ejemplo para insertar (`POST /api/v1/prendas`):**

```json
{
  "nombre": "Prenda de prueba",
  "categoria": "Camiseta",
  "marca": "Marca Prueba",
  "talla": "M",
  "color": "Azul",
  "precio": 10000,
  "stock": 10
}
```

**Ejemplo para actualizar (`PUT /api/v1/prendas/{id}`):**

```json
{
  "stock": 8
}
```

## Endpoints de ventas

Permiten consultar y administrar los registros de ventas realizadas.

| Operación | Método | URL |
|---|---|---|
| Consultar todas | GET | `/api/v1/ventas` |
| Consultar por ID | GET | `/api/v1/ventas/{id}` |
| Insertar | POST | `/api/v1/ventas` |
| Actualizar | PUT | `/api/v1/ventas/{id}` |
| Eliminar | DELETE | `/api/v1/ventas/{id}` |

**Ejemplo para insertar (`POST /api/v1/ventas`):**

```json
{
  "fecha": "2026-11-11",
  "cliente": "Cliente de prueba",
  "producto": "Prenda de prueba",
  "marca": "Marca Prueba",
  "cantidad": 1,
  "total": 10000
}
```

**Ejemplo para actualizar (`PUT /api/v1/ventas/{id}`):**

```json
{
  "cantidad": 2
}
```

### Cómo utilizar las operaciones CRUD

- Para **GET general**, basta enviar la petición a la ruta de la colección.
- Para **GET por ID**, **PUT** y **DELETE**, reemplazar `{id}` por el `_id` real devuelto por MongoDB (por ejemplo, al consultar o insertar un documento).
- Para **POST** y **PUT**, seleccionar `Body → raw → JSON` en Postman y enviar `Content-Type: application/json`.
- Las operaciones de escritura modifican los documentos almacenados en MongoDB.

## Endpoints de reportes

La API incluye los tres reportes solicitados en el Proyecto 2. Todos utilizan el método `GET` y requieren Bearer Token.

### 1. Marcas con al menos una venta

- **Método:** `GET`
- **URL:** `http://127.0.0.1:5000/api/v1/reportes/marcas-con-ventas`
- **Descripción:** agrupa las ventas por marca y devuelve las marcas que aparecen en los registros de venta.

Ejemplo de respuesta:

```json
[
  {"marca": "Adidas"},
  {"marca": "Nike"},
  {"marca": "Puma"}
]
```

### 2. Prendas vendidas y cantidad restante en stock

- **Método:** `GET`
- **URL:** `http://127.0.0.1:5000/api/v1/reportes/prendas-vendidas-stock`
- **Descripción:** suma las unidades vendidas por nombre de producto, relaciona ese nombre con la colección de prendas y calcula `stock - cantidadVendida`.

Ejemplo ilustrativo de respuesta:

```json
[
  {
    "prenda": "Camiseta Oversize",
    "cantidadVendida": 4,
    "stockRestante": 21
  }
]
```

**Nota:** para relacionar las colecciones, `ventas.producto` debe coincidir exactamente con `prendas.nombre`. El sistema no descuenta automáticamente las unidades del stock al registrar una venta: el cálculo se realiza en este reporte, de acuerdo con la lógica del Proyecto 1.

### 3. Cinco marcas más vendidas

- **Método:** `GET`
- **URL:** `http://127.0.0.1:5000/api/v1/reportes/top-5-marcas`
- **Descripción:** agrupa las ventas por marca, suma las cantidades vendidas y muestra como máximo cinco marcas, ordenadas de mayor a menor.

Ejemplo ilustrativo de respuesta:

```json
[
  {"marca": "Nike", "cantidadVendida": 7},
  {"marca": "Adidas", "cantidadVendida": 3},
  {"marca": "Puma", "cantidadVendida": 2}
]
```

Los ejemplos muestran el formato esperado; los valores reales dependen de los documentos guardados en MongoDB.

## Pruebas de la API con Postman

En la carpeta `API/postman/` se encuentra la colección `Tienda_Ropa_API.postman_collection.json`, que contiene 24 peticiones: un Login, cinco operaciones por cada una de las cuatro colecciones y tres reportes.

Para probarla:

1. Abrir Postman y seleccionar **Import**.
2. Importar `API/postman/Tienda_Ropa_API.postman_collection.json`.
3. Configurar las variables de colección:
   - `baseUrl`: `http://127.0.0.1:5000`
   - `usuario`: el valor de `API_USERNAME` en `.env`
   - `contrasena`: el valor de `API_PASSWORD` en `.env`
4. Ejecutar **Login - obtener token**. La colección guarda `access_token` en la variable `token`.
5. Ejecutar **Obtener todos** de usuarios, marcas, prendas y ventas.
6. Probar **Crear**, **Obtener por ID**, **Actualizar** y **Eliminar** con registros de prueba. La variable `id` puede actualizarse después de crear un documento.
7. Ejecutar los tres reportes y comprobar que devuelvan información.
8. Probar un endpoint protegido sin Bearer Token para verificar que la API rechace el acceso.

**Importante:** las operaciones POST, PUT y DELETE cambian la base de datos. Se recomienda utilizar registros de prueba.

## Códigos de respuesta HTTP

| Código | Significado |
|---|---|
| `200 OK` | Consulta, actualización o eliminación exitosa. |
| `201 Created` | Documento creado correctamente. |
| `400 Bad Request` | Datos o identificador no válido. |
| `401 Unauthorized` | Credenciales incorrectas o token ausente, inválido o vencido. |
| `404 Not Found` | Documento o ruta no encontrado. |

## Consideraciones

- La API utiliza una arquitectura por capas y modelos separados para cada colección.
- Es necesario mantener el servidor MongoDB en ejecución para realizar las consultas.
- La base configurada en `.env` debe ser la misma que contiene los datos (`tiendaRopa`).
- El token es obligatorio para los endpoints de datos y reportes; el Login es público para permitir obtenerlo.
- El proyecto está orientado a prácticas de API y MongoDB; no incorpora una interfaz gráfica ni un sistema de inventario transaccional.
- No deben subirse archivos `.env`, entornos virtuales ni contraseñas al repositorio público.

## Integrantes

- Sebastian Coto
