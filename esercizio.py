def calcola_perimetro():
    print("Scegli una figura geometrica:")
    print("A. Quadrato")
    print("B. Cerchio")
    print("C. Rettangolo")
    
    scelta = input("Inserisci la lettera della figura scelta: ")
    
    if scelta == 'A':
        lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
        perimetro = lato * 4
        print(f"Il perimetro del quadrato è: {perimetro}")
    
    elif scelta == 'B':
        raggio = float(input("Inserisci il raggio del cerchio: "))
        perimetro = 2 * 3.14159 * raggio
        print(f"La circonferenza del cerchio è: {perimetro}")
    
    elif scelta == 'C':
        base = float(input("Inserisci la lunghezza della base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        perimetro = 2 * (base + altezza)
        print(f"Il perimetro del rettangolo è: {perimetro}")
    
    else:
        print("Scelta non valida. Riprova.")


calcola_perimetro()
