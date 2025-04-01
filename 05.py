def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

def main():
    texto = input("Informe uma string para inverter: ")
    resultado = inverter_string(texto)
    print(f"String invertida: {resultado}")

if __name__ == "__main__":
    main()