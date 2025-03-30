# Napiš program, který bude pracovat s informacemi o uživatelském účtu: username, age, email
#
#
# Vytvoř následující funkce:
#
# is_adult: Funkce ověří zda je uživatel dospělý
# is_name_valid: Funkce ověří zda uživatelské jméno je alespoň 4 znaky dlouhé
# create_user:
#   Funkce vytvoří slovník reprezentujícího uživatele.
#  Uvnitř funkce zkontroluj, zda je uživatel dospělý a jeho jméno je validní.
# Pokud je vše v pořádku, create_user vrátí následující slovník:
# {
# "success": True,
# "user": {"username": "...", "age": ..., "email": "..."}
# }
#  Pokud validace selže, create_user vrátí:
# {
# "success": False,
# "error": "Chybová zpráva..."
# }
#
#
# print_user_info: Funkce vytiskne uživatele do konzole s libovolným formátováním, případně vytiskne chybovou zprávu při neúspěšném vytvoření
#
# Pomocí metody create_user vytvoř alespoň 4 různé uživatele. Hodnoty si zvol podle sebe přímo v programu.
#
# Nakonec vytvořené uživatele vytiskni pomocí cyklu a metody print_user_info.


# funkce ověčí zda je uživatel dospělý
def is_adult(age: int) -> bool:
    if age > 18:
        return True
    else:
        return False


# funkce ověří zda jde o platné jméno
def is_name_valid(user_name: str) -> bool:
    if len(user_name) >= 4:
        return True
    else:
        return False


# funkce pro vytvoření slovníku reprezentující uživatele

def create_user(username: str, age: int, email: str) -> {}:
    if is_adult(age) == False:
        return {"succes": False, "error": "Chyba vstupních dat: věk je příliš nízký"}
    if is_name_valid(username) == False:
        return {"succes": False, "error": "Chyba vstupních dat: jméno musí mít minimálně čtyři znaky"}

    return {"succes": True, "user": {"username": username, "age": age, "email": email}}


# funkce print pro vytištění uživatele do konzole, funkce rovněž tiskne chybové stavy

def print_user_info(user: dict) -> None:
    if user["succes"]:
        print(f"Jméno: {user["user"]["username"]} ,věk: {user["user"]["age"]}, email: {user["user"]["email"]}")
    else:
        print(user["error"])


# deklarace proměných
# list pro uložení všech slovníků s uživateli
list_users = []




jmeno1 = "Karel123"
age1 = 24
email1 = "karel123@atlas.cz"

jmeno2 = "pavel8"
age2 = 13
email2 = "pavel@seznam.cz"

jmeno3 = "jarda"
age3 = 54
email3 = "jarda@seznam.cz"

jmeno4 = "kuk"
age4 = 25
email4 = "kuk@kuk.com"

# tato sekvence by se za normálních okolností načítala ve funkci a v cyklu


user = create_user(jmeno1, age1, email1)
if user["succes"]:
    list_users.append(user)
else:
    print_user_info(user)

user = create_user(jmeno2, age2, email2)
if user["succes"]:
    list_users.append(user)
else:
    print_user_info(user)

user = create_user(jmeno3, age3, email3)
if user["succes"]:
    list_users.append(user)
else:
    print_user_info(user)

user = create_user(jmeno4, age4, email4)
if user["succes"]:
    list_users.append(user)
else:
    print_user_info(user)

print("Výpis uživatelů v cyklu")
for user in list_users:
    print_user_info(user)
