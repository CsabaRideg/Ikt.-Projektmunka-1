path = input(f"Adja meg a beolvasni kívánt fájl (relatív) elérési útvonalát (pl:'ki.txt'). -- ")
inbetween = input(f"Milyen jellel vannak az adatok elválasztva? -- ")
f = open(path,'r',encoding='utf8')
lines = f.readlines()
f.close()
lines = [line.strip().split(inbetween) for line in lines]
if len(lines) > 1:
    arrange_together = int(input("Az állományban több sorban is vannak adatok. Egybe legyenek rendezve vagy külön soronként? 0/1 -- "))
    if arrange_together == 0:
        lines = ["".join(lines)]

def arrangement1(list): #Cserés rendezés
    for count,word in enumerate(list):
        if count != 0:
            current = count
            before = count-1
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
            arrangement1(little_list)
            while len(little_list) != 0:
                list[test_count] = little_list[0]
                little_list.remove(little_list[0])
                test_count += gap
            if count == gap:
                square = int(square*2)
                break
    arrangement1(list)
    return list       

def number_converter(list): #Számok elé 0-kat pakolás  
    numbers = []
    for item in list:
        if item.isnumeric():
            numbers.append(int(item))
    length = len(str(max(numbers)))
    numbers = [str(i) for i in numbers]
    for count,number in enumerate(numbers):
        list.remove(number)
        if len(number) != length:
            numbers[count] = (length-len(number))*'0' + number
    list = numbers + list
    return list

def number_reverter(list): # Számok elöl 0-kat eltöntetés
    for count,item in enumerate(list):
        if item.isnumeric():
            list[count] = str(int(item))
    return list

lists = []
correct_list = True
for count,line in enumerate(lines):
    if all(i.isnumeric() for i in lines[count]):
        lists.append(number_converter(line))
    elif all(i.isalpha() for i in lines[count]):
        lists.append(line)
    else:
        for item in line:
            if all(i.isnumeric() for i in item)==False and all(i.isalpha() for i in item)==False:
                print('Helytelen adat van az adathalmazba --> Rendezés lehetetlen. :(')
                exit()
        mixed_list = int(input(f"A {count+1}. lista tartalmaz számokat és betühalmazokat is. Egybe vagy kölön a számokat és külön a betűhalmazokat rendezve? 0/1 -- "))
        if mixed_list == 0:

            lists.append(number_converter(line))
        elif mixed_list == 1:
            numbers= []
            words = []
            for item in line:
                if all(i.isnumeric() for i in item):
                    numbers.append(item)
                elif all(i.isalpha() for i in item):
                    words.append(item)
            lists.append([number_converter(numbers),words])
print(lists)

arrangement_type = int(input('Melyik rendezési módszerrel legyen rendezve a lista? 1/2 -- '))
sequence = int(input('Növekvő vagy Csökkenő legyen a sorrend? 1/-1 -- '))
for count,i in enumerate(lists):
    if len(i) ==2:
        if isinstance(i[1],list):
            if arrangement_type == 1:
                all(lists[count][count2] == arrangement1(i2)[::sequence] for count2,i2 in enumerate(i))
            elif arrangement_type == 2:
                all(lists[count][count2] == arrangement2(i2)[::sequence] for count2,i2 in enumerate(i))
    else:
        if arrangement_type == 1:
            lists[count] == arrangement1(i)[::sequence]
        elif arrangement_type == 2:
            lists[count] == arrangement2(i)[::sequence]

for i in lists:
    print(i)
add_new = int(input(f"Szeretne új elemet hozzáadni a listához? 0/1 -- "))
list_number = int()
while add_new != 0:
    new_item = input(f"Adjon meg egy új elemet. -- ")
    for char in new_item:
        if type != 'text' and char.isalpha():
            print(f"Az elem minden karaktere kell hogy legyen!")
        if type != 'number' and char.isnumeric():
            print(f"Az elem minden karaktere kell hogy legyen!")
    for count,i in enumerate(lists[0]):
        if i.upper() > new_item.upper():
            lists.insert(count,new_item)
            break
    add_new = int(input(f"Szeretne új elemet hozzáadni a listához? 0/1 -- "))