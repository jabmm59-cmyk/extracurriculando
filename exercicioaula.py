while True:
    usr = input(">>> ").lower().strip()
    if usr == "sair":
        break
    elif usr == "ajuda":
        print("Digite 'sair' para encerrar o programa.")
        print("Digite 'questão 1' para verificar se você pode entrar na festa.")
        print("Digite 'questão 2' para verificar se você pode entrar na festa teen.")
        print("Digite 'questão 3' para verificar se você pode entrar no camarim.")
        print("Digite 'questão 4' para verificar se você pode jogar.")
        print("Digite 'questão 5' para verificar o preço do celular.")
        print("Digite 'questão 6' para conversar com o mini simulador de conversa.")
        print("Digite 'questão 7' para verificar se você é um Gamer de verdade.")   
        print("Digite 'ajuda' para ver esta mensagem novamente.")
    elif usr == "questão 1":
        while True:
            print("==== Você pode entrar na festa? ====")
            try:
                agq1 = float(input("Digite a sua idade >>> "))
                agvr = int(agq1)
            except ValueError:
                print("Por favor, digite um número válido para a idade.")
                continue
            if agq1 >= 14:
                print("Você pode entrar na festa!")
                break
            else:
                print("Você não pode entrar na festa!")
                break
    elif usr == "questão 2":
        while True:
            print("==== Verificação de idade para festa teen? ====")
            try:
                agq2 = float(input("Digite a sua idade >>> "))
                agvr = int(agq2)
                if agq2 >= 14 and agq2 <= 17:
                    print("Você pode entrar na festa!")
                    break
                else:
                    print("Você não pode entrar na festa!")
                    break
            except ValueError:
                print("Por favor, digite um número válido para a idade.")
                continue
    elif usr == "questão 3":
        camq3 = ["Carlos", "Bianca", "Ana", "Adalberto"]
        while True:
            print("==== Verificação de camarim ====")
            nm= input("Digite o seu nome >>> ")
            if nm in camq3:
                print("Você pode entrar para o camarote!")
                break
            else:
                print("Você tem ingresso normal")
                break
    elif usr == "questão 4":
        print("==== Verificação de Idade de Jogo ====")
        while True:
            try:
                agq4 = float(input("Digite a sua idade >>> "))
                agvr = int(agq4)
            except ValueError:
                print("Por favor, digite um número válido para a idade.")
                continue
            if agvr >= 15:
                print("Você pode jogar!")
                break
            else:
                acomp = input("Você está acompanhado de um adulto? (s/n) >>> ")
                if acomp == "s":
                    print("Você pode jogar!")
                    break
                else:
                    print("Você não pode jogar!")
                    break
    elif usr == "questão 5":
        print("==== Comprando um Celular ====")
        while True:
            prc = 1000
            print(f"O preço do celular é R${prc}.")
            est = input("Você é estudante? (s/n) >>> ")
            if est == "s":
                prc -= 250
                print(f"Você tem direito a um desconto de R$250, o preço final é R${prc}.")
                break
            ver = input("Você irá pagar à vista ou parcelado? (digite 'vista' ou 'parcelado') >>> ")
            if ver == "vista":
                print(f"Você pagará R${prc} à vista.")
                break
            elif ver == "parcelado":
                while True:
                    pr = input("Digite o número de parcelas (2, 3 ou 4) >>> ")
                    try:
                        pr_int = int(pr)
                        if pr_int in [2, 3, 4]:
                            print(f"Você pagará R${prc/pr_int:.2f} por parcela.")
                            break
                        else:
                            print("Por favor, digite 2, 3 ou 4 parcelas.")
                    except ValueError:
                        print("Por favor, digite um número válido.")
                break
    elif usr == "questão 6":
        while True:
            print("==== Mini Simulador de Conversa ====") #Tá parecendo até aquela agente ELISA que vinha no DOS 6.0
            usrq6 = input("Digite uma mensagem >>> ").lower().strip()
            if usrq6 in ["oi", "olá", "Oi", "Olá"]:
                print("Olá! Como você está?")
            elif usrq6 in ["tudo bem?", "tudo bem"]:
                print("Estou bem, obrigado por perguntar!")
            elif usrq6 in ["tchau", "adeus"]:
                print("Tchau! Até a próxima!")
                break
            else:
                print("Desculpe, não entendi a sua mensagem. Pode repetir?")
    elif usr == "questão 7":
        print("===== Você é Gamer de verdade? =====")
        while True:
            print("Responda com 'sim' ou 'não'.")
            pont = 0
            while True:
                q1 = input("Você joga mais de 3 horas por dia? >>> ").lower().strip()
                if q1 == "sim":
                    pont += 1
                    break
                elif q1 == "não":
                    break
                else:
                    print("Por favor, responda apenas com 'sim' ou 'não'.")
            while True:
                q2 = input("Você participa de campeonatos de jogos? >>> ").lower().strip()
                if q2 == "sim":
                    pont += 1
                    break
                elif q2 == "não":
                    break
                else:
                    print("Por favor, responda apenas com 'sim' ou 'não'.")
            while True:
                q3 = input("Você tem um setup gamer completo? >>> ").lower().strip()
                if q3 == "sim":
                    pont += 1
                    break
                elif q3 == "não":
                    break
                else:
                    print("Por favor, responda apenas com 'sim' ou 'não'.")
            while True:
                q4 = input("Você conhece todos os lançamentos de jogos? >>> ").lower().strip()
                if q4 == "sim":
                    pont += 1
                    break
                elif q4 == "não":
                    break
                else:
                    print("Por favor, responda apenas com 'sim' ou 'não'.")
            while True:
                q5 = input("Você já gastou mais de R$500 em jogos? >>> ").lower().strip()
                if q5 == "sim":
                    pont += 1
                    break
                elif q5 == "não":
                    break
                else:
                    print("Por favor, responda apenas com 'sim' ou 'não'.")
            print(f"Você marcou {pont} pontos.")
            if pont >= 4:
                print("Você é um Gamer de verdade!")
            elif pont == 3:
                print("Você é quase um Gamer de verdade!")
            else:
                print("Você não é um Gamer de verdade!")
            break

