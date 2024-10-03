import random
import string

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


def checknum():
    
