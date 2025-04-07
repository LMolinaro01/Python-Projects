import math

class Calculadora:
    def __init__(self):
        self.resultado = None

    def adicao(self, x, y):
        self.resultado = x + y
        return self.resultado

    def subtracao(self, x, y):
        self.resultado = x - y
        return self.resultado

    def multiplicacao(self, x, y):
        self.resultado = x * y
        return self.resultado

    def divisao(self, x, y):
        if y == 0:
            print("\nErro! Divisão por zero não é permitida.")
            self.resultado = None
        else:
            self.resultado = x / y
        return self.resultado

    def potencia(self, x, y):
        self.resultado = x ** y
        return self.resultado

    def raiz_quadrada(self, x):
        if x < 0:
            print("\nErro! Não é possível calcular a raiz quadrada de um número negativo.")
            self.resultado = None
        else:
            self.resultado = math.sqrt(x)
        return self.resultado

# Função principal
def main():
    calc = Calculadora()

    print("""\n---------------- Calculadora ----------------""")

    while True:
        print("\nSelecione a operação:")
        print("\n1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potência")
        print("6. Raiz Quadrada")
        print("7. Sair")

        opcao = input("\nDigite a opção (1-7): ")

        if opcao in ['1', '2', '3', '4']:
            num1 = float(input("\nDigite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == '1':
                print("\nResultado:", calc.adicao(num1, num2))
            elif opcao == '2':
                print("\nResultado:", calc.subtracao(num1, num2))
            elif opcao == '3':
                print("\nResultado:", calc.multiplicacao(num1, num2))
            elif opcao == '4':
                print("\nResultado:", calc.divisao(num1, num2))

        elif opcao == '5':
            num1 = float(input("\nDigite a base: "))
            num2 = float(input("Digite o expoente: "))
            print("Resultado:", calc.potencia(num1, num2))

        elif opcao == '6':
            num = float(input("\nDigite o número: "))
            print("Resultado:", calc.raiz_quadrada(num))

        elif opcao == '7':
            print("\nEncerrando o programa...")
            break

        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    main()
