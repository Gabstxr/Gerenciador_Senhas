senha = 0
fila = []

while True:
    print("========== Gerador de Senhas ==========")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print(" ")
    print("Digite 1 para pegar uma senha")
    print("Digite 2 para verificar qual senha foi chamada")
    print("Digite 3 para sair")
    print(" ")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    menu = input("Digite um valor:  ")

    if(int(menu) == 1):
        senha += 1
        print(f"Senha gerada: {senha}")
        print(" ")
        fila.append(senha)
    elif(int(menu) == 2):
        if(len(fila) == 0):
          print("Nao possui senhas")
          print(" ")
        else: 
            senhaSaida = fila.pop(0)
            print(f"Senha chamada:  {senhaSaida}")
            print(" ")
    elif(int(menu) == 3):
        break
   
print("Senhas restantes: ")
print(fila)