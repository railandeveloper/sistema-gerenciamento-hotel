from modulo import exibir_menu, Hotel
import time



hotel = Hotel()

while True:
    exibir_menu()
    opcao = input("Escolha uma opção [1/2/3/4/5]: ")

    if opcao == "1":
        print("Cadastrar um quarto selecionado.")
        hotel.adicionar_quarto()
    elif opcao == "2":
        print("Reservar um quarto selecionado.")
        print(f'escolha o indice do quarto que gostaria de reservar')
        hotel.exibir_lista_de_quartos_e_reserva()
        hotel.reservar_quarto()
    elif opcao == "3":
        print("Cancelar uma reserva selecionado.")
        hotel.exibir_lista_de_quartos_e_reserva()
        hotel.cancelar_reserva()
    elif opcao == "4":
        print("Listar quartos e reservas selecionado.")
        hotel.exibir_lista_de_quartos_e_reserva()
    elif opcao == "5":
        print("Saindo do programa...")
        time.sleep(2)
        print('ate logo.')
        break
    else:
        print("Opção inválida, tente novamente.")