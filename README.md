# Proyecto Tienda de Ropa con MongoDB

## Descripción

Este proyecto consiste en una base de datos para una tienda de ropa utilizando MongoDB.

La idea principal es poder guardar y manejar información relacionada con los usuarios, las marcas, las prendas disponibles y las ventas realizadas.

Dentro del archivo `database.js` se incluyen ejemplos para insertar datos, actualizar información, eliminar registros y realizar diferentes consultas sobre las ventas y el inventario.

El proyecto fue pensado con una estructura sencilla para poder entender mejor cómo trabajar con MongoDB y dejar una base que se pueda utilizar más adelante en una aplicación o una API.

## Tecnologías utilizadas

- MongoDB
- JavaScript
- GitHub
- Markdown

## Estructura del proyecto

```text
proyecto-tienda-ropa-mongodb/
│
├── database/
│   └── database.js
│
└── README.md
```

## Colecciones

La base de datos utiliza las siguientes colecciones:

- usuarios
- marcas
- prendas
- ventas

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

## Operaciones realizadas

En el archivo `database.js` se realizan diferentes operaciones para cada colección.

Las operaciones utilizadas son:

- `insertOne` para insertar un documento.
- `insertMany` para insertar varios documentos.
- `updateOne` para actualizar información.
- `deleteOne` para eliminar un documento.

## Consultas realizadas

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

## Integrantes

- Sebastian Coto
