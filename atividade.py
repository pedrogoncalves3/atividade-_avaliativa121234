import os 
from dataclasses import dataclass
import time 

os.system("clear")

#criar uma class para os dados dos funcionarios
@dataclass
class Funcionario:
    nome: str 
    cpf: str
    cargo: str
    salario: float
    

#lista de funcionarios para armazenar os dados da classe
nomes = []
    
    
#verificar se a lista está vazia 
def verificar_lista_vazia(nomes):
    if not nomes:
        print(f"\nA lista esta vazia!")
        return True
    return False 


#função para adicionar funcionario
def adicionar(nomes):
    try:
        registro1 = Funcionario(        
            nome = input("digite o NOME do funcionario para cadastro: "),
            cpf = input("digite o CPF do funcionario para cadastro: "),
            cargo = input("digite o seu CARGO na empresa: "),
            salario = input("digite o seu SALARIO: ") 
        )
        nomes.append(registro1)
        print("cadastro concluido!")
        os.system("clear")
        print(f"===Funcionario cadastrado com sucesso!===\n")
    except ValueError:
        print("Erro ao cadastrar funcionario.\nTente novamente!")
        os.system("clear")
        print(f"===Funcionario não cadastrado!===\n")
        
   
# função para mostrar nomes dos funcionarios
def mostrar(nomes):
    try:
        if  verificar_lista_vazia(nomes):
            return

        print(f"\n===lista de nomes===\n")    
        for nome in nomes:
            print(f"nome: {nome.nome}\ncpf: {nome.cpf}\ncargo: {nome.cargo}\nsalario: {nome.salario}\n")  
        
        print(f"====================\n")
    except ValueError:
        print("Erro ao mostrar funcionarios.\nTente novamente!")
        os.system("clear")
        print(f"===Funcionario não encontrado!===\n")        


# função para atualizar nomes        
def atualizar(nomes):
    if verificar_lista_vazia(nomes):
        return
    mostrar(nomes)
    nome_antigo = input(f"\nDigite o nome que deseja atualizar: ")
    try:
        indice = [registro1.nome for registro1 in nomes].index(nome_antigo)
        registro1 = nomes[indice]
        #atualizando os dados
        registro1.nome = input("digite o novo nome: ")
        registro1.cpf = input("digite o novo CPF: ")
        registro1.cargo = input("digite o novo CARGO: ")
        registro1.salario = input("digite o novo SALARIO: ")
        print("atualizado...")
    except ValueError:
        print("erro")   
       

# função para excluir nomes
def excluir(nomes):
    if verificar_lista_vazia(nomes):
        return
    
    mostrar(nomes)
    nome_excluido = input(f"\nDigite o nome que deseja excluir: ")
    try:
       indice = [registro1.nome for registro1 in nomes].index(nome_excluido)
       registro1 = nomes[indice]
       nomes.remove(registro1)
       print ("Apagando...")
    except ValueError:
        print("erro")  


os.system("clear")
print(f"===== Bem vindo ao sistema de cadastro de funcionarios! =====\n")


def cadastro():
    while True:
        print(f"FAÇA SEU CADASTRO\n")
        print("1 - adicionar")
        print("2 - Lista")
        print("3 - Atualizar")
        print(f"4 - Excluir")
        print(f"5 - Sair\n")
        
        opcao = int(input("Digite uma das opções acima: "))
        
        match opcao:
            case 1:
                adicionar(nomes)
            case 2:
                mostrar(nomes)
            case 3:
                atualizar(nomes)
            case 4:
                excluir(nomes)
            case 5: 
                print(f"\nSaindo do programa.")    
                print(f"===Volte sempre!===\n") 
                break
            case _:
                print("opção invalida.\ntente novamente!")
        if opcao != 1:
            time.sleep(3)   
            os.system("clear")
      
cadastro()
    
       
# função para salvar os funcionarios em um arquivo       
def salvar_funcionarios():
    nome_arquivo = "dados_funcionarios.csv"
    with open(nome_arquivo, "a") as arquivo_funcionarios:
        for funcionario in nomes:
            arquivo_funcionarios.write(f"NOME: {funcionario.nome}\nCPF: {funcionario.cpf}\nCARGO: {funcionario.cargo}\nSALARIO: {funcionario.salario}\n\n\n")
    print("Salvando dados dos funcionários...")
    time.sleep(3)
        
salvar_funcionarios()

