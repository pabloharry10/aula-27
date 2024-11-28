def calcular_media(notas):                                                      #A palavra-chave def em Python é usada para definir funções.
    soma= notas[0]+notas[1]+notas[2]+notas[3]                                   #essa linha de codigo serve para calcular as notas dos alunos
    return soma /4                                                              #depois de calcular toda a nota ele vai dividir por 4
def situacao_aluno (media,faltas):                                              #aqui esta definindo algumas funçoes
    if media >= 8.0 and faltas<= 20:                                            #então ele vai verificar se a nota e maior ou igual a 8 e faltas menor ou igual a 20
        return "aprovado"                                                       #se essas duas condiçoes for verdadeiras ele será aprovado
    elif media < 5.0 or faltas >25:                                             #aqui tembem ele vai verificar se media for menor que 5 ou faltas for maior que 25
        return "reprovado"                                                      #o aluno e reprovado
    else:                                                                       #aqui ele verifica se o aluno esta de recuperação
        return"recuperação"                                                     #o aluno esta de recuperação 
def gerar_relatorio(alunos, num_alunos):                                        #definindo a função aluno e numeros de alunos
    print("relatorio da sitiação dos alunos:")                                  #vai mostrar na tela
    print ("-"*50)                                                              #tembem vai mostrar na tela

    i=0                                                                         #esse "i" ele funciona como se fosse um contador 
    while i < num_alunos:                                                       #enquanto "i"for menor que num de alunos ele ira repetir
        aluno=alunos[i]                                                         #isso acessa algumas possiçoes como ana, gabriel ou joão
        print(f"aluno:{aluno[0]}")                                              #mostra o nome do aluno
        print(f"media:{aluno[1]:.2f}")                                          #mostra a media desse aluno
        print(f"faltas{aluno[2]}")                                              #mostra a quantidade de faltas desse aluno 
        print(f"situação:{aluno[3]}")                                           #mostra a situação desse aluno se ele foi reprovado, aprovado ou de recuperação 
        print("-"*50)                                                           #mostra na tela
        i+=1                                                                    #isso serve para parar o while "um contador"
def main():                                                                     #isso serve para definir uma função
    quantidade_alunos=int(input("quantos alunos você deseja cadrastrar:"))      #pergunta quantidade de alunos o usuario deseja cadastrar
    alunos=[]                                                                   #arrar que guarda alunos
    contador=0                                                                  #isso e um contador como qualquer um 
    while contador < quantidade_alunos:                                         #enquanto contador for menor que quantidade de alunos ele para
        nome = input(f"Nome do aluno {contador + 1}: ")                         # Nome do aluno
        notas = [                                                               #isso guarda as notas dos alunos para poder calcular
            float(input("Digite a primeira nota: ")),                           #isso guarda a primeira nota do aluno e mostra na tela
            float(input("Digite a segunda nota: ")),                            #isso guarda a segunda nota do aluno e mostra na tela 
            float(input("Digite a terceira nota: ")),                           #isso guarda a terceira nota do aluno e mostra na tela 
            float(input("Digite a quarta nota: "))                              #isso tambem guarda a segunda nota do aluno e mostra na tela 
        ]
        faltas = int(input("Número de faltas: "))                               #aqui o usuario digita as notas dos aluno que ele solicitou 
        media=calcular_media(notas)                                             #media=calcular medias 
        situacao=situacao_aluno(media,faltas)                                   #ve a situação do aluno 
        alunos.append([nome,media,faltas,situacao])                             #acessa a essas posiçoes mostradas 
        contador+=1                                                             #novamente um contador qualquer 
    gerar_relatorio(alunos,quantidade_alunos)                                   #relatorio dos alunos 
main()                                                                          #A função main() em programação é frequentemente usada para ser o ponto de entrada principal de um programa.