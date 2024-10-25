n1 = str(input("Digite uma palavra que vc ache que é um palindromo: "))

n1 = n1.lower()
n1 = n1.replace(" ", "")

n1_reverso = n1[::-1]

print("String formatada: {}".format(n1))

if n1 == n1_reverso:
    print("É um palíndromo!!")
else:
    print("Não é um palíndromo!")
