'''MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input("informe sua idade: "))

#IF utilizado normalmente
if idade >= MAIOR_IDADE:
    print("Pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")


if idade >= MAIOR_IDADE:
    print("Pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")

#Utilizando o elif
if idade >= MAIOR_IDADE:
    print("Pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode tirar sobre condições especiais")
else:
    print("Ainda não pode tirar a CNH")'''

#if aninhado (if dentro de if)
conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Naque realizado com uso do chque especial")
    else:
        print("Não foi possível realizar o saque!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")
else:
    print("Tipo de conta não identificado!")
