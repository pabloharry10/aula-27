#ler entradas do usuario
import time
nome=nota1=nota2=nota3=nota4=faltas=situacao=media=0
alunos =[]
nota1 = 0
while True:
    escolha_menu=int(input("\nEscolha uma opção: \n1.Cadastrar\n2.relatorio\n3.encerrar\nEscolha uma dessas opçoes: "))
    if escolha_menu ==1: 
        escolha_usuario=int (input("Quantos alunos você deseja cadastrar? "))
        cont=0
        while cont < escolha_usuario:
            nome =input("\nDigite o nome do aluno: ")#ARMAZENAR o nome do aluno

            #4 notas dos alunos
            nota1=float(input("Digite a nota do 1°bimestre: "))
            nota2=float(input("Digite a nota do 2°bimestre: "))
            nota3=float(input("Digite a nota do 3°bimestre: "))
            nota4=float(input("Digite a nota do 4°bimestre: "))

            faltas=int(input("Digite as faltas do aluno: "))

            #calculo da media
            media=(nota1+nota2+nota3+nota4)/4
            print (f"A media do aluno foi: {media}")

            #logica da situação
            if faltas > 31:
                situacao ="Reprovado por faltas"
            elif media >= 8:
                situacao="aprovado"
            elif media >=5:#recuperação
                print("quanto o aluno tirou na recuperação?")
                #ler a nota de recuperacao
                recuperacao=float(input())
                if recuperacao >=(10-media):
                    situacao="aprovado na recuperação"
                    print(situacao)
                else:
                    situacao="reprovado na recuperação"
                    print(situacao)
            else:
                situacao="reprovado por media"

            #enviar dados do aluno para a lista de alunos
            alunos.append([nome,media,faltas,situacao])
            
            #relatorio
            cont+=1
    elif escolha_menu == 2:
        print("processando...")
        time.sleep(3)
        for i in alunos:
            print("-"*50)
            print(f"\nNome: {i[0]}")
            print("Faltas: ", i[2])
            print("Media: ", i[1])
            print(f"Situação: {i[3]}\n")
        print("-"*50)
    elif escolha_menu == 3:
        print("Você encerrou o cadastro!")
        break