def q1():
    print("==== Questão 1 ====")
    while True:
        try:
            nq1 = int(input("Digite um número >>> "))
        except ValueError:
            print("Número inválido")
            continue
        tmpnq1 = 1
        while tmpnq1 <= nq1:
            print(tmpnq1)
            tmpnq1 += 2
        break
def q2():
    print("==== Questão 2 ====")
    while True:
        try:
            nq2 = int(input("Digite um número inteiro >>> "))
        except ValueError:
            print("Número inválido")
            continue
        tmpnq2 = 2
        while tmpnq2 <= nq2:
            print(tmpnq2)
            tmpnq2 += 2
        break
def q3():
    print("==== Questão 3 ====")
    while True:
        try:
            naq3 = int(input("Digite o primeiro número >>> "))
            nbq3 = int(input("Digite o segundo número >>> "))
        except ValueError:
            print("Número inválido")
            continue
        break #pausa temporária
        
print("Digite 'help' para listar todas as atividades feitas")
while True:
    usrin = input("live@user-P:/> ")
    if usrin == "sair":
        break
    elif usrin == "questão 1":
        q1()
    elif usrin == "questão 2":
        q2()
    else:
        print("Atividade ainda não feita ou inexistente")