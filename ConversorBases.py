print()
print("\033[;1mBem vindo ao CONVERSOR de bases para decimal!")
print("\033[;1mFeito por: @EvertonKauancg")
print("Digite a base que você deseja converter para decimal: \033[m\n")
print("\033[1;44m[1] BINÁRIO\033[m    \033[1;44m[2] OCTAL\033[m    \033[1;44m[3] HEXADECIMAL\033[m\n")

escolha = int(input("\033[;1mDigite aqui: "))

while not 1 <= escolha <= 3:
    print()
    print("\033[;1m\033[31mBase inválida!")
    escolha = int(input("Digite corretamente: \033[m"))

if escolha == 1:
    base = "BINÁRIA"
    print("\nA base escolhida foi \033[1;36m{}\n\033[m".format(base))
    calcBefore = 0

    depois = str(input("\033[;1mDigite aqui o valor inteiro: "))
    resposta = str(input("\nEsse número possui parte decimal? [s/n] "))
    if resposta.lower() == "não" or resposta.lower() == "n" or resposta.lower() == "nao" or resposta.lower() == "negativo":
        quantityBefore = len(depois)

        for c in range(quantityBefore):
            unit = int(depois[c])
            calcBefore += unit * 2 ** (quantityBefore - 1 - c)
        print('O seu número na base 10 é {}'.format(calcBefore))

    else:
        decimal = str(input('\nQual é? '))
        quantityBefore = len(depois)

        for c in range(quantityBefore):
            unit = int(depois[c])
            calcBefore += unit * 2 ** (quantityBefore - 1 - c)

        calcAfter = 0
        quantityAfter = len(decimal)

        for c in range(quantityAfter):
            unit2 = int(decimal[c])
            calcAfter += unit2 * 2 ** -(c + 1)

        print('\nO seu número na base 10 é: {}'.format(calcBefore + calcAfter))

elif escolha == 2:
    base = "OCTAL"
    print("\nA base escolhida foi \033[1;36m{}\n\033[m".format(base))
    depois2 = str(input('Digite aqui o valor inteiro: '))
    resposta2 = str(input("Esse número possui parte decimal? [s/n] "))
    if resposta2.lower() == "não" or resposta2.lower() == "n" or resposta2.lower() == "nao" or resposta2.lower() == "negativo":
        quantityBefore = len(depois2)

        CalcAfter2 = 0
        quantityBefore2 = len(depois2)
        for i in range(quantityBefore2):
            unitario = int(depois2[i])

            CalcAfter2 += unitario * 8 ** (quantityBefore2 - 1 - i)
        print("\033[34m\nA conversão do número para decimal é {}\033[m".format(CalcAfter2))
    else:
        calculated = 0
        decimal2 = str(input("\nQual é? "))
        quantityBefore2 = len(depois2)
        for i in range(quantityBefore2):
            unitario = int(depois2[i])

            calculated += unitario * 8 ** (quantityBefore2 - 1 - i)
        CalcAfter2 = 0

        depois2 = len(decimal2)
        for i in range(depois2):
            quantityBefore2 = int(decimal2[i])

            CalcAfter2 += quantityBefore2 * 8 ** -(i + 1)
        print('\033[34mO seu número na base 10 é: {}\033[m'.format(calculated + CalcAfter2))

elif escolha == 3:
    base = "HEXADECIMAL"
    print()
    print("A base escolhida foi \033[1;36m{}\n\033[m".format(base))
    Dec6 = str(input("\033[;1mDigite o número para ser convertido: "))
    print()
    soma = 0
    if '.' in Dec6:
        Dec6 = Dec6.split('.')
        T = len(Dec6[0])
        for t in range(0, T):
            if "A" == Dec6[0][t] or "a" == Dec6[0][t]:
                soma += 10 * 16 ** (T - 1 - t)
            elif "B" == Dec6[0][t] or "b" == Dec6[0][t]:
                soma += 11 * 16 ** (T - 1 - t)
            elif "C" == Dec6[0][t] or "c" == Dec6[0][t]:
                soma += 12 * 16 ** (T - 1 - t)
            elif "D" == Dec6[0][t] or "d" == Dec6[0][t]:
                soma += 13 * 16 ** (T - 1 - t)
            elif "E" == Dec6[0][t] or "e" == Dec6[0][t]:
                soma += 14 * 16 ** (T - 1 - t)
            elif "F" == Dec6[0][t] or "f" == Dec6[0][t]:
                soma += 15 * 16 ** (T - 1 - t)
            else:
                soma += int(Dec6[0][t]) * 16 ** (T - 1 - t)
        T = len(Dec6[1])
        for t in range(0, T):
            if "A" == Dec6[1][t] or "a" == Dec6[1][t]:
                soma += 10 * 16 ** -(t + 1)
            elif "B" == Dec6[1][t] or "b" == Dec6[1][t]:
                soma += 11 * 16 ** -(t + 1)
            elif "C" == Dec6[1][t] or "c" == Dec6[1][t]:
                soma += 12 * 16 ** -(t + 1)
            elif "D" == Dec6[1][t] or "d" == Dec6[1][t]:
                soma += 13 * 16 ** -(t + 1)
            elif "E" == Dec6[1][t] or "e" == Dec6[1][t]:
                soma += 14 * 16 ** -(t + 1)
            elif "F" == Dec6[1][t] or "f" == Dec6[1][t]:
                soma += 15 * 16 ** -(t + 1)
            else:
                soma += int(Dec6[1][t]) * 16 ** -(t + 1)

        print("\033[34mSeu número na base 10 é: {}\033[m".format(soma))
        #print("\033[34Seu número na base 10 é: {}\033[m"
    else:
        print("\033[34mSeu número na base 10 é: {}\033[m".format((int(Dec6, 16))))
        #print(int(Dec6, 16)) \033[34m  \033[m