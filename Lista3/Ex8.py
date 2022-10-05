num = int(input('Digite um valor positivo: '))
for multi in range(1, num + 1):
    if num % multi == 0:
        print(multi)