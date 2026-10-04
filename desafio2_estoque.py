import json
import uuid

def carregar_estoque():
    with open("dados_estoque.json", "r", encoding="utf-8") as file:
        return json.load(file)

def salvar_estoque(dados):
    with open("dados_estoque.json", "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=2, ensure_ascii=False)

def movimentar_estoque(codigo_produto, tipo_movimentacao, quantidade, descricao):
    dados = carregar_estoque()
    produto_encontrado = None

    for item in dados["estoque"]:
        if item["codigoProduto"] == codigo_produto:
            produto_encontrado = item
            break

    if not produto_encontrado:
        print("Produto não encontrado!")
        return

    # Gera um identificador único para a movimentação
    id_movimentacao = str(uuid.uuid4())[:8]

    if tipo_movimentacao.lower() == "entrada":
        produto_encontrado["estoque"] += quantidade
    elif tipo_movimentacao.lower() == "saida":
        if produto_encontrado["estoque"] < quantidade:
            print("Estoque insuficiente!")
            return
        produto_encontrado["estoque"] -= quantidade
    else:
        print("Tipo de movimentação inválido! Use 'entrada' ou 'saida'.")
        return

    salvar_estoque(dados)

    print("--- Movimentação Realizada com Sucesso ---")
    print(f"ID da Movimentação: {id_movimentacao}")
    print(f"Descrição: {descricao}")
    print(f"Produto: {produto_encontrado['descricaoProduto']}")
    print(f"Quantidade final em estoque: {produto_encontrado['estoque']}")

# Exemplo de teste: Entrada de 50 unidades do produto 101 (Caneta Azul)
movimentar_estoque(
    codigo_produto=101,
    tipo_movimentacao="entrada",
    quantidade=50,
    descricao="Entrada de estoque - Nota Fiscal 00123"
)