class Quarto:
    def __init__(self, numero_do_quarto, capacidade_de_hospedes, disponibilidade,valor_diaria, nome_locador=""):   
        self.numero_do_quarto = numero_do_quarto
        self.capacidade_de_hospedes = capacidade_de_hospedes
        self.disponibilidade = disponibilidade
        self.valor_diaria = valor_diaria
        self.nome_locador = nome_locador
             
                
    def __str__(self):
        informacoes = f"Número do Quarto: {self.numero_do_quarto} | Capacidade: {self.capacidade_de_hospedes} Pessoas | Disponibilidade: {self.disponibilidade} | Diaria: R${self.valor_diaria}"
        if self.disponibilidade == 'reservado':
            informacoes += f" | Locador: {self.nome_locador.title()}"
        return informacoes
  
        
    
class Hotel():
    def __init__(self):
        self.lista_de_quartos = []
        
     
    def adicionar_quarto(self):
        while True:
            try:
                numero_quarto = int(input('Digite o numero do quarto: '))
                if numero_quarto > 0:
                    numero_ja_existe = False
                    for quarto in self.lista_de_quartos:
                        if numero_quarto == quarto.numero_do_quarto:
                            numero_ja_existe = True
                            break
                            
                    if numero_ja_existe:
                        print(f'Ja existe um quarto com esse numero')
                        continue      
                    else:
                        break
                else:
                    print('O numero do quarto nao pode ser negativo')                              
            except ValueError:
                print('Digite um numero inteiro')        
                          
        while True:
            try:                    
                capacidade_de_hospedes = int(input(f'Quantas pessoas cabem no quarto?: '))
                if capacidade_de_hospedes > 0:
                    break
                else:
                    print('Digite um numero positivo')
                    continue
            except ValueError:
                print('A quantidade deve ser um numero inteiro')
                
                
        disponibilidade = 'disponivel'
        
        while True:
            try:
                valor_diaria = float(input(f'Digite o valor da diaria desse quarto: '))
                if valor_diaria > 0:
                    break
            except ValueError:
                print('Digite o valor em numeros reais')     
        novo_quarto = Quarto(numero_quarto, capacidade_de_hospedes, disponibilidade, valor_diaria)
        self.lista_de_quartos.append(novo_quarto)
            
    
    def reservar_quarto(self):
        
        if self.lista_de_quartos:
            quartos_disponiveis = [quarto for quarto in self.lista_de_quartos if quarto.disponibilidade == 'disponivel']
            
            if not quartos_disponiveis:
                print('Todos os quartos estão reservados no momento.')
                return
            
            valor_total = 0
            while True:
                try:
                    qtd_dias_locacao = int(input('Digite a quantidade de dias que deseja ficar alocado: '))
                    if qtd_dias_locacao > 0:  
                        break 
                    else:
                        print(f'digite um numero positivo') 
                except ValueError:
                    print(f'Digite um numero inteiro')
            
            nome_locador = str(input(f'Nome de quem esta alugando: ')).strip().lower()
            while True:
                try:
                    indice_a_ser_reservado = int(input(f'Digite o indice da sua escolha: '))
                    quarto_alugado = False
                    if indice_a_ser_reservado >=0 and indice_a_ser_reservado <= len(self.lista_de_quartos) -1 :
                        for indice, quarto in enumerate(self.lista_de_quartos):
                            if indice_a_ser_reservado  == indice and quarto.disponibilidade == 'disponivel':
                                quarto.disponibilidade = f'reservado'
                                quarto.nome_locador = nome_locador
                                valor_total = qtd_dias_locacao * quarto.valor_diaria
                                print(f'Quarto reservado com sucesso para {nome_locador.title()}!')
                                print(f'Valor total a ser pago: R${valor_total}')
                                quarto_alugado = True
                                break
                        else:
                            print('Esse quarto ja esta alugado')
                        if quarto_alugado:
                            break        
                    else:
                        print('Esse indice nao existe na lista')       
                except ValueError:
                    print('Digite um numero inteiro valido')           
        else:
            print(f'Nenhum quarto disponivel para reserva')            
    
    
    def cancelar_reserva(self):
        if self.lista_de_quartos:
            quartos_reservados = [quarto for quarto in self.lista_de_quartos if quarto.disponibilidade == 'reservado']
            
            if not quartos_reservados:
                print('Todos os quartos estão disponiveis no momento. nao e possivel cancelar')
                return
                
            while True:
                print(f'Digite o seu nome para cancelarmos sua reserva')
                nome_para_cancelar= str(input('Nome: ')).strip().lower()
                cancelado = False
                for indice, quarto in enumerate(self.lista_de_quartos):
                    if quarto.nome_locador == nome_para_cancelar and quarto.disponibilidade == 'reservado':
                        quarto.disponibilidade = 'disponivel'
                        cancelado = True
                        print(f'Reserva de {nome_para_cancelar} cancelada com  sucesso')
                
                if cancelado:
                    break        
                    
                if not cancelado:
                    print('Nenhuma reserva encontrada para o nome informado ou o quarto não está reservado.')
        else:
            print('Nao ha quartos reservados')
                    
    
    def exibir_lista_de_quartos_e_reserva(self):
        if self.lista_de_quartos:
            for indice, quarto in enumerate(self.lista_de_quartos):
                print(f'indice {indice}| {quarto}')
        else:
            print('A lista de quartos esta vazia')        

  
def exibir_menu():
        print("\n===== MENU =====")
        print("1. Cadastrar um quarto")
        print("2. Reservar um quarto")
        print("3. Cancelar uma reserva")
        print("4. Listar quartos e reservas")
        print("5. Sair")    
    
            