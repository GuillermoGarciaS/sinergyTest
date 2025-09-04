import pandas as pd

# ---------------------- Extract ---------------------- #

clientes = pd.read_csv("clientes.csv")
orders = pd.read_csv("orders.csv")
productos = pd.read_csv("productos.csv")
order_items = pd.read_csv("order_items.csv")

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

clientes.to_csv("clientes_clean.csv", index=False)
productos.to_csv("productos_clean.csv", index=False)