import random
import string
import os

numdrbszamok = []
numalhatarok = []
numfelhatarok = []
strdrbszamok = []

def inputnum():
    drb = int(input("Adott darabszam "))
    alhatar = int(input("alsohatar "))
    felhatar = int(input("felsohatar "))
    numdrbszamok.append(drb)
    numalhatarok.append(alhatar)
    numfelhatarok.append(felhatar)
    
    return drb, alhatar, felhatar

def inputstr():
    drb = int(input("Adott darabszam "))
    strdrbszamok.append(drb)

    return drb

def gennum():
    drb, alhatar, felhatar = inputnum()

    f = open("ki.txt", "a", encoding="utf8")
    for count,a in enumerate(range(drb)):
        if count == 0:
            f.write(f"{random.randint(alhatar, felhatar)}")
        else:
            f.write(f";{random.randint(alhatar, felhatar)}")
    f.write("\n")
    f.close()
    

def genstr():
    drb = inputstr()
    abc = string.ascii_letters

    f = open("ki.txt", "a", encoding="utf8")

    for count,a in enumerate(range(drb)):
        lista = ""
        for a in range(random.randint(1, 20)):

            lista += random.choice(abc)
        if count == 0:
            f.write(f"{lista}")
        else:
            f.write(f";{lista}")
    f.write("\n")

    f.close()

def checknums():
    if os.path.exists("ki.txt") and os.stat("ki.txt").st_size == 0:
        print("A ki.txt fájl üres.")
        return
    drb, alhatar, felhatar = inputnum()
    with open("ki.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            try:
                numbers = list(map(int, line.strip().split(";")))
                if all(alhatar <= n <= felhatar for n in numbers) and len(numbers) == drb:
                    print(f"{line.strip()} megfelel a feltételeknek.")
                else:
                    print(f"{line.strip()} nem felel meg a feltételeknek.")
            except ValueError:
                continue

def checkstrs():
    if os.path.exists("ki.txt") and os.stat("ki.txt").st_size == 0:
        print("A ki.txt fájl üres.")
        return
    drb = inputstr()
    with open("ki.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            strings = line.strip().split(";")
            if all(s.isalpha() and (1 <= len(s) <= 20) for s in strings) and len(strings) == drb:
                print(f"{line.strip()} megfelel a feltételeknek.")
            else:
                print(f"{line.strip()} nem felel meg a feltételeknek.")

def menu():
    print("Válasszon az alábbi lehetőségek közül:")
    print("1. Véletlen egész számok generálása")
    print("2. Véletlen szöveg generálása")
    print("3. Számok ellenőrzése")
    print("4. Szövegek ellenőrzése")

    choice = int(input("Adja meg a választott lehetőséget (1-4): "))
    
    if choice == 1:
        gennum()
    elif choice == 2:
        genstr()
    elif choice == 3:
        checknums()
    elif choice == 4:
        checkstrs()
    else:
        print("Érvénytelen választás.")

menu()
