from datetime import datetime, timedelta, date

tipocarro = 'G' # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipocarro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual} e o ficará pronto às {data_estimada}')
elif tipocarro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou: {data_atual} e o ficará pronto às {data_estimada}')
else:
   data_estimada = data_atual + timedelta(minutes=tempo_grande)
   print(f'O carro chegou: {data_atual} e o ficará pronto às {data_estimada}')

print(date.today()- timedelta(days=1)) #usando o timedelta reduz um dia na data

#manipulando hora usando date time e timedelta
resultado = datetime(2026, 6, 23, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

#Pegando apenas a parte da data
print(datetime.now().date())