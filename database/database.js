// ======================================================
// CREACION DE LA BASE DE DATOS
// ======================================================

// Creamos o seleccionamos la base de datos de la tienda
use("tiendaRopa");


// ======================================================
// CREACION DE COLECCIONES
// ======================================================

db.createCollection("usuarios");
db.createCollection("marcas");
db.createCollection("prendas");
db.createCollection("ventas");


// ======================================================
// COLECCION: USUARIOS
// ======================================================

// Insertar un usuario
db.usuarios.insertOne({
    nombre: "Carlos Ramirez",
    correo: "carlos@gmail.com",
    telefono: "8888-8888"
});

// Insertar varios usuarios
db.usuarios.insertMany([
    {
        nombre: "Andrea Solano",
        correo: "andrea@gmail.com",
        telefono: "8777-1111"
    },
    {
        nombre: "Luis Vargas",
        correo: "luis@gmail.com",
        telefono: "8666-2222"
    },
    {
        nombre: "Maria Fernandez",
        correo: "maria@gmail.com",
        telefono: "8555-3333"
    }
]);

// Actualizar un usuario
db.usuarios.updateOne(
    { correo: "carlos@gmail.com" },
    {
        $set: {
            telefono: "8999-9999"
        }
    }
);

// Eliminar un usuario
db.usuarios.deleteOne({
    correo: "maria@gmail.com"
});


// ======================================================
// COLECCION: MARCAS
// ======================================================

// Insertar una marca
db.marcas.insertOne({
    nombre: "Nike",
    pais: "Estados Unidos"
});

// Insertar varias marcas
db.marcas.insertMany([
    {
        nombre: "Adidas",
        pais: "Alemania"
    },
    {
        nombre: "Puma",
        pais: "Alemania"
    },
    {
        nombre: "Zara",
        pais: "España"
    },
    {
        nombre: "Levis",
        pais: "Estados Unidos"
    },
    {
        nombre: "H&M",
        pais: "Suecia"
    }
]);

// Actualizar una marca
db.marcas.updateOne(
    { nombre: "Puma" },
    {
        $set: {
            activo: true
        }
    }
);

// Eliminar una marca
db.marcas.deleteOne({
    nombre: "H&M"
});


// ======================================================
// COLECCION: PRENDAS
// ======================================================

// Insertar una prenda
db.prendas.insertOne({
    nombre: "Camiseta Oversize",
    categoria: "Camiseta",
    marca: "Nike",
    talla: "M",
    color: "Negro",
    precio: 15000,
    stock: 20
});

// Insertar varias prendas
db.prendas.insertMany([
    {
        nombre: "Sudadera Deportiva",
        categoria: "Sudadera",
        marca: "Adidas",
        talla: "L",
        color: "Gris",
        precio: 28000,
        stock: 15
    },
    {
        nombre: "Pantalon Jogger",
        categoria: "Pantalon",
        marca: "Puma",
        talla: "M",
        color: "Negro",
        precio: 22000,
        stock: 18
    },
    {
        nombre: "Jeans Clasicos",
        categoria: "Jeans",
        marca: "Levis",
        talla: "32",
        color: "Azul",
        precio: 32000,
        stock: 12
    },
    {
        nombre: "Camiseta Basica",
        categoria: "Camiseta",
        marca: "Zara",
        talla: "S",
        color: "Blanco",
        precio: 12000,
        stock: 25
    },
    {
        nombre: "Short Deportivo",
        categoria: "Short",
        marca: "Nike",
        talla: "M",
        color: "Azul",
        precio: 18000,
        stock: 10
    }
]);

// Actualizar una prenda
db.prendas.updateOne(
    { nombre: "Camiseta Oversize" },
    {
        $set: {
            stock: 25
        }
    }
);

// Eliminar una prenda
db.prendas.deleteOne({
    nombre: "Camiseta Basica"
});


// ======================================================
// COLECCION: VENTAS
// ======================================================

// Insertar una venta
db.ventas.insertOne({
    fecha: new Date("2026-10-01"),
    cliente: "Carlos Ramirez",
    producto: "Camiseta Oversize",
    marca: "Nike",
    cantidad: 2,
    total: 30000
});

// Insertar varias ventas
db.ventas.insertMany([
    {
        fecha: new Date("2026-10-02"),
        cliente: "Andrea Solano",
        producto: "Sudadera Deportiva",
        marca: "Adidas",
        cantidad: 1,
        total: 28000
    },
    {
        fecha: new Date("2026-10-03"),
        cliente: "Luis Vargas",
        producto: "Pantalon Jogger",
        marca: "Puma",
        cantidad: 2,
        total: 44000
    },
    {
        fecha: new Date("2026-10-03"),
        cliente: "Carlos Ramirez",
        producto: "Jeans Clasicos",
        marca: "Levis",
        cantidad: 1,
        total: 32000
    },
    {
        fecha: new Date("2026-10-04"),
        cliente: "Andrea Solano",
        producto: "Short Deportivo",
        marca: "Nike",
        cantidad: 3,
        total: 54000
    },
    {
        fecha: new Date("2026-10-05"),
        cliente: "Luis Vargas",
        producto: "Camiseta Oversize",
        marca: "Nike",
        cantidad: 1,
        total: 15000
    },
    {
        fecha: new Date("2026-10-05"),
        cliente: "Carlos Ramirez",
        producto: "Sudadera Deportiva",
        marca: "Adidas",
        cantidad: 2,
        total: 56000
    }
]);

// Actualizar una venta
db.ventas.updateOne(
    {
        cliente: "Luis Vargas",
        producto: "Camiseta Oversize"
    },
    {
        $set: {
            cantidad: 2,
            total: 30000
        }
    }
);

// Eliminar una venta
db.ventas.deleteOne({
    cliente: "Carlos Ramirez",
    producto: "Jeans Clasicos"
});


// ======================================================
// CONSULTAS
// ======================================================


// ------------------------------------------------------
// CONSULTA 1
// Obtener la cantidad de prendas vendidas por fecha
// ------------------------------------------------------

db.ventas.aggregate([
    {
        $group: {
            _id: "$fecha",
            cantidadVendida: {
                $sum: "$cantidad"
            }
        }
    },
    {
        $sort: {
            _id: 1
        }
    }
]);


// ------------------------------------------------------
// CONSULTA 1.1
// Obtener la cantidad de prendas vendidas en una fecha
// especifica
// ------------------------------------------------------

db.ventas.aggregate([
    {
        $match: {
            fecha: new Date("2026-10-05")
        }
    },
    {
        $group: {
            _id: "$fecha",
            cantidadVendida: {
                $sum: "$cantidad"
            }
        }
    }
]);


// ------------------------------------------------------
// CONSULTA 2
// Obtener la lista de todas las marcas que tienen
// al menos una venta
// ------------------------------------------------------

db.ventas.aggregate([
    {
        $group: {
            _id: "$marca"
        }
    },
    {
        $sort: {
            _id: 1
        }
    }
]);


// ------------------------------------------------------
// CONSULTA 3
// Obtener las prendas vendidas y calcular la cantidad
// restante en stock
// ------------------------------------------------------

db.ventas.aggregate([
    {
        $group: {
            _id: "$producto",
            cantidadVendida: {
                $sum: "$cantidad"
            }
        }
    },
    {
        $lookup: {
            from: "prendas",
            localField: "_id",
            foreignField: "nombre",
            as: "datosPrenda"
        }
    },
    {
        $unwind: "$datosPrenda"
    },
    {
        $project: {
            _id: 0,
            prenda: "$_id",
            cantidadVendida: 1,
            stockRestante: {
                $subtract: [
                    "$datosPrenda.stock",
                    "$cantidadVendida"
                ]
            }
        }
    }
]);


// ------------------------------------------------------
// CONSULTA 4
// Obtener las 5 marcas mas vendidas y su cantidad
// de ventas
// ------------------------------------------------------

db.ventas.aggregate([
    {
        $group: {
            _id: "$marca",
            cantidadVendida: {
                $sum: "$cantidad"
            }
        }
    },
    {
        $sort: {
            cantidadVendida: -1
        }
    },
    {
        $limit: 5
    }
]);
