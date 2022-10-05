par = 0
impar = 0
for multi in range(10):
    valor = int(input(f'{multi+1}° valor: '))
    if valor % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"São {impar} números ímpares")
print(f"São {par} números pares")