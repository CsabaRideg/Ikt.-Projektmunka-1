path = input(f"Adja meg a beolvasni kívánt fájl elérési útvonalát(pl:'ki.txt'). -- ")
inbetween = input(f"Milyen jellel vannak az adatok elválasztva? -- ")

f = open(path,'r',encoding='utf8')
lines = f.readlines()
f.close()
lines = [line.strip().split(inbetween) for line in lines]
arrange_together = 0
if len(lines) > 1:
    arrange_together = input("Az állományban több sorban is vannak adatok. Egybe legyenek rendezve vagy külön soronként? 0/1 -- ")
    if arrange_together == 0:
        lines = ["".join(lines)]

def arrangement(list): #Cserés rendezés
    for count,word in enumerate(list):
        if count != 0:
            current = count
            before = count-1
            if list_type == 'text':
                while list[current].upper() < list[before].upper():
                    if list[current].upper() > list[before].upper():
                        break
                    if before == 0:
                        list[before],list[current] = list[current],list[before]
                        break
                    if list[current].upper() < list[before].upper():
                        list[before],list[current] = list[current],list[before]
                    current -=1
                    before-=1
            else:
                while list[current] < list[before]:
                    if list[current] > list[before]:
                        break
                    if before == 0:
                        list[before],list[current] = list[current],list[before]
                        break
                    if list[current] < list[before]:
                        list[before],list[current] = list[current],list[before]
                    current -=1
                    before-=1
    return list

def arrangement2(list): #Shell rendezés
    max_square = 2
    square= 2
    while True:
        if max_square < len(list)/2:
            max_square = int(max_square*2)
        if max_square > len(list)/2:
            max_square = int(max_square/2)
            break
    while max_square >= square:
        for count,word in enumerate(list):
            test_count = count
            gap = int(len(list)/square)
            little_list = []
            while len(little_list) != square:
                little_list.append(list[test_count])
                test_count += gap
                if test_count >= len(list):
                    break
            test_count = count
            arrangement(little_list)
            while len(little_list) != 0:
                list[test_count] = little_list[0]
                little_list.remove(little_list[0])
                test_count += gap
            if count == gap:
                square = int(square*2)
                break
    arrangement(list)
    return list       

items = []
list_types = []
correct_list = True
for count,line in enumerate(lines):
    if all(i.isnumeric() for i in lines[count]):
        line = [int(i) for i in line]
        items.append(line)
        list_types.append('szám')
    elif all(i.isalpha() for i in lines[count]):
        items.append(lines)
        list_types.append('szöveg')
    else:
        for item in line:
            if all(i.isnumeric() for i in item)==False and all(i.isalpha() for i in item)==False:
                print('Helytelen adat van az adathalmazba --> Rendezés lehetetlen. :(')
                exit()
        print(f"A {count+1}. listád helytelen!")
        mixed_list = input(f"A {count+1}. listád tartalmaz számhalmazokat és betühalmazokat is. Külön legyen rendezve vagy egybe? 0/1 -- ")
        if mixed_list == 1:
            list_types.append('vegyes')
            items.append(line)
        elif mixed_list ==0:
            numbers,words = [],[]
            for item in line:
                if all(i.isnumeric() for i in item):
                    numbers.append(item)
                elif all(i.isalpha() for i in item):
                    words.append(item)
            list_types.append('külön')
            items.append([numbers,words])


arrangement_type = int(input('Melyik rendezési módszerrel legyen rendezve a lista? 1/2 -- '))
if arrangement_type == 1:
    list_arranged = arrangement(items)
elif arrangement_type == 2:
    list_arranged = arrangement2(items)

sequence = int(input('Növekvő vagy Csökkenő legyen a sorrend? 1/-1 -- '))
if sequence == -1:
    print(list_arranged[::-1])
elif sequence == 1:
    print(list_arranged)

add_new = int(input(f"Szeretne új elemet hozzáadni a listához? 0/1 -- "))
while add_new != 0:
    print(f"Az új a elem {list_type} kell ,hogy legyen!")
    new_item = input(f"Adjon meg egy új elemet. -- ")
    for char in new_item:
        if type != 'text' and char.isalpha():
            print(f"Az elem minden karaktere {list_type} kell hogy legyen!")
        if type != 'number' and char.isnumeric():
            print(f"Az elem minden karaktere {list_type} kell hogy legyen!")
    for count,i in enumerate(items):
        if i.upper() > new_item.upper():
            items.insert(count,new_item)
            break
    add_new = int(input(f"Szeretne új elemet hozzáadni a listához? 0/1 -- "))