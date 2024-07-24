# Lista global para armazenar carros cadastrados
carros = []

# Função principal para gerenciar o programa
def gerente():
    while True:
        print("\nBem-vindo ao programa de Carro")
        print("Escolha uma das opções abaixo:")
        print("1 - Cadastrar novo Carro")
        print("2 - Comprar um Carro")
        print("3 - Vender o Carro")
        print("4 - Sair")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            cadastrando_um_novo_veiculo()
        elif opcao == "2":
            comprar()
        elif opcao == "3":
            vender()
        elif opcao == "4":
            print("Obrigado por utilizar o programa")
            break
        else:
            print("Opção inválida, Tente Novamente")

# Cadastrar um novo veiculo
def cadastrando_um_novo_veiculo():
    print("\nCadastrar novo veiculo") 
    modelo = input("Digite o modelo que você quer: ")
    ano = input("Digite o Ano: ")
    preco = float(input("Digite o Preço: "))
    carro = {"modelo": modelo, "ano": ano, "preco": preco}
    carros.append(carro)
    print(f"O Carro {modelo} do Ano {ano} está custando R$ {preco}")

# Comprar um carro
def comprar():
    print("\nComprar um Carro")
    modelo_car = input("Digite Qual modelo vc quer: ")
    ano_car = input("Digite o Ano que vc procura: ")
  
    # Verifica se o carro existe na lista de carros cadastrados
    carro_encontrado = None
    for carro in carros:
        if carro["modelo"] == modelo_car and carro["ano"] == ano_car:
            carro_encontrado = carro
            break
    
    if carro_encontrado:
        print(f"Carro encontrado: Modelo: {carro_encontrado['modelo']}, Ano: {carro_encontrado['ano']}, Preço: {carro_encontrado['preco']}")
        # Aqui você pode adicionar lógica para comprar o carro, como remover da lista
    else:
        print("Carro não encontrado.")

# Vender um carro
def vender():
    print("\nVender um Carro")
    modelo_c = input("Digite o veículo que você quer vender: ")
    ano_c = input("Digite o ano: ")
    
    # Verifica se o carro existe na lista de carros cadastrados
    carro_encontrado = None
    for carro in carros:
        if carro["modelo"] == modelo_c and carro["ano"] == ano_c:
            carro_encontrado = carro
            break
    
    if carro_encontrado:
        carros.remove(carro_encontrado)
        print(f"Carro {carro_encontrado['modelo']} do ano {carro_encontrado['ano']} vendido com sucesso!")
    else:
        print("Carro não encontrado.")

# Chama a função gerente para iniciar o programa
gerente()
