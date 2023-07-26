texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço")
    
# range(stop) -> range object
# range(start, stop, [step]) -> range object

lista = list(range(5))
print(lista)

# Tabuada
for numero in range(0, 61, 6):
    print(numero, end=" ")
