preço = 20.00

idade = int(input("Digite a idade do cliente: "))
if idade < 0:
    print("Erro!")
else:
    if idade > 120:
        print("Erro!")

estudante = input("O cliente é estudante? (S/N): ")

if idade < 12:
    print(f"Valor do ingresso: R$ {preço/2:.1f} (meia entrada para criança)")
else: 
    if estudante == "S":
        print(f"Valor do ingresso: R$ {preço/2:.1f} (meia entrada para estudante)")
    if idade >=60:
        print(f"Valor do ingresso: R$ {preço/2:.1f} (meia entrada para idosos)") 