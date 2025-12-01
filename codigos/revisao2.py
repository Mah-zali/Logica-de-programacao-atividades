numero = 5

tentativa = int(input("Adivinhe o número (entre 1 e 10): "))

if tentativa < 1:
    print("Palpite inválido")
if tentativa >10:
    print("Palpite inválido")
if tentativa == numero:
    print("Acertou!")

if tentativa < numero:
    if tentativa >= 1:
        if tentativa <= 10:
            print("Muito baixo!")

if tentativa > numero:
    if tentativa >= 1:
        if tentativa <= 10:
            print("Muito alto!")
#proxima tentativa
if tentativa!= numero:
    tentativa2 = int(input("Adivinhe o número (entre 1 e 10): "))

    if tentativa2 < 1:
        print("Palpite inválido")
    if tentativa2 >10:
        print("Palpite inválido")
    if tentativa2 == numero:
        print("Acertou!")

    if tentativa2 < numero:
        if tentativa2 >= 1:
            if tentativa2 <= 10:
                print("Muito baixo!")

    if tentativa2 > numero:
        if tentativa2 >= 1:
            if tentativa2 <= 10:
                print("Muito alto!")

if tentativa!= numero:
    tentativa3 = int(input("Adivinhe o número (entre 1 e 10): "))

if tentativa3 < 1:
    print("Palpite inválido")
if tentativa3 >10:
    print("Palpite inválido")
if tentativa3 == numero:
    print("Acertou!")

if tentativa3 < numero:
    if tentativa3 >= 1:
        if tentativa3 <= 10:
            print("Muito baixo!")

if tentativa3 > numero:
    if tentativa3 >= 1:
        if tentativa3 <= 10:
            print("Muito alto!")

if tentativa3!= numero:
    print(f"Fim de jogo. O certo seria o numero {numero}.")