nome = input("qual palavra?")

for i in range(0, len(nome)+1):
    print(nome[:i])

for i in range(0, len(nome)):
    print(nome[i])
