saldo = 1000
saque = 250
limite = 200
conta_especial = True

True and True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo>= saque)

print(exp)
print(exp2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite) 
conta_especial_com_saldo_suficiente = (conta_especial and saldo>= saque)

exp3 = conta_normal_com_saldo_suficiente or conta_normal_com_saldo_suficiente
print(exp3)