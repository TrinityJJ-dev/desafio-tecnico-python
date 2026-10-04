from datetime import datetime, date

def calcular_juros_vencimento(valor, data_vencimento_str):
    # Converte a string de data para o formato de data
    data_vencimento = datetime.strptime(data_vencimento_str, "%Y-%m-%d").date()
    hoje = date.today()

    # Calcula a diferença de dias entre hoje e o vencimento
    dias_atraso = (hoje - data_vencimento).days

    if dias_atraso <= 0:
        print("O título não está em atraso.")
        return valor, 0.0

    taxa_diaria = 0.025  # 2.5% ao dia
    valor_juros = valor * taxa_diaria * dias_atraso
    valor_total = valor + valor_juros

    print("--- Cálculo de Juros por Atraso ---")
    print(f"Data de Vencimento: {data_vencimento_str}")
    print(f"Data Atual: {hoje.strftime('%Y-%m-%d')}")
    print(f"Dias em Atraso: {dias_atraso} dia(s)")
    print(f"Valor Original: R$ {valor:.2f}")
    print(f"Valor dos Juros (2.5%/dia): R$ {valor_juros:.2f}")
    print(f"Valor Total a Pagar: R$ {valor_total:.2f}")

    return valor_total, valor_juros

# Exemplo de teste:
# Digite um valor e uma data passada no formato "AAAA-MM-DD"
calcular_juros_vencimento(valor=1000.00, data_vencimento_str="2026-09-20")