import json

def calcular_comissao(valor):
    if valor < 100.00:
        return 0.0
    elif valor < 500.00:
        return valor * 0.01
    else:
        return valor * 0.05

with open("dados_vendas.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

comissoes = {}

for venda in dados["vendas"]:
    vendedor = venda["vendedor"]
    valor = venda["valor"]
    comissao = calcular_comissao(valor)
    
    if vendedor not in comissoes:
        comissoes[vendedor] = 0.0
    comissoes[vendedor] += comissao

print("--- Total de Comissão por Vendedor ---")
for vendedor, total in comissoes.items():
    print(f"{vendedor}: R$ {total:.2f}")