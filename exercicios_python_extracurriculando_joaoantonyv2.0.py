print("Exercícios Python Extracurriculando (Versão 2.0) - João Antony")

while True:
    usropc = input(
        "Qual atividade deseja verificar? (Digite 'ajuda' para ver as opções) >>> "
    ).lower().strip()

    if usropc == "hello world":
        print("========== Hello, World! ==========")
        print("                                   ")
        print("Hello, World!")
        print("                                   ")
        print("===================================")
    elif usropc == "saudacao":
        print("========= Saudação =========")
        print("                           ")
        nmusrecoec = input("Digite seu nome >>> ")
        print(f"Olá {nmusrecoec}, seja bem-vindo(a)!")
        print("                           ")
        print("============================")
    elif usropc == "eco":
        print("============ Eco ============")
        print("                             ")
        msgeco = input("Digite algo para que essa mensagem possa 'ecoar' ela >>> ")
        print(f"Você disse: {msgeco}")
        print("                             ")
        print("=============================")
    elif usropc == "ajuda":
        print("================== Atvidades Feitas ==================")
        print("                                                      ")
        print("1. Hello, World! (digite 'hello world' para verificar)")
        print("2. Saudação (digite 'saudacao' para verificar)")
        print("3. Eco (digite 'eco' para verificar)")
        print("4. Calculadora (digite 'calculadora' para verificar)")
        print("5. Conversor de Temperatura (digite 'conversor de temperatura' para verificar)")
        print("6. Calculadora de Idade (digite 'calculadora de idade' para verificar)")
        print("7. Área de um Retângulo (digite 'area de um retangulo' para verificar)")
        print("8. Exponenciação (digite 'exponenciacao' para verificar)")
        print("9. Média de Notas (digite 'media de notas' para verificar)")
        print("10. Digite suas informações (digite 'informacao' para verificar)")
        print("11. Imprimir a soma de dois números (digite 'imprimir a soma de dois numeros' para verificar)")
        print("12. Converter Metro para Milímetro (digite 'converter metro para mil")
        print("13. Converter Hora para Minuto (digite 'converter hora para minuto' para verificar)")
        print("14. Converter Dias, Horas, Minutos e Segundos (digite 'converter dias horas minutos e segundos para segundos' para verificar)")
        print("15. Percentual (digite 'percentual' para verificar)")
        print("16. Sair (digte 'sair' para encerrar o programa)")
        print("                                                      ")
        print("======================================================")
    elif usropc == "calculadora":
        print("============= Calculadora =============")
        print("                                       ")
        while True:
            try:
                num1calc = float(input("Digite o primeiro número >>> "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        opcalclist = ["+", "-", "*", "/"]
        while True:
            opcalc = input("Digite a operação (+, -, *, /) >>> ").strip()
            if opcalc in opcalclist:
                break
            print("Operação inválida. Por favor, escolha entre +, -, *, ou /.")
        while True:
            try:
                num2calc = float(input("Digite o segundo número >>> "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        if opcalc == "+":
            print(f"{num1calc} + {num2calc} = {num1calc + num2calc}")
        elif opcalc == "-":
            print(f"{num1calc} - {num2calc} = {num1calc - num2calc}")
        elif opcalc == "*":
            print(f"{num1calc} * {num2calc} = {num1calc * num2calc}")
        elif opcalc == "/":
            print(f"{num1calc} / {num2calc} = {num1calc / num2calc}")
        print("                                       ")
        print("=======================================")
    elif usropc == "conversor de temperatura":
        print("======= Conversor de Temperatura =======")
        print("                                        ")
        try:
            cdtC = float(input("Digite a temperatura em Celsius >>> "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue
        cdtF = (cdtC * 9/5) + 32
        print(f"{cdtC}°C é equivalente a {cdtF}°F")
        print("                                        ")
        print("========================================")
    elif usropc == "calculadora de idade":
        print("=== Calculadora de Idade (para 2026) ===")
        print("                                        ")
        ddnas = int(input("Digite a sua data de nascimento >>> "))
        ag = 2026 - ddnas
        print(f"Em 2026 você terá {ag} anos.")
        print("                                        ")
        print("========================================")
    elif usropc == "area de um retangulo":
        print("========= Área de um Retângulo =========")
        print("                                        ")
        badur = float(input("Digite a base do retângulo >>> "))
        aadur = float(input("Digite a altura do retângulo >>> "))
        print(f"A área do retângulo com base {badur} e altura {aadur} é igual a {badur * aadur} pois {badur} x {aadur} = {badur * aadur}")

        print("========================================")
    elif usropc == "exponenciacao":
        print("============ Exponenciação ============")

        numespcao = float(input("Digite o número que deseja elevar >>> "))
        numelespcao = float(input("Digite o número em que deseja elevá-lo >>> "))
        print(f"{numespcao} elevado a {numelespcao} é igual a {numespcao ** numelespcao}")
        print("                                        ")
        print("=======================================")
    elif usropc == "media de notas":
        print("========= Média de Notas =========")
        print("                                  ")
        num1medno = float(input("Digite a primeira nota >>> "))
        num2medno = float(input("Digite a segunda nota >>> "))
        num3medno = float(input("Digite a terceira nota >>> "))
        medno = (num1medno + num2medno + num3medno) / 3
        print(f"A média das notas é: {medno}")
        print("                                  ")
        print("==================================")
    elif usropc == "informacao":
        print("========= Informações do Usuário =========")
        print("                                         ")
        nmusrinfoeco = input("Digite seu nome >>> ")
        ageusrinfoeco = float(input("Digite sua idade >>> "))
        ctyusrinfoeco = input("Digite sua cidade >>> ")
        print(f"Olá {nmusrinfoeco}, você tem {ageusrinfoeco} anos e mora em {ctyusrinfoeco}.")
        print("                                         ")
        print("=========================================")
    elif usropc == "imprimir a soma de dois numeros":
        print("========= Imprimir a soma de dois números =========")
        print("                                                   ")
        num1somaprdnum = int(input("Digite o primeiro número >>> "))
        num2somaprdnum = int(input("Digite o segundo número >>> "))
        print(f"A soma de {num1somaprdnum} e {num2somaprdnum} é igual a {num1somaprdnum + num2somaprdnum}")
        print("                                                   ")
        print("===================================================")

    elif usropc == "converter metro para milimetro":
        print("========= Converter Metro para Milímetro =========")
        print("                                                   ")
        mtrcmpm = float(input("Digite o valor em metros >>> "))
        mlmcmpm = mtrcmpm * 1000
        print(f"{mtrcmpm} metros é igual a {mlmcmpm} milímetros.")
        print("                                                   ")
        print("===================================================")

    elif usropc == "converter hora para minuto":
        print("========= Converter Hora para Minuto =========")
        print("                                                   ")
        hrchpm = float(input("Digite o valor em horas >>> "))
        minchpm = hrchpm * 60
        print(f"{hrchpm} horas é igual a {minchpm} minutos.")
        print("                                                   ")
        print("===================================================")

    elif usropc == "converter dias horas minutos e segundos para segundos":
        print("========= Converter Dias, Horas, Minutos e Segundos =========")
        print("                                                   ")
        dcdhmesps = int(input("Digite o valor em dias >>> "))
        hcdhmesps = int(input("Digite o valor em horas >>> "))
        mcdhmesps = int(input("Digite o valor em minutos >>> "))
        scdmesps = int(input("Digite o valor em segundos >>> "))
        horas += dcdhmesps * 24
        minutos += horas * 60
        segundos += minutos * 60
        print("                                                   ")
        print(f"{dcdhmesps} dias, {hcdhmesps} horas, {mcdhmesps} minutos e {scdmesps} segundos é igual a {segundos} segundos.")
        print("                                                   ")
        print("===================================================")

    elif usropc == "percentual":
        print("========= Percentual =========")
        print("                                                   ")
        ttprctl = float(input("Digite o valor total >>> "))
        prctlprctl = float(input("Digite o percentual >>> "))
        print(f"{prctlprctl}% de {ttprctl} é {((prctlprctl / 100) * ttprctl)}.")
        print(f"logo, o total a ser pago é {ttprctl - ((prctlprctl / 100) * ttprctl)}")
        print("                                                   ")
        print("===================================================")
    elif usropc == "sair":
        print("Saindo do programa ...")
        break
        
    else:
        print("Comando inválido. Digite 'ajuda' para ver as atividades.")