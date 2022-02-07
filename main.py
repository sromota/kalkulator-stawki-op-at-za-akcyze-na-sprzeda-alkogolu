#wariant dla alkoholu do 4,5% oraz piwa


#wczytywanie danych od użytkowanika
year_of_business = int(input("Podaj rok prowadzenia działalności: "))
lump_sum = int(input("Podaj obecną stawkę ryczałtu: "))
limit_lump = int(input("Podaj limit do którego rozlicza się wg. ryczałtu: "))
percent_payment = float(input("Podaj procent opłaty nieryczałtowanej (w ułamku dziesiętnym, z przedzieleniem kropką): "))
year_before_score = int(input("Podaj sprzedaż w zeszłym roku: "))


#sprawdzanie sumarycznej płatności 
if year_of_business == 0:
        summarize_payment = 0

elif year_of_business == 1:
        summarize_payment = lump_sum

elif year_before_score > limit_lump:
        summarize_payment = int(round(percent_payment*year_before_score, 0))
else:
        summarize_payment = lump_sum

print("Całkowita płatność: ", summarize_payment)
print("")

 



#zdefiniowanie danych do obliczenia rat
number_of_instalments = 12
instalments = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
delta = int
popular = int(round(summarize_payment/number_of_instalments, 0))

#obliczanie rat (najpierw dla liczby podzielnej przez liczbę rat, potem dla zaokrąglenia w dół, potem dla zaokrąglenia w góre )
if popular*number_of_instalments == summarize_payment:
    print("Równe raty, każda = ", popular)

elif popular*number_of_instalments < summarize_payment:
        delta = (summarize_payment-number_of_instalments*popular)
        for i in range(1, number_of_instalments+1):
            instalments [i-1] = popular
        for y in range(1, delta+1):
            instalments [y-1] = instalments [y-1]+1
        for z in range(1, number_of_instalments+1):
            print("Rata ", z, "= ", instalments[z-1])
            print("")
else: 
        delta = (number_of_instalments*popular - summarize_payment)
        for i in range(1, number_of_instalments+1):
            instalments [i-1] = popular
        for y in range(1, delta+1):
            instalments [y-1] = instalments [y-1]-1
        for z in range(1, number_of_instalments+1):
            print("Rata ", z, "= ", instalments[z-1])
            print("")
