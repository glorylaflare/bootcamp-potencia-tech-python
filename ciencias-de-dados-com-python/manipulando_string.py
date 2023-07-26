# Métodos
curso = "      Python "

print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())

titulo = "Python"
print(titulo.center(14, "#"))
print(".".join(titulo))

bagunca = "bAGuNçA"

print(bagunca.upper())
print(bagunca.lower())
print(bagunca.title())

# Interpolação
nome = "Marcelo"
idade = 30
profissao = "Engenheiro"
linguagem = "Java"
saldo = 10.435

print("Nome: %s Idade: %d Profissão: %s Linguagem: %s" % (nome,idade,profissao,linguagem))
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem} Saldo: {saldo:.2f}")

# Fatiamento
nome_completo = "Marcelo Gonçalves de Oliveira Junior"
print(nome_completo[0])
print(nome_completo[-5])
print(nome_completo[:7])
print(nome_completo[8:])
print(nome_completo[8:17])
print(nome_completo[8:17:2])
print(nome_completo[:])
print(nome_completo[::-1])

# String de multiplas linhas
mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo Python.
"""

print(mensagem)
