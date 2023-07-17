logic = True
print()

# Pergunta o número de dias que tem o mês

while logic:

    dias = int(input("Informe o número de dias do mês: "))

    if dias >= 28 and dias <= 31:

        logic = False
    
    else: 

        print("VALOR INVALIDO! ")

logic = True

# Pergunta o dia da semana que começa o mês

while logic:

    inicio = int(input("Informe o dia da semana: "))

    if inicio >= 1 and inicio <= 7:

        logic = False

    else:

        print("VALOR INVALIDO! ")

logic = True

# Gera o calendário apartir das respostas dadas pelo terminal

if logic:

    print()
    print("DOM SEG TER QUA QUI SEX SAB")

    cont_dia_semana = 1

    sai = False

    for i in range(inicio - 1):

        cont_dia_semana += 1

        print("  ", end="  ")

    for i in range(dias):

        if cont_dia_semana == 8:

            cont_dia_semana = 1

            print()

            print(f"{i+1:02}", end="  ")

        else:

            print(f"{i+1:02}", end="  ")
            
        cont_dia_semana += 1

    for cont_dia_semana in range(7):

        print("  ", end="  ")

    print()
