books = [
    {
        "name": "Pán prstenů: Společenstvo prstenu",
        "price": 500,
        "author": "J.R.R. Tolkien",
        "publication_year": 1954,
    }
]

# 1: Přidej do proměnné 'books' 2 libovolné knihy, údaje mohou být libovolné. Vypiš list.
books.append({
    "name": "Atomové návyky",
    "price": 650,
    "author": "James Clear",
    "publication_year": 2010,
})

books.append({
    "name": "1984",
    "price": 280,
    "author": "George Orwell",
    "publication_year": 1949,
})

print("Seznam knih po přidání dvou nových:")
for book in books:
    print(book)

# 2. Změň cenu jedné libovolné knihy. Vypiš list.
books[0]["price"] = 550  # Změna ceny první knihy (Pán prstenů)

print("\nSeznam knih po změně ceny:")
for book in books:
    print(book)

# 3. Odstraň nějakou knihu. Vypiš list.
del books[1]  # Odstranění druhé knihy (Atomové návyky)

print("\nSeznam knih po odstranění jedné knihy:")
for book in books:
    print(book)

# 4. Vypiš celkový počet knih v listu.
print(f"\nCelkový počet knih: {len(books)}")

# Bonusový úkol
print("\nPřidání nové knihy pomocí uživatelského vstupu:")
name = input("Zadej název knihy: ")
price = int(input("Zadej cenu knihy: "))
author = input("Zadej autora knihy: ")
year = int(input("Zadej rok vydání: "))

books.append({
    "name": name,
    "price": price,
    "author": author,
    "publication_year": year,
})

print("\nAktualizovaný seznam knih:")
for book in books:
    print(book)





# 1: Přidej do proměnné 'books' 2 libovolné knihy, údaje mohou být libovolné. Vypiš list.

# 2. Změň cenu jedné libovolné knihy. Vypiš list.

# 3. Odstraň nějakou knihu. Vypiš list.

# 4. Vypiš celkový počet knih v listu.

# Bonusový úkol (dobrovolné): Přidej 1 knihu pomocí uživatelského vstupu (https://www.w3schools.com/python/ref_func_input.asp)