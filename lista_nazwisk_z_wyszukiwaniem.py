#Wczytanie długości listy
warun = False
while warun == False:
    a = int(input("Podaj liczbe osób do wczytania: "))
    if a<=0:
        print("Liczba musi być większa od zera")
    else:
        warun = True


#Wczytywanie imion i nazwisk
tablica = [[0] * 2 for i in range(a)]
i=0
while i < a:
    tablica[i]=input("Podaj imię oraz nazwisko przedzielone spacją: ").split()
    i += 1
    if len(tablica[i-1]) == 1:
        print("Nie przedzielono spacją! Powtórz czynność")
        i -= 1
        
    
#Wczytanie danych do wyszukiwania
keyword = (input("Podaj szukane nazwisko, by otrzymać imiona osób o tym nazwisku: "))
imiona_danego_nazwiska = []
liczba_danego_nazwiska = 0

#Wyszukiwanie
for i in range(a):
            if keyword in tablica[i][1]:
                imiona_danego_nazwiska.append(tablica[i][0])
                liczba_danego_nazwiska +=1

#Wyniki wyszukiwania
print()
print("Takie nazwisko posiadają osoby o nazwisku: ", imiona_danego_nazwiska)
print()
print("Jest ", liczba_danego_nazwiska, " takich osób")
