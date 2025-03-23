#program pro určení ceny tramvajových jízdenek


# rogram bude pracovat se třemi údaji: věk zákazníka, cena vstupenky a zda je nakupující zaměstnancem tramvajové služby.
# Hodnoty pro údaje můžeš určit libovolně přímo v kódu [+0B],
# nebo je můžeš načíst z uživatelského vstupu - pomocí funkce input [+1B],
# pokud ještě navíc ukončíš program s chybovou hláškou, když je zadaný datový typ špatný, dostaneš [+1B]
# Program určí a následně vypíše konečnou cenu na základě těchto kritérií:
# Plná cena jízdenky je 45 Kč.
# Cestující do 12 let jezdí zdarma.
# Cestující mladší 18 let má slevu 50%.
# Cestující nad 65 let mají 30% slevu.
# Zaměstnanci tramvajové služby mají slevu 80%.
# Zaměstnanci tramvajové služby nad 55 let mají jízdenku zdarma.
# Bonusový úkol (Pokud ho nebudete mít hotový, nebude to mít vliv na váš celkový výsledek, body za něj nebudou odečítány.):
# Při zadání špatného datového typu se program neukonči, ale vyzve uživatele o nové zadání hodnoty.
#
# Úkol odevzdejte jako soubor .py

cena=None
plna_cena=45
mladsi_18=plna_cena*0.5
mladsi_12=0
starsi_65=plna_cena*0.7
zamestnanec=plna_cena*0.2
zamestnanec_nad55=0

#zadání údajů o zákazníkovi
print("Zadej údaje zákazníka")

# zadání věku zákazníka, vstup je ošetřen blokem try - except, nekonečná smyčka while je přerušena v případě dobře zadaného vstupu příkazem break

while True:
    try:
      zakaznik_vek=input("Zadej vek zákazníka: ")

      zakaznik_vek=int(zakaznik_vek)
      break

    except ValueError:
        print("Špatně zadaná hodnota, zadej číslo")

# zadání zda jde o zaměstnance či nikoliv, vstup ohlídán pomocí bloku if - else, vstup je převeden na malé písmo
# z důvodu variability vstupu

while True:
    zakaznik_zamestnanec=input("Zadej zda je zákazník zaměstnanec (ANO/NE): ").lower()
    if zakaznik_zamestnanec == "ano" or zakaznik_zamestnanec== "ne":
        break
    else: print("Špatně zadaná hodnota, zadej ANO nebo NE")


# blok který určí výslednou cenu na základě daných podmínek

if zakaznik_zamestnanec=="ano":
    if zakaznik_vek>55:
        cena=zamestnanec_nad55
    else:cena=zamestnanec
else:
    if zakaznik_vek>65:
        cena=starsi_65
    else:
        if zakaznik_vek<18:
            if zakaznik_vek<12:
                cena=mladsi_12
            else: cena=mladsi_18
        else: cena=plna_cena
print("Výsledná cena je: ",cena)







