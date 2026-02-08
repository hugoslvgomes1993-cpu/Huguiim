def calculadora():
    print("=== CALCULADORA EM PYTHON ===")
    print("Operações disponíveis:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
   

    try:
        opcao = int(input("Escolha a operação (1 a 4): "))
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            resultado = num1 + num2
            operacao = "+"
        elif opcao == 2:
            resultado = num1 - num2
            operacao = "-"
        elif opcao == 3:
            resultado = num1 * num2
            operacao = "*"
        elif opcao == 4:
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
                return
            resultado = num1 / num2
            operacao = "/"
        else:
            print("Opção inválida.")
            return

        print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")

    except ValueError:
        print("Erro: digite apenas números válidos.")

# Executa a calculadora
calculadora()
