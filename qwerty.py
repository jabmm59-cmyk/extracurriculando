while True:
    usrin = input("Escolha a questão que quer avaliar (Digite 'help' para vê-lás) >>> ").lower().strip()
    if usrin == "sair":
        break    
    elif usrin == "help":
        print("1 - questão 1")
        print("2 - questão 2")
        print("3 - questão 3")
        print("4 - questão 4")
        print("5 - questão 5")
        print("6 - questão 6")
        print("7 - questão 7")
        print("8 - questão 8")
        print("9 - questão 9")
        print("10 - questão 10")
        print("11 - questão 11")
        print("12 - questão 12")
        print("13 - questão 13")
        print("14 - questão 14")
        print("15 - questão 15")
    elif usrin == "questão 1":
        aq1 = 1
        print("==== Questão 1 ====")
        while aq1 <= 50:
            print(aq1)
            aq1 += 1
    elif usrin == "questão 2":
        print("==== Questão 2 ====")
        aq2 = 1
        while aq2 <= 100:
            if aq2 % 2 == 0:
                print(aq2)
            aq2 += 1
    elif usrin == "questão 3":
        print("==== Questão 3 ====")
        usrinq3 = input("Digite algo para ecoar 11 vezes >>> ")
        aq3 = 1
        while aq3 <= 11:
            print(usrinq3)
            aq3 += 1
    elif usrin == "questão 4":
        print("=== Questão 4 ===")
        while True:
            try:
                numq4 = int(input("Digite um número >>> "))
                break
            except ValueError:
                print("Por favor, digite um número válido.")
        mtq4 = 1
        while mtq4 <= 10:
            print(f"{numq4} x {mtq4} = {numq4 * mtq4}")
            mtq4 += 1
    elif usrin == "questão 5":
        print("=== Questão 5 ===")
        while True:
            try:
                numq5 = int(input("Digite o número >>> "))
                tmpq5 = 1
                while tmpq5 <= 11:
                    print(numq5)
                    tmpq5 += 1
                break
            except ValueError:
                print("Por favor, digite um número válido.")
        if numq5 > 8000:
            print("O valor é maior que 8000.")
        else:
            print("O valor não é maior que 8000.")
    elif usrin == "questão 6":
        print("==== Questão 6 ====")
        aq6 = 1
        while aq6 <= 1000:
            if aq6 % 5 == 0:
                print(aq6)
            aq6 += 1
    elif usrin == "questão 7":
        print("==== Questão 7 ====")
        tmpq7 = 1
        while tmpq7 <= 6:
            try:
                altq7 = float(input("Digite a altura(em metros) >>> "))
            except ValueError:
                print("Por favor, digite uma altura válida.")
                continue
            if tmpq7 == 1:
                menalt = altq7
            else:
                if altq7 < menalt:
                    menalt = altq7
            tmpq7 += 1
        print(f"A menor altura é: {menalt} metros")
    elif usrin == "questão 8":
        print("==== Questão 8 ====")
        tmpq8 = 1
        parcnt = 0
        imparcnt = 0
        while tmpq8 <= 10:
            try:
                numq8 = int(input("Digite um número >>> "))
            except ValueError:
                print("Por favor, digite um número válido.")
                continue
            if numq8 % 2 == 0:
                parcnt += 1
            else:
                imparcnt += 1
            tmpq8 += 1
        print(f"Quantidade de números pares: {parcnt}")
        print(f"Quantidade de números ímpares: {imparcnt}")
    elif usrin == "questão 9":
        print("==== Questão 9 ====")
        while True:
            try:
                m = int(input("Digite um valor para M (1 a 10) >>> "))
                if 1 <= m <= 10:
                    break
                else:
                    print("M deve estar entre 1 e 10.")
            except ValueError:
                print("Por favor, digite um número válido.")

        soma = 0
        i = 1
        while i <= m:
            soma += i
            i += 1

        print(f"A soma dos primeiros {m} números naturais é: {soma}")
    elif usrin == "questão 10":
        print("==== Questão 10 ====") 
        while True:
            try:
                usrinq10 = float(input(">>> "))
            except ValueError:
                print(" válido")
            if usrinq10 == 1:
                maxnum = usrinit
            elif usrinit > maxnum:
                maxnum = usrinit
            elif usrinit == 0:
                print(f"Maior número digitado: {maxnum}")
                break
    elif usrin == "questão 11":
        print("==== Questão 11 ====")
        while True:
            try:
                usrinq11 = float(input(">>> "))
            except ValueError:
                print("Digite um número válido")
            tmpnum = usrinq11
            sumnum = usrinq11 + tmpnum
            if usrinq11 == 0:
                print(f"Dos números que você digitou, o maior deles foi {sumnum}")
                break            
    elif usrin == "questão 12":
        print("==== Questão 12 ====")
        while True:
            try:
                ageq12 = int(input("Digite sua idade >>> "))
            except ValueError:
                print("Digite um número válido")
            tmpageq12 = ageq12
            divageq12 = tmpageq12 / ageq12
            if ageq12 <= 0:
                print(f"A média das idades que você me mostrou é {divageq12}")
    elif usrin == "questão 13":
        print("==== Repetir palavra N vezes ====")
        palavra = input("Digite uma palavra >>> ")
        n = len(palavra)
        i = 1
        while i <= n:
            print(palavra)
            i += 1
    elif usrin == "questão 14":
        print("==== Questão 14 ====")
        trcs = 0
        while True:
            try:
                psa = int(input("Digite o números de pessoas que estarão presentes na conversa (até agora suportado até duas pessoas) >>> "))
            except ValueError:
                print("Digite um número válido")
            psalist = [1, 2]
            if psa not in psalist:
                print("número de pessoas suportadas por conversa: 2, tente de novo")
            if psa == 1:
                msg = input("p1 >>> ")
            else:
                msg = input("p2 >>> ")
            if msg.lower().strip() == "tchau":
                break

            trcs += 1
            psa = 2 if psa == 1 else 1

        print(f"Total de trocas de mensagens: {trcs}")
    elif usrin == "questão 15":
        print("==== Questão 15 ====")
        menq15 = 0
        maxq15 = 0

        while True:
            try:
                ageq15 = int(input("Digite a idade >>> "))
            except ValueError:
                print("Por favor, digite um número válido.")
                continue

            if ageq15 == 0:
                break
            elif ageq15 < 18:
                menq15 += 1
            else:
                maxq15 += 1

        print(f"Quantidade de pessoas menores de 18 anos: {menq15}")
        print(f"Quantidade de pessoas com 18 anos ou mais: {maxq15}")