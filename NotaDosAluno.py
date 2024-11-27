nomes=[]
QuantidadeAlunos=int(input("quantos alunos são?"))
soma_total_notas=0
contador_aluno=0
cont=0
while contador_aluno < QuantidadeAlunos:
    print (f"Aluno {contador_aluno+1}:")

    cont+=1
    soma_total_aluno=0
    notas_dadas=0
    while notas_dadas <4:
        nota=input(f"digite a nota {notas_dadas+1} do aluno {contador_aluno+1}:")


