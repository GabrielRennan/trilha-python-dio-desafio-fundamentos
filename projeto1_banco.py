menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
 

==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES= 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("Depósito".center(18,'='))
        deposito = float(input("Informe o valor a ser depositado:"))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

        else:
            print("Operação Falhou! O valor informado é inválido")

    elif opcao == 2:
        print("Saque".center(15,'='))

        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")

        else:

            saque = float(input("Informe o Valor do saque:"))

            if saque > saldo:
                print("Operação falhou ! Seu saldo é inferior ao saque solicitado!")

            elif saque > limite:
                print("Operação falhou ! Saque desejado é maior que o limite permitido")    
            
            elif saque >0:
                saldo -=saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_saques+=1

            else :
                print("Operação falhou! O valor informado é inválido.")


    elif opcao == 3:
        print("EXTRATO".center(17,'='))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("".center(17,'='))

    elif opcao== 0 :

        break

    else:
         print("Operação Invalida, por favor selecione novamente a operação desejada")