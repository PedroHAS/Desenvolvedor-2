def calcular_percentuais(faturamentos):
    total = sum(faturamentos.values())
    percentuais = {
        estado: (valor / total) * 100 for estado, valor in faturamentos.items()
    }
    return percentuais

def main():
    faturamentos = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    percentuais = calcular_percentuais(faturamentos)
    total = sum(faturamentos.values())

    print(f"Faturamento total: R$ {total:.2f}\n")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()