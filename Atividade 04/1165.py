n = int(input())

while n > 0:
    x = int(input())
    i = 2
    primo = True

    while i * i <= x:
        if x % i == 0:
            primo = False
            break
        i += 1

    if primo:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")

    n -= 1
