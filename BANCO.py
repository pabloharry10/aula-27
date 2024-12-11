#cadastro do usuario e senha
#menu principal
#ler a escolha do usuario 
def validar_senha():
    senha_validar=input("Digite sua senha: ")
    if senha_validar==senha:
        return True
saldo=0.0
while True:
    escolha_menu= int(input("Escolha uma das opçoes:\n 1.cadastrar \n 2.login \n 3.encerar\n escolha uma dessas opçoes: "))#le a escolha do usuario

    if escolha_menu==1:
        #crie uma senha e um usuario
        usuario=input("\nCrie um nome de usuario: ")
        senha=input("Crie uma senha: ")

    elif escolha_menu==2:
        login_usuario=input("Digite seu usuario: ")
        login_senha=input("Digite sua senha: ")

        if login_usuario==usuario and login_usuario==senha:
            print("login realizado com sucesso!")
            #se login correto entra no menu principal
            print (f"Bem vindo, {usuario}")

            while True:
                print("1.Deposito\n2.Sacar\n3.Pagamento\n4.Extrato\n5.Encerrar")
                escolha_principal=int(input("Escolha uma dessas opçoes: "))

                if escolha_principal==1:
                    valor_deposito=float (input("Valor do deposito:"))
                    saldo = saldo + valor_deposito
                    print(f"Novo saldo é: {saldo}")

                elif escolha_principal ==2:
                    valor_saque=float (input("Digite o valor do saque: "))

                    if validar_senha():
                        saldo=saldo-valor_saque
                        print(f"você sacou: {saldo}")

                    else:
                        print("Senha incorreta")

                elif escolha_principal ==3:
                    valor_pix= float (input("Digite o valor do pix: "))

                    if validar_senha():
                        saldo=saldo-valor_pix

                    else:
                        print("A sua senha está incorreta")
                
                elif escolha_principal==4:
                    if validar_senha():
                        print (f"extrato:{saldo}")
                    
                    else:
                        print("Senha incorreta")
                elif escolha_principal==5:
                    senha_encerrar=input("Digite sua senha: ")
                    if senha_encerrar==senha:
                        break
                    else:
                        print("senha incorreta")
        else:
            print ("Usuario ou senha incorretos")