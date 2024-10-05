import string
import time
ABC = string.ascii_letters
NUM = [0,1,2,3,4,5,6,7,8,9]

f = open('ki.txt','r',encoding='utf8')
lines = f.readlines()
f.close()

def arrangement(list): #cserés rendezés
    for count,word in enumerate(list):
        if count != 0:
            current = count
            before = count-1
            if Type == 'text':
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
            max_square = int(max_square *2)
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
correct_chars = True
for line in lines:
    line = line.strip().split(";")
    for item in line:
        if item[0] in ABC:
            Type = 'text'
        elif int(item[0]) in NUM:
            Type = 'number'
        for char in item:
            if correct_chars:
                if Type == 'text':
                    if char not in ABC:
                        correct_chars = False
                elif Type == 'number':
                    if int(char) not in NUM:
                        correct_chars = False
        if Type =='text':
            items.append(item)
        elif Type =='number':
            items.append(int(item))

if correct_chars == False:
    print('Helytelen adathalmaz.')

arrangement_type = int(input('Melyik rendezési módszerrel legyen rendezve a list? 1/2 -- '))
if arrangement_type == 1:
    list_arranged = arrangement(items)
elif arrangement_type == 2:
    list_arranged = arrangement2(items)

sequence = int(input('Növekvő vagy Csökkenő legyen a sorrend? 1/-1 -- '))
if sequence == -1:
    print(list_arranged[::-1])
if sequence == 1:
    print(list_arranged)