print("Vítejte na horské dráze")
hroch = int(input("Jaká je vaše výška v cm?\n"))
bill = 0
if hroch >= 87:
    print("Můžete jet na horské dráze.")
    age = int(input("Jaká je váš věk?\n"))
    if age < 18:
        print("Cena vašeho lístku je 100 Kč.")
        bill = 50
    else:
        print("Cena vašeho lístku je 150 Kč")
        fotka = input ("chce se během jízdy vyfotit ano nebo ne\n")
        if fotka == "ano": 
            bill=+50
            print (f"tak dobře cena vašeho lístku je {bill}")
else:
    print("Omlouváme se, ale na horské dráze jet nemůžete.")