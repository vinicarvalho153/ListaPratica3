cont = 0
for multi in range(10):
    num = int(input(f"{multi +1}° número: "))
    if 10 <= num <= 20:
        cont += 1
print(f"O numero  {cont} esta dentro do intervalo [10,20]")