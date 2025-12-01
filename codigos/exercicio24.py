filo = input()
classe = input()
tipo = input()

if filo == 'vertebrado':
    if classe == 'ave':
        if tipo == 'carnivoro':
            print('águia')
        elif tipo == 'onivoro':
            print('pomba')
    elif classe == 'mamifero':
        if tipo == 'onivoro':
            print('homem')
        elif tipo == 'herbivoro':
            print('vaca')    
#repetiçao do bloco
if filo == 'invertebrado':
    if classe == 'inseto':
        if tipo == 'hematofago':
            print('pulga')
        elif tipo == 'herbivaro':
            print('lagarta')
    elif classe == 'anelideo':
        if tipo == 'hematofago':
            print('sanguessuga')
        elif tipo == 'onivero':
            print('minhoca') 