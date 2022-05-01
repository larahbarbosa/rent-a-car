#Criando a classe pai locadora que herdará os objetos Carro e Cliente

class locadora(object):
  def __init__(self):
    self.ListarClientes = []
    self.ListarCarros = []
    self.AlugarCarro = []
    self.menu()

#Criando o menu que chamará o código pela visão do usuário

  def menu(self):

        while True:
            print('Bem-vinda(o) à locadora de veículos Rent a Car')
            print('1) Cadastrar novo veículo')
            print('2) Cadastrar novo cliente')
            print('3) Alugar um veículo')
            print('4) Relatório de locação')
            print('0) Finalizar!')

            while True:
                try:
                    opc = int(input("\nDigite: "))
                    break
                except ValueError:
                    print("\nInsira um número válido!\n")

            if opc == 1:
                Carro.cadastrar_carro(self)

            elif opc == 2:
                Cliente.cadastrar_cliente(self)

            elif opc == 3:
                locadora.alugar_carro(self)

            elif opc == 4:
                Carro.relatorio(self)

            elif opc == 0:
                print("\nFinalizando programa...")
                break

            else:
                print("\nOpção inválida!\n")

#Criando o atributo 'alugar' para chamar os métodos de cadastrar e alugar um veículo

  def alugar(self):
    self.nome = str(input('Digite seu nome completo: '))
    Carro.cadastrar_carro(self)
    Carro.alugar_carro(self)
    locadora.alugar_carro(self)  

#Criando a classe Carro que herdará da classe locadora.
#Definindo o método construtor para receber os parâmetros.

class Carro(locadora):
    def __init__(self, categoria, transmissao, combustivel, marca, modelo, ano, placa, alugar):
        self.categoria = categoria
        self.transmissao = transmissao
        self.combustivel = combustivel
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.alugar = alugar
        

    def cadastrar_carro(self):

        Carro.categoria(self)

        Carro.transmissao(self)

        Carro.combustivel(self)

        self.marca = str(input('Digite a marca: ')).upper()
        self.modelo = str(input('Digite o modelo: ')).upper()
        self.ano = int(input('Digite o ano: '))
        self.placa = str(input('\n\nPlaca: ')).upper()
        self.alugar = 'DISPONÍVEL' 
        
        carro = {
            'categoria': self.categoria,
            'transmissao': self.transmissao,
            'combustivel': self.combustivel,
            'marca': self.marca,
            'modelo': self.modelo,
            'ano': self.ano,
            'placa': self.placa,
            'alugar': self.alugar        }
        self.ListarCarros.append(carro)
        print(self.ListarCarros)    

    def categoria(self):
        while True:
            print('\n[1] Sedan\n [2] Picape\n [3] SUV')
            while True:
                try:
                    category = int(input('\nDigite a categoria: '))
                    break
                except ValueError:
                    print('\nInsira um número válido!\n')

            if category == 1:
                self.categoria = 'SEDAN'
                break
            elif category == 2:
                self.categoria = 'PICAPE'
                break
            elif category == 3:
                self.categoria = 'SUV'
                break
            else:
                print('\nOpção inválida')

    def transmissao(self):
        while True:
            print('\n [1] Automático\n [2] Manual')
            while True:
                try:
                    transmiss = int(input('\nDigite o tipo: '))
                    break
                except ValueError:
                    print('\nInsira um número válido!\n')

            if transmiss == 1:
                self.transmissao = 'AUTOMATICO'
                break
            elif transmiss == 2:
                self.transmissao = 'MANUAL'
                break
            else:
                print('\nOpção inválida')

    def combustivel(self):
        while True:
            print('\n [1] Gasolina\n [2] Álcool\n [3] Flex\n [4] Diesel\n [5] GNV')
            while True:
                try:
                    combust = int(input('\nDigite o tipo: '))
                    break
                except ValueError:
                    print('Insira um número válido!\n')

            if combust == 1:
                self.combustivel = 'GASOLINA'
                break
            elif combust == 2:
                self.combustivel = 'ALCOOL'
                break
            elif combust == 3:
                self.combustivel = 'FLEX'
                break
            elif combust == 4:
                self.combustivel = 'DIESEL'
                break
            elif combust == 5:
                self.combustivel = 'GNV'
                break
            else:
                print('\nOpção inválida')
                                                      

#Criando a classe Cliente que herdará da classe locadora.
#Definindo o método construtor para receber os parâmetros.

class Cliente(locadora):
    def __init__(self, nome, cpf, rg):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg

    def cadastrar_cliente(self):
        while True:
            self.nome = str(input('Digite o nome do usuário a ser cadastrado: '))
            break
        self.cpf = str(input('CPF: ')).upper()
        self.rg = str(input('RG: '))
        usuario = {
            'nome': self.nome,
            'cpf': self.cpf,
            'rg': self.rg
        }

        self.ListarClientes.append(usuario)
        print(self.ListarClientes)

class Finalizar():
  breakpoint   

locadora()                                     

#Falta criar a função para alugar o carro, sinalizada como alugar_carro