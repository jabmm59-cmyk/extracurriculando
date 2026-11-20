def intype(intcmd):
     while True:
        try:
            return int(input(intcmd))
        except ValueError:
            print("Por favor, digite um número inteiro válido")
def utype(incmd):
    while True
def q3():
    print("==== Questão 3 ====")
    n1q3 = intype("Digite o primeiro número >>> ")
    n2q3 = intype("Digite o segundo número >>> ")
    minq3 = min(n1q3, n2q3)
    maxq3 = max(n1q3, n2q3)
    numq3 = minq3
    while numq3 <= maxq3:
        if numq3 % 2 != 0:
            print(numq3)
        numq3 += 1
q3()