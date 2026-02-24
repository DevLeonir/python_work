reservation = input("Quantos lugares em uma mesa você precisa? ")
reservation = int(reservation)

if reservation >= 8:
    print("\nÉ necessario aguardar por uma mesa.")
else:
    print("A mesa já está disponível.")