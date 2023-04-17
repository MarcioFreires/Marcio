from fastapi import FastAPI
app = FastAPI()
vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa", "preco_unitario": 3, "quantidade": 3},
}
@app.get("/")
def home():
    return {"vendas": len(vendas)}
@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    return vendas[id_venda]