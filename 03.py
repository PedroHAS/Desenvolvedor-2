import json


FILE_PATH = "/data/dados.json"

def carregar_dados(path):
    with open(path, 'r') as f:
        return json.load(f)

def analisar_faturamento(dados):
    # Filtrar dias com faturamento > 0
    faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

    menor = min(faturamentos)
    maior = max(faturamentos)
    media = sum(faturamentos) / len(faturamentos)
    dias_acima_media = sum(1 for valor in faturamentos if valor > media)

    return menor, maior, media, dias_acima_media

def main():
    dados = carregar_dados(FILE_PATH)
    menor, maior, media, dias_acima_media = analisar_faturamento(dados)

    print(f"Menor faturamento: R$ {menor:.2f}")
    print(f"Maior faturamento: R$ {maior:.2f}")
    print(f"Média mensal (dias com faturamento): R$ {media:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")

if __name__ == "__main__":
    main()