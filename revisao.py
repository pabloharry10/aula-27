#ler entradas do usuario
alunos =[]
escolha_usuario=int (input("Quantos alunos você deseja cadastrar? "))
cont=0
while cont < escolha_usuario:
    nome =input("Digite o nome do aluno: ")#ARMAZENAR o nome do aluno
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
print(alunos)