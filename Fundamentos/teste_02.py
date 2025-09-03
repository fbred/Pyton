def verificador_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 !=0 or (ano %400 == 0)):
        return True
    else:
        return False
        
ano = int(input())
if verificador_ano_bissexto(ano):
  print("SIM")
else:
  print("NÃO")