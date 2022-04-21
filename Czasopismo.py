class Czasopismo:
    def __init__(self, nazwa, wydawnictwo, rok_założenia, rok_ostatniego_numeru, ilosc_wydań_w_roku, liczba_stron, cena):
        self.nazwa = nazwa 
        self.wydawnictwo = wydawnictwo
        self.rok_założenia = rok_założenia
        self.rok_ostatniego_numeru = rok_ostatniego_numeru
        self.ilosc_wydań_w_roku = (rok_ostatniego_numeru - rok_założenia) / ilosc_wydań_w_roku
        self.liczba_stron = liczba_stron
        self.cena = cena > 0

    def wirtualna_sluzaca_do_wyswietlania_danych(self):
         print(f"Nazwa: {self.nazwa}")
         print(f"Wydawnictwo: {self.wydawnictwo}")
         print(f"Rok założenia: {self.rok_założenia}")
         print(f"Rok ostatniego numeru: {self.rok_ostatniego_numeru}")
         print(f"Ilość wydań w roku: {self.ilosc_wydań_w_roku}")
         print(f"Liczba stron: {self.liczba_stron}")
         print(f"Cena: {self.cena}") 

czasopismo01 = Czasopismo("Nazwa", "Wydawnictwo", 2000, 2020, 12, 100, 100)

print(czasopismo01.wirtualna_sluzaca_do_wyswietlania_danych())


class Kwartalnik(Czasopismo):
    def __init__(self, nrISBN, miesiac_1_wydania_w_roku, redaktor):
        self.nrISBN = nrISBN
        self.miesiac_1_wydania_w_roku = miesiac_1_wydania_w_roku
        self.redaktor = redaktor

    def abstrakcyjna_sluzaca_do_okreslenia_typu_czasopisma(self):

        if  self.nrISBN == "":
            print("Kwartalnik nierecenzowany")

        if (self.nrISBN == "" or self.redaktor == ""):
            print("Kwartalnik nierecenzowany")

        if self.nrISBN != "" and self.redaktor != "":
            print("Kwartalnik recenzowany")

        if self.miesiac_1_wydania_w_roku == "Styczeń" or "Luty":
            print("Kwartalnik wydawany z początkiem roku")

        if self.miesiac_1_wydania_w_roku == "Marzec" or "Kwiecień":
            print("Kwartalnik wydawany z początkiem II kwartału")

        if super().rok_założenia <= 2000 and self.nrISBN != "":
            print("Kwartalnik naukowy z długoletnią tradycją")

        if super().rok_założenia >= 2009:
            print("Nowość")

kwartarnik01 = Kwartalnik("", "Styczeń", "")
print(kwartarnik01.abstrakcyjna_sluzaca_do_okreslenia_typu_czasopisma())