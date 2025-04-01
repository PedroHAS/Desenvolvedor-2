def is_fibonacci(n: int) -> bool:
    if n == 0:
        return True
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def main():
    numero = int(input("Informe um número: "))
    if is_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()