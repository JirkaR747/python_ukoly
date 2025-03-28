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

def print_user_info(user: []) -> None:
    if user["succes"]:
        print(f"Jméno: {user["username"]} ,věk: {user["age"]}, email: {user["email"]}")
    else:
        print(user["error"])




#   funkce vytvořené mad rámec úkolu
# funkce pro vytvoření menu

# funkce pro přidání nového uživatele
def new_user() ->[]:
    list_users=[]
    username=input("Zadej jméno")
    age=input("Zadej věk")
    email=input("zadej email")
    return list_users


# menu
def menu() -> None:
    while True:
        print("Pokračuj stiskem klávesy")
        char_menu=input("(Z)adej nového uživatele , (V)ypiš všechny uživatele , (K)onec").lower()
        if char_menu == "z" :
            list_users.append(new_user())

        if char_menu == "v":
            print("ano V")

        if char_menu == "k":
            print("ano K")




menu()


# deklarace proměných
# list pro uložení všech slovníků s uživateli
#list_users = []
#user={}