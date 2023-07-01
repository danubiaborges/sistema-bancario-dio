nome = "Danubia"
idade = 20
profissao = "Estudante"
linguagem = "Python"
dados = {"nome": "Danubia", "idade": 20}
saldo = 45.435

print("Nome: %s Idade: %d" % (nome, idade))     # não se usa

# .format()
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

# f"
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")