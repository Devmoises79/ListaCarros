class Carro:
    def __init__(self, Marca, Modelo, Ano, Preco):
        self.Marca = Marca
        self.Modelo = Modelo
        self.Ano = Ano
        self.Preco = Preco

# Criando os carros
carro1 = Carro("Chevrolet", "Camaro SS", 2015, 'R$ 250.000,00')
carro2 = Carro("Ford", "Mustang 4.0", 2010, 'R$ 300.000,00')
carro3 = Carro("Volkswagen", "Jetta 1.4", 2019, 'R$ 130.000,00')

# Lista dos carros
carros = [carro1, carro2, carro3]

# Exibindo opções
print("Escolha um carro:")
print("1 - Chevrolet Camaro SS")
print("2 - Ford Mustang 4.0")
print("3 - Volkswagen Jetta 1.4")

# Pegando a escolha do usuário
opcao = input("Digite o número do carro desejado: ")

# Verificando a escolha e imprimindo as informações corretas
if opcao in ['1', '2', '3']:
    carro_escolhido = carros[int(opcao) - 1]  
    print("\nVocê escolheu:") 
    print(f"Marca: {carro_escolhido.Marca}")
    print(f"Modelo: {carro_escolhido.Modelo}")
    print(f"Ano: {carro_escolhido.Ano}")
    print(f"Preço: {carro_escolhido.Preco}")
else:
    print("\nOpção inválida! Escolha um número entre 1 e 3.")

