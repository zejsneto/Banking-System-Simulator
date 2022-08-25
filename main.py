import os

#Import date and time
from datetime import datetime
dataHoraAtuais = datetime.now()
dataHoraTexto = dataHoraAtuais.strftime('%d/%m/%Y %H:%M')

def createNewClient():
    nome = input("Enter your name: ")
    cpf = input("Enter your Social Security Number: ")
    conta = input("Enter type of account (s: Salary, c: Common ou p: Plus): ")
    senha = input("Enter your password: ")
    valorInicial = input("Enter initial value: ")
    if os.path.isfile(cpf+".txt"):
        print("Client already registered.")    
    else:
        arquivo = open(cpf+".txt", "a")
        arquivo.write("Name: %s\n" % nome)
        arquivo.write("Social Security Number: %s\n" % cpf)
        if conta == "s":
            arquivo.write("Account: Salary\n")
        elif conta == "c":
            arquivo.write("Account: Common\n")
        elif conta == "p":
            arquivo.write("Account: Plus\n")
        arquivo.write("Password: %s\n" % senha)
        arquivo.write("Initial Value: %s\n" % valorInicial)
        arquivo.close()
        print("Client created.")

def eraseClient():
    cpfVerificar = input("Enter Social Security Number: ")
    if  os.path.exists(cpfVerificar+".txt"):
        senhaVerificar = input("Enter password: ")
        arquivo = open(cpfVerificar+".txt", "r")
        senha = []
        for i in arquivo.readlines():
            senha.append(i.strip().split())
        arquivo.close()
        if senhaVerificar == senha[3][1]:
            os.remove(cpfVerificar+".txt")
            print("Account erased.")
        if senhaVerificar != senha[3][1]:
            print("Wrong password.")
            return
    
    else: 
        print("The Social Security Number is wrong or do not exist.")
        return

def debit():
    cpfVerificar = input("Enter Social Security Number: ")
    if  os.path.exists(cpfVerificar+".txt"):
        senhaVerificar = input("Enter password: ")
        arquivo = open(cpfVerificar+".txt", "r")
        senha = []
        for i in arquivo.readlines():
            senha.append(i.strip().split())
        arquivo.close()
        if senhaVerificar == senha[3][1]:
            if senha[2][1] == "Salary":
                valorDebitado = float(input("Enter the amount to be debited: "))
                arquivo = open(cpfVerificar+".txt", "a")
                tarifa = (0.05*valorDebitado)
                novoSaldo = float(senha[-1][-1]) - valorDebitado - tarifa
                if novoSaldo >= 0:
                    arquivo.write("Date: %s - %.2f Tax: %.2f Balance: %.2f\n" %(dataHoraTexto, valorDebitado, tarifa, novoSaldo))
                    arquivo.close()
                    print("An amount of %.2f was debited with a tax of  %.2f" %(valorDebitado, tarifa))
                else:
                    print("Insufficient balance to complete the transaction.")

            elif senha[2][1] == "Common":
                valorDebitado = float(input("Enter the amount to be debited: "))
                arquivo = open(cpfVerificar+".txt", "a")
                tarifa = (0.03*valorDebitado)
                novoSaldo = float(senha[-1][-1]) - valorDebitado - tarifa
                if novoSaldo >= -500:
                    arquivo.write("Date: %s - %.2f Tax: %.2f Balance: %.2f\n" %(dataHoraTexto, valorDebitado, tarifa, novoSaldo))
                    arquivo.close()
                    print("An amount of %.2f was debited with a tax of %.2f" %(valorDebitado, tarifa))
              
                else:
                    print("Insufficient balance to complete the transaction.")

            elif senha[2][1] == "Plus":
                valorDebitado = float(input("Enter the amount to be debited: "))
                arquivo = open(cpfVerificar+".txt", "a")
                tarifa = (0.01*valorDebitado)
                novoSaldo = float(senha[-1][-1]) - valorDebitado - tarifa
                if novoSaldo >= -5000:
                    arquivo.write("Date: %s - %.2f Tax: %.2f Balance: %.2f\n" %(dataHoraTexto, valorDebitado, tarifa, novoSaldo))
                    arquivo.close()
                    print("An amount of %.2f was debited with a tax of %.2f" %(valorDebitado, tarifa))

                else:
                    print("Insufficient balance to complete the transaction.")

        if senhaVerificar != senha[3][1]:
            print("Wrong password.")
            return
            
    else: 
        print("The Social Security Number is wrong or do not exist.")
        return

def deposit():
    cpfVerificar = input("Enter Social Security Number: ")
    if  os.path.exists(cpfVerificar+".txt"):
        arquivo = open(cpfVerificar+".txt", "r")
        senha = []
        for i in arquivo.readlines():
            senha.append(i.strip().split())
        arquivo.close()
        valorDepositado = float(input("Enter the amount you want to deposit: "))
        arquivo = open(cpfVerificar+".txt", "a")
        novoSaldo = float(senha[-1][-1]) + valorDepositado
        arquivo.write("Date: %s + %.2f Tax: 0.00 Balance: %.2f\n" %(dataHoraTexto, valorDepositado, novoSaldo))
        arquivo.close()
        print("An amount of %.2f was deposited." %valorDepositado)
            
    else: 
        print("The Social Security Number is wrong or do not exist.")
        return

def balance():
    cpfVerificar = input("Enter Social Security Number: ")
    if  os.path.exists(cpfVerificar+".txt"):
        senhaVerificar = input("Enter password: ")
        arquivo = open(cpfVerificar+".txt", "r")
        senha = []
        for i in arquivo.readlines():
            senha.append(i.strip().split())
        arquivo.close()

        if senhaVerificar == senha[3][1]:
            print("Your balance is %s." %senha[-1][-1])
            
        if senhaVerificar != senha[3][1]:
            print("Wrong password.")
            return
            
    else: 
        print("The Social Security Number is wrong or do not exist.")
        return

def extract():
    cpfVerificar = input("Enter Social Security Number: ")
    if  os.path.exists(cpfVerificar+".txt"):
        senhaVerificar = input("Enter password: ")
        arquivo = open(cpfVerificar+".txt", "r")
        senha = []
        for i in arquivo.readlines():
            senha.append(i.strip().split())
        arquivo.close()

        if senhaVerificar == senha[3][1]:
            senha.pop(3)
            senha.pop(3)
            for i in range(len(senha)):
                   print(*senha[i])
            
        else:
            print("Wrong password.")
            return
            
    else: 
        print("The Social Security Number is wrong or do not exist.")
        return

#Creates Menu
def main():
    while True:
        print()
        print("-----Menu-----")
        print()
        print("1. Create New Client")
        print("2. Delete Existing Client")
        print("3. Debit")
        print("4. Deposit")
        print("5. Balance")
        print("6. Extract")
        print()
        print("0. Sair")
        print()
        print("--------------")

        opcao = input("Choose one of the options: ")

        if opcao == "1":
            createNewClient()
        
        if opcao == "2":
            eraseClient()

        if opcao == "3":
            debit()  

        if opcao == "4":
            deposit()  

        if opcao == "5":
            balance()  

        if opcao == "6":
            extract()  

        if opcao == "0":
            break  

main()