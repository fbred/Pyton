#formas de declarar um dicionário
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print(pessoa)

pessoa2 = dict(nome="Maria", idade=25, cidade="Rio de Janeiro")
print(pessoa2)

pessoa3 = dict()#dicionário vazio
pessoa3["idade"] = 28
pessoa3["nome"] = "Ana"
print(pessoa3)

#acessar valores
pessoa4 = {"nome": "Carlos", "idade": 40, "cidade": "Belo Horizonte"}
print(pessoa4["nome"]) #Acessando pelo nome da chave
print(pessoa4["idade"]) #Acessando pela idade
print(pessoa4["cidade"]) #Acessando pela cidade

pessoa5 = dict(nome="Luiza", idade=22, cidade="Curitiba")
print(pessoa5.get("nome")) #Acessando pelo nome da chave
print(pessoa5.get("idade")) #Acessando pela idade
print(pessoa5.get("cidade")) #Acessando pela cidade

# Exemplo de uso de dicionário
contatos = {
    "guilherme": {"email": "guilherme@example.com", "telefone": "1234-5678", "endereco": "Rua A, 123","extra": {"campo1": "valor1", "campo2": "valor2"}},#dicionario dentro de dicionário
    "ana": {"email": "ana@example.com", "telefone": "9876-5432", "endereco": "Rua B, 456"},
    "maria": {"email": "maria@example.com", "telefone": "5555-5555", "endereco": "Rua C, 789"},
    "pedro": {"email": "pedro@example.com", "telefone": "1111-1111", "endereco": "Rua D, 101"}
}
#Acessando um dicionário dentro de outro(aninhado)
print(contatos["guilherme"]["telefone"]) # Acessando os dados de Guilherme
print(contatos["ana"]["email"]) # Acessando os dados de Ana
print(contatos["maria"]["endereco"]) # Acessando os dados de Maria
print(contatos["pedro"]["telefone"]) # Acessando os dados de Pedro
print(contatos["guilherme"]["extra"]["campo1"]) # Acessando um campo extra de Guilherme

#acessando os valores do dicionario com for
for contato, dados in contatos.items():
    print(f"Dados de {contato}:")
    for chave, valor in dados.items():
        print(f"  {chave}: {valor}")
    print()
