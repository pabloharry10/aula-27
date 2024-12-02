#ler entradas do usuario
nome =input("Digite o nome do aluno:")#ARMAZENAR o nome do aluno
#4 notas dos alunos
nota1=float(input("Digite a nota do 1°bimestre: "))
nota2=float(input("Digite a nota do 2°bimestre: "))
nota3=float(input("Digite a nota do 3°bimestre: "))
nota4=float(input("Digite a nota do 4°bimestre: "))

faltas=int(input("Digite as faltas do aluno: "))
#calculo da media
media=(nota1+nota2+nota3+nota4)/4
print (f"A media do aluno foi: {media}")

if media >=8:
    print("o aluno foi aprovado")