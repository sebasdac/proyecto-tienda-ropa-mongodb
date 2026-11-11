# API de Tienda de Ropa (Proyecto 2)

API Flask + MongoDB. Mantiene la estructura de las colecciones `usuarios`, `marcas`, `prendas`, `ventas` del Proyecto 1.

## Cómo ejecutar

1. Iniciar MongoDB y crear/cargar la base `tiendaRopa` con el archivo `database/database.js` del repositorio original (usar MongoDB Shell/mongosh). **El script de ejemplo contiene inserciones; ejecutarlo varias veces duplica datos.**
2. Entrar a `API/` y crear un entorno virtual: `python -m venv venv`.
3. Activar en Windows: `venv\Scripts\activate` (PowerShell: `.\venv\Scripts\Activate.ps1`).
4. Instalar: `pip install -r requirements.txt`.
5. Copiar `.env.example` a `.env` y cambiar las credenciales y `JWT_SECRET` (no subir `.env`).
6. Ejecutar: `python run.py`.
7. Servidor: `http://127.0.0.1:5000`.

## Autenticación

`POST /api/v1/login` (es el único endpoint público; permite conseguir el token):

```json
{"usuario":"admin","contrasena":"la-clave-que-configuraste"}
```

Respuesta: `{"access_token":"...", "token_type":"Bearer", "expires_in":7200}`.
En Postman configurar **Authorization > Bearer Token** y pegar el valor de `access_token` para **todos** los endpoints de datos y reportes.

## CRUD por colección

Las siguientes rutas se implementan para **cada** recurso `usuarios`, `marcas`, `prendas`, `ventas`:

| Acción | Método | Ruta |
|---|---|---|
| Consultar todos | GET | `/api/v1/{recurso}` |
| Consultar por ID | GET | `/api/v1/{recurso}/{id}` |
| Crear | POST | `/api/v1/{recurso}` |
| Actualizar campos | PUT | `/api/v1/{recurso}/{id}` |
| Eliminar | DELETE | `/api/v1/{recurso}/{id}` |

El `id` es el `_id` de MongoDB (ObjectId) que devuelve el GET/POST. Para POST y PUT enviar `Content-Type: application/json`.

### Ejemplos POST (uno por modelo)

**Usuarios** — `POST /api/v1/usuarios`
```json
{"nombre":"Carlos Ramirez", "correo":"carlos@gmail.com", "telefono":"8888-8888"}
```

**Marcas** — `POST /api/v1/marcas`
```json
{"nombre":"Nike", "pais":"Estados Unidos"}
```

**Prendas** — `POST /api/v1/prendas`
```json
{"nombre":"Camiseta Oversize", "categoria":"Camiseta", "marca":"Nike", "talla":"M", "color":"Negro", "precio":15000, "stock":20}
```

**Ventas** — `POST /api/v1/ventas`
```json
{"fecha":"2026-10-01", "cliente":"Carlos Ramirez", "producto":"Camiseta Oversize", "marca":"Nike", "cantidad":2, "total":30000}
```

### Ejemplos GET, PUT y DELETE

- `GET /api/v1/prendas` obtiene prendas.
- `GET /api/v1/prendas/672aafc0fa12e0985b210001` consulta una prenda (reemplazar por ID real).
- `PUT /api/v1/prendas/672aafc0fa12e0985b210001` con `{"stock": 18}` actualiza el stock del documento.
- `DELETE /api/v1/prendas/672aafc0fa12e0985b210001` elimina ese documento.
- Cambiar `prendas` por `usuarios`, `marcas` o `ventas` para obtener las operaciones equivalentes.

## Reportes (todos requieren Bearer Token)

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/api/v1/reportes/marcas-con-ventas` | Marcas con al menos una venta |
| GET | `/api/v1/reportes/prendas-vendidas-stock` | Suma prendas vendidas por producto y resta a stock, como el Proyecto 1 |
| GET | `/api/v1/reportes/top-5-marcas` | 5 marcas con mayor suma de unidades vendidas |

**Nota de lógica:** el reporte de stock reproduce la consulta del Proyecto 1 (`stock - cantidadVendida`); la API no rebaja stock automáticamente cuando se crea una venta, para evitar descontarlo dos veces. Este API CRUD didáctico no implementa transacciones de inventario ni relaciones referenciales estrictas.

## Postman

Importar `postman/Tienda_Ropa_API.postman_collection.json` y luego editar las variables `baseUrl`, `usuario` y `contrasena`. Ejecutar primero **Login**; el script guardará el token de acceso en `token`. Después probar cada GET, POST, PUT y DELETE usando IDs reales de documentos. **Las operaciones POST/PUT/DELETE modifican la base**.

## Códigos HTTP

- `200`: consulta / actualización / eliminación exitosa.
- `201`: documento creado.
- `400`: datos o ID inválidos.
- `401`: token ausente, inválido o vencido.
- `404`: documento no encontrado.

La aplicación requiere MongoDB funcionando para consultar recursos o reportes.
