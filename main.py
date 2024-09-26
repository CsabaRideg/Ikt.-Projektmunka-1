import random
import string

def gen1():
    drb = int(input("Adott darabszam "))
    alhatar = int(input("alsohatar "))
    felhatar = int(input("felsohatar "))

    f = open("ki.txt", "a", encoding="utf8")
    for count,a in enumerate(range(drb)):
        if count == 0:
            f.write(f"{random.randint(alhatar, felhatar)}")
        else:
            f.write(f";{random.randint(alhatar, felhatar)}")
    f.write("\n")
    f.close()
    

def gen2():
    drb = int(input("Adott darabszam "))
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


gen2()
