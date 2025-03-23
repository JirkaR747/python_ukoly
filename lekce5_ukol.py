numbers = [1, 2, 4, -6, 7, 8, 100, -125, 11, 123]
names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
random_codes = ["1-okdsaaa", "0-nFnldd", "0-AA", "0-uwqqq", "2-ZSTh", "0-RKOcsxxx", "1-LwWtss", "0-cdKiddd", "2-KpAAaa", "3-sOdSxhcds"]

# 1. pomocí cyklu for vypište čísla ze seznamu numbers, ale přeskočte záporná čísla.

# 2. pomocí cyklu while vypište všechna jména, pokud narazíš na jméno 'Alice' cyklus ukonči

# 3. pomocí list comprehension vytvoř nový list, který bude obsahovat pouze prvky z 'random_codes', které obsahují 0

# Dobrovolny ukol pro pokrocile (nebude bodovan): Vypis všechny pod-seznamy s alespoň třemi po sobě jdoucími stejnými znaky v seznamu 'random_codes'



# úkol 1 - v cyklu se vypíší jen kladná čísla

print("úkol číslo 1 : ")
for number in numbers:
    if number >0:
        print(number)

# úkol 2 - cyklus vypíše všechna jména a skončí pokud narazí na Alice
print("úkol číslo 2 : ")
i=0
while True:
    if names[i] == "Alice":
        break
    print(names[i])
    i+=1

# úkol 3 - cyklus vybere jen čísla která obsahují dvě nuly

zero_list= [code for code in random_codes if "0" in code]

print(zero_list)


