import pandas as pd
import numpy as np
import random 
from faker import Faker
import os

fake = Faker("es_MX")

clientes = []
for i in range(1, 101):
    clientes.append({
        "id_cliente": i,
        "nombre": fake.name(),
        "email": fake.email(),
        "telefono": fake.phone_number(),
        "direccion": fake.address()
    })

categorias = ["book", "tarot", "bookmark", "candle", "stationery"]
generos = ["Ficción", "Poesía", "Filosofía", "Historia", "Fantástico"]

productos = []
for i in range(1, 201):  # 200 products
    categoria = random.choice(categorias)
    producto = {
        "id_producto": i,
        "nombre": fake.catch_phrase(),
        "categoria": categoria,
        "precio": round(random.uniform(50, 500), 2),
        "tags": ",".join(random.sample(generos, k=random.randint(1, 2)))
    }
    productos.append(producto)

df_productos = pd.DataFrame(productos)
print(df_productos.head())

books = []
for p in productos:
    if p["categoria"] == "book":
        books.append({
            "id_libro": p["id_producto"],
            "autor": fake.name(),
            "editorial": fake.company(),
            "anio_publicacion": random.randint(1950, 2023),
            "genero": random.choice(generos)
        })

df_books = pd.DataFrame(books)
print(df_books.head())

orders = []
order_items = []
order_id = 1
order_item_id = 1

for _ in range(300):  # 300 orders
    cliente_id = random.randint(1, 100)
    fecha = fake.date_this_year()
    num_items = random.randint(1, 5)

    order_total = 0
    for _ in range(num_items):
        prod = random.choice(productos)
        cantidad = random.randint(1, 3)
        precio = prod["precio"]
        order_total += cantidad * precio

        order_items.append({
            "id_order_item": order_item_id,
            "id_order": order_id,
            "id_producto": prod["id_producto"],
            "cantidad": cantidad,
            "precio_unitario": precio
        })
        order_item_id += 1

    orders.append({
        "id_order": order_id,
        "id_cliente": cliente_id,
        "fecha": fecha,
        "total": round(order_total, 2)
    })
    order_id += 1

df_orders = pd.DataFrame(orders)
df_order_items = pd.DataFrame(order_items)

print(df_orders.head())
print(df_order_items.head())

os.makedirs("../data/raw", exist_ok=True)

df_clientes = pd.DataFrame(clientes)
df_clientes.to_csv("data/raw/clientes.csv", index=False)
df_productos.to_csv("data/raw/productos.csv", index=False)
df_books.to_csv("data/raw/books.csv", index=False)
df_orders.to_csv("data/raw/orders.csv", index=False)
df_order_items.to_csv("data/raw/order_items.csv", index=False)