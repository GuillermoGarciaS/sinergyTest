import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------- Extract ---------------------- #

clientes = pd.read_csv("data/raw/clientes.csv")
orders = pd.read_csv("data/raw/orders.csv")
productos = pd.read_csv("data/raw/productos.csv")
order_items = pd.read_csv("data/raw/order_items.csv")

# --------------------- Transform --------------------- #

#Limpiamos la tabla de clientes
clientes['email'] = (
    clientes['email']
    .str.strip()
    .str.lower()
    .str.replace("¢", "c", regex = False)
    .str.replace(" ", "", regex = False)
    )

# Limpiamos los productos
productos['price'] = (
    productos['price']
    .astype(str)
    .str.replace("-", "", regex = False)
    .str.strip()
)

# ----------------------- Load ------------------------ #

clientes.to_csv(os.path.join(BASE_DIR, "data/clientes_clean.csv"), index=False)
productos.to_csv(os.path.join(BASE_DIR, "data/productos_clean.csv"), index=False)
orders.to_csv(os.path.join(BASE_DIR, "data/orders_clean.csv"), index=False)
order_items.to_csv(os.path.join(BASE_DIR, "data/order_items_clean.csv"), index=False)