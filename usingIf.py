
# utilizando o if para comparar o valor do preço de algo
precoBanana = int(input("digite um preço para a banana:"))
print("o preco da banana é de: ", precoBanana)

if precoBanana < 10:
    print("a banana está barata.")
elif precoBanana > 10:
    print("a banana está cara.")
elif precoBanana == 10:
    print("a banana está no preco ideal")

