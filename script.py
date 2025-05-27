win = False
palavra = input("insira a palavra secreta: ")

for i in range(1000):
    print()

desc = []
for i in range(len(palavra)):
    desc.append("?")

tem_list = []

ex_list = []

print("a palavra tem",len(palavra),"letras")
while not win:
    print("C = certo")
    print("L = lugar errado")
    print("E = não há na palavra")
    print()
    resp = input("Tente adivinhar: ")
    av = []
    if resp == palavra:
        print("Você acertou!")
        win = True
    elif len(resp) != len(palavra):
        print("Sua resposta não tem",len(palavra),"letras")
    else:
        i_pos = 0
        for i in resp:
            ex = True
            tem = True
            i_pos += 1
            j_pos = 0
            E = True
            av.append("A")
            for j in palavra:
                j_pos += 1
                if j == i:
                    if i_pos == j_pos:
                        av[i_pos - 1] = "C"
                        desc[i_pos - 1] = i
                        E = False
                    elif av[i_pos - 1] != "C":
                        av[i_pos - 1] = "L"
                        for t in tem_list:
                            if i == t:
                                tem = False
                        if tem:
                            tem_list.append(i)
                        E = False
            if E:
                av[i_pos - 1] = "E"
                for x in ex_list:
                    if i == x:
                        ex = False
                if ex:
                    ex_list.append(i)

    if not win:
        print(av)
        print("letras excluidas:",ex_list)
        print("letras da palavra:",tem_list)
        print("palavra:",desc)

