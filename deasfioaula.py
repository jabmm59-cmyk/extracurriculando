print("Desafio de aula")
while True:
    usrinp = input("Escolha qual questão você quer ver >>> ").lower().strip()
    if usrinp == "questão 1":
        while True:
            print("Qual a sua situação atual?")
            print("1 Solteiro(a)")
            print("2 Casado(a)")
            print("3 Viúvo(a)")
            print("4 Enrolado(a)")
            print("5 Não desejo declarar")

            usropcq1 = input(">>> ").strip()
            if usropcq1 not in {"1", "2", "3", "4", "5"}:
                print("Opção inválida")
                continue

            usropcq1 = int(usropcq1)
            if usropcq1 == 1:
                print("Você está solteiro(a)")
            elif usropcq1 == 2:
                print("Você está casado(a)")
            elif usropcq1 == 3:
                print("Você está viúvo(a)")
            elif usropcq1 == 4:
                print("Você está enrolado(a)")
            elif usropcq1 == 5:
                print("Você preferiu não responder")
            break
    elif usrinp == "questão 2":
        print("Positivo ou Negativo, Par ou Ímpar")
        while True:
            usropcq2 = float(input(">>> ").strip())
            if usropcq2  >= 0:
                print("Positivo")
            elif usropcq2 < 0:
                print("Negativo")
            if usropcq2 % 2 == 0:
                print("Par")
            else:
                print("Ímpar")
            break
    elif usrinp == "questão 3":
        print("Vogal ou Consoante")
        while True:
            usropcq3 = input(">>> ").lower().strip()
            if usropcq3 in {"a", "e", "i", "o", "u"}:
                print("Vogal")
            else:
                print("Consoante")
            break
    elif usrinp == "questão 4":
        print("Qual o maior número?")
        while True:
            usropcq4 = float(input("Digite o primeiro número >>> ").strip())
            usropcq4_2 = float(input("Digite o segundo número >>> ").strip())
            if usropcq4 > usropcq4_2:
                print(f"O maior número é {usropcq4}")
            elif usropcq4 < usropcq4_2:
                print(f"O maior número é {usropcq4_2}")
            else:
                print("Os números são iguais")
            break
    elif usrinp == "questão 5":
        print("É um ano bissexto?")
        while True:
            usropcq5 = float(input("Digite o ano >>> ").strip())
            if usropcq5 % 4 == 0 and (usropcq5 % 100 != 0 or usropcq5 % 400 == 0):
                print(f"{usropcq5} é um ano bissexto")
            else:
                print(f"{usropcq5} não é um ano bissexto")
            break
    elif usrinp == "questão 6":
        print("Você é maior de idade?")
        while True:
            usropcq6 = float(input("Digite sua idade >>> ").strip())
            try:
                usropcq6 = int(usropcq6)
            except ValueError:
                print("Idade inválida")
                continue
            if usropcq6 >= 18:
                print("Você é maior de idade")
            elif usropcq6 < 18 and usropcq6 >= 13:
                print("Você é um adolescente")
            elif usropcq6 < 13:
                print("Você é uma criança")
            elif usropcq6 >= 60:
                print("Você é um idoso")
            break
    elif usrinp == "questão 7":
        print("Software de valor e parcelas")
        while True:
            usropcq7 = float(input("Digite o valor do software >>> ").strip())
            usropcq7_2 = int(input("Digite a quantidade de parcelas >>> ").strip())
            if usropcq7_2 <= 0:
                print("Quantidade de parcelas inválida")
                continue
            valpar = usropcq7 / usropcq7_2
            if valpar >= 100:
                print(f"Sua parcela é igual ou acima de R$ 100,00, logo não terá juros, mas a parcela será de {valpar}")
            else:
                print(f"O valor de cada parcela é {valpar}, mas como é abaixo de R$ 100,00, terá juros de 5% sobre o valor total, logo o valor final será de {usropcq7 * 1.05} e a parcela será de {(usropcq7 * 1.05) / usropcq7_2}")
            break
    elif "adalberto" in usrinp:
        print("........               ........")
        print("........               ........")
        print("........               ........")
        print("...............................")
        print("...............................")
        print("....      ...........      ....")
        print("....      ...........      ....")
        print("....      ...........      ....")
        print("....      ...........      ....")
        print("....      ...........      ....")
        print("...............................")
        print("...............................")
        print("     .......    .......")
        print("     .......    .......")
        print("     _______    _______")
        print("    /       |  |       \ ")
        print("   /        |  |        \ ")
        print("  |_________|  |_________|")
        print("")
        print("Você vasculhou tanto o código que encontrou o Easter Egg Adalberto, parabéns!")
    elif usrinp == "sair":
        break
    else:
        print("Questão inválida ou não disponível")
