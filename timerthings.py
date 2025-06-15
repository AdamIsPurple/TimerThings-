import time

def timer(nome_attività, durata):
    print(f"Inizio timer per '{nome_attività}'... ({durata} secondi)")
    while durata > 0:
        mins, secs = divmod(durata, 60)
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        print(f"\r{timer_format}", end="")
        time.sleep(1)
        durata -= 1
    print("\nTempo scaduto! Puoi fare una pausa o proseguire con un'altra attività.")

def main():
    print("Benvenuto nel timer personalizzato!")

    nome_attività = input("Inserisci il nome dell'attività che vuoi fare (es. Studio, Sport, etc.): ")
    
    try:
        durata = int(input("Inserisci la durata del timer in secondi: "))
        if durata <= 0:
            print("La durata deve essere un numero positivo!")
        else:
            timer(nome_attività, durata)
    except ValueError:
        print("Per favore inserisci un numero valido per la durata.")

if __name__ == "__main__":
    main()
