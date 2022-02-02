class Magazyn:
    def __init__(self, lista_produktow):
        self.lista_produktow =lista_produktow

    def wyswietl_dostepne_produkty(self):
        print('Dostępne produkty:')
        for produkt in self.lista_produktow:
            print(produkt)

    def dodaj_produkt(self):
        self.nazwa_produktu = input('Podaj nazwę produktów: >>> ')
        if self.nazwa_produktu not in self.lista_produktow:
            self.lista_produktow.append(self.nazwa_produktu)
        print(f'Produkt {self.nazwa_produktu} został wprowadzony do magazynu')

    def unun_produkt(self):
        self.nazwa_produktu = input('Podaj nazwę produktu który chcesz usunąć: >>> ')
        if self.nazwa_produktu in self.lista_produktow:
            self.lista_produktow.remove(self.nazwa_produktu)
            print('Usunięto produkt z magazynu')
        else:
            print('Nie ma takiego produktu')

magazyn  = Magazyn(['mleko', 'woda', 'jajka'])
while True:
    print("Wprowadź 1 aby wyświetlić stan magazynu")
    print("Wprowadź 2 aby dodać stan magazynu")
    print("Wprowadź 3 aby usunąć stan magazynu")
    print("Wprowadź 4 aby zakończyć")
    wybor_uzytkownia = int(input('>>> '))
    if(wybor_uzytkownia == 1):
        magazyn.wyswietl_dostepne_produkty()
    if(wybor_uzytkownia == 2):
        magazyn.dodaj_produkt()
    if(wybor_uzytkownia == 3):
        magazyn.unun_produkt()
    if(wybor_uzytkownia == 4):
        break
        
