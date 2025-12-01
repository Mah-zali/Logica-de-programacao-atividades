coelhos = ratos = sapos = total = 0

for i in range(int(input())):
    quantidade, animal = input().split(' ')
    total += int(quantidade)

    if animal== 'C':
        coelhos += int(quantidade)
    elif animal == 'R':
        ratos += int(quantidade)
    elif animal == 'S':
        sapos += int(quantidade)

print(f"Total: {total} cobaias")        
print(f"Total de coelhos: {total}")        
print(f"Total de ratos: {total}")        
print(f"Total de sapos: {total}")
print(f"Percentual de coelhos: {((100.0/total)*coelhos):.2f} %")        
print(f"Percentual de ratos: {((100.0/total)*ratos):.2f} %")        
print(f"Percentual de sapos: {((100.0/total)*sapos):.2f} %")        