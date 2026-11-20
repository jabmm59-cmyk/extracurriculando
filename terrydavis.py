import random
def utype(inpcmd):
    while True:
        return input(inpcmd)
def intype(intcmd):
    while True:
        try:
            return int(input(intcmd))
        except ValueError:
            print("Por favor, digite um número inteiro válido")
def floatype(flcmd):
    while True:
        try:
            return float(input(flcmd))
        except ValueError:
            print("Por favor, digite uma float válida")
def shw(*printcmd, sep=" ", end="\n"):
    print(*printcmd, sep=sep, end=end)
def q1():
    shw("==== Questão 1 ====")
    nq1 = intype("Digite um número >>> ")
    tmpnq1 = 1
    while tmpnq1 <= nq1:
        print(tmpnq1)
        tmpnq1 += 2
def q2():
    shw("==== Questão 2 ====")
    nq2 = intype("Digite um número inteiro >>> ")
    tmpnq2 = 2
    while tmpnq2 <= nq2:
        print(tmpnq2)
        tmpnq2 += 2
def q3():
    shw("==== Questão 3 ====")
    n1q3 = intype("Digite o primeiro número >>> ")
    n2q3 = intype("Digite o segundo número >>> ")
    minq3 = min(n1q3, n2q3)
    maxq3 = max(n1q3, n2q3)
    numq3 = minq3
    while numq3 <= maxq3:
        if numq3 % 2 != 0:
            print(numq3)
        numq3 += 1
def q4():
    shw("==== Questão 4 ====")
    while True:
        tamq4 = intype("Digite o tamanho do lado (tamanho suportado: 1 a 20) >>> ")
        if 1 <= tamq4 <= 20:
            break
        shw("O tamanho deve estar entre 1 e 20")
    lnq4 = 1
    while lnq4 <= tamq4:
        colq4 = 1
        while colq4 <= tamq4:
            shw("*", end="")
            colq4 += 1
        shw()
        lnq4 += 1
def q5():
    shw("==== Questão 5 ====")
    n1q5 = intype("Digite o primeiro número >>> ")
    n2q5 = intype("Digite o segundo número >>> ")
    while True:
        n3q5 = intype("Digite o terceiro número (divsor) >>> ")
        if n3q5 != 0:
            break
        shw("O divisor não pode ser zero")
    minq5 = min(n1q5, n2q5)
    maxq5 = max(n1q5, n2q5)
    numq5 = minq5
    while numq5 <= maxq5:
        if numq5 % n3q5 == 0:
            shw(numq5, end = ", ")
        numq5 += 1
    shw()
def q6():
    shw("==== Questão 6 ====")
    cdq6 = ord("a")
    while cdq6 <= ord("z"):
        shw(chr(cdq6), end=" ")
        cdq6 += 1
    shw()
def q7():
    shw("==== Questão 7 ====")
    pq7 = 0
    nq7 = 0
    zq7 = 0
    ctq7 =1
    while ctq7 <= 6:
        numq7 = intype(f"Digite o {ctq7}º número >>> ")
        if numq7 > 0:
            pq7 += 1
        elif numq7 < 0:
            nq7 += 1
        else:
            zq7 += 1
        ctq7 += 1
    shw(f"Positivos: {pq7}")
    shw(f"Negativos: {nq7}")
    shw(f"Zeros: {zq7}")
def q8():
    shw("==== Questão 8 ====")
    bsq8 = intype("Digite a base >>> ")
    while True:
        expq8 = intype("Digite o expoente >>> ")
        if expq8 >= 0:
            break
        shw("O expoente não pode ser negativo")
    shw(f"{bsq8} ^ {expq8} = {bsq8 ** expq8}")

shw("Digite help para listar todas as atividades feitas")
while True:
    usrin = utype("live@user-P:/> ")
    if usrin == "sair":
        break
    elif usrin == "questão 1":
        q1()
    elif usrin == "questão 2":
        q2()
    elif usrin == "questão 3":
        q3()
    elif usrin == "questão 4":
        q4()
    elif usrin == "questão 5":
        q5()
    elif usrin == "questão 6":
        q6()
    elif usrin == "questão 7":
        q7()
    elif usrin == "questão 8":
        q8()
    else:
        print("Atividade ainda não feita ou inexistente")