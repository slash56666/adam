print("Vítejte v kalkulátoru plateb")
platba = int(input("Kolik máte zaplatit? "))
sporitne = int(input("Kolik chcete zaplatit na spropitné (v Kč)? "))
rozdvoj = int(input("Mezi kolika lidmi se má rozdělit? "))
potga = ((platba) + (sporitne)) / rozdvoj
print(f"Každý člověk by měl zaplatit: {potga:.2f} Kč")


