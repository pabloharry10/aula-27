def horario(hora_do_dia):
    if (hora_do_dia>=0)and(hora_do_dia <=12):
        print("Bom dia!")
    elif (hora_do_dia>=13)and(hora_do_dia<=18):
        print("Boa tarde!")
    elif (hora_do_dia>=19)and(hora_do_dia<=23):
        print("Boa noite!")
    else:
        print("esse horario não existe")

resposta = float(input("digite que horas são: "))
horario(resposta)