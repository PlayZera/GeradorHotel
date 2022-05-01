hotel = []

class Hotel:

    def gerarHotel(nAndares:int):
        while nAndares !=0:
            andar = ["Andar", int, "Quartos", [False, False, False, False]]
            andar[1] = nAndares
            hotel.append(andar)
            nAndares = nAndares-1
        return hotel

    def reservarQuarto(nAndar:int, nQuarto:int, hotel:list):
        hotel.reverse()
        aluga = True
        andar = hotel[nAndar-1]
        quarto = andar[3]
        quarto[nQuarto] = aluga
        print(hotel)

    def menu():
        print("Bem vindo a rede de hotéis instantâneos")
        print("Digite o número de andares que você deseja para o seu hotel: ")
        nAndares = int(input())
        hotel = Hotel.gerarHotel(nAndares)
        print(hotel, f"\nEsse é o seu hotel ele possui {nAndares} andares.")

        print("Digite o numero do andar que gostaria de reservar: ")
        nAndar = int(input())
        print("Digite o numero do quarto que gostaria de reservar")
        nQuarto = int(input())
        Hotel.reservarQuarto(nAndar, nQuarto, hotel)

Hotel.menu()