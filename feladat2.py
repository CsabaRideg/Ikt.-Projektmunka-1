import string
import time
ABC = string.ascii_letters
ABC_numbered = [['a',1],['b',2],['c',3],['d',4],['e',5],['f',6],['g',7],['h',8],['i',9],['j',10],['k',11],['l',12],['m',13],['n',14],['o',15],['p',16],['q',17],['r',18],['s',19],['t',20],['u',21],['v',22],['w',23],['x',24],['y',25],['z',26]]
NUM = [0,1,2,3,4,5,6,7,8,9]

f = open('ki.txt','r',encoding='utf8')
lines = f.readlines()
f.close()

def arrangement(list):
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

def arrangement2(list):
    print(len(list))
    for count,word in enumerate(list):
        print()
        print(f"Kiválasztott elem: {word}, {count}")
        print(list)
        word = word.lower()
        if count != 0:
            if word < list[count-1].lower() or word > list[count+1].lower():
                for letter in ABC_numbered:
                    if word[0].lower() == letter[0]:
                        list.insert(int(len(list)/26*(letter[1])),word)
                        list.remove(list[count])
            else:
                break
            current = list.index(word)
            before = current-1
            after = current + 1
            print(f"Az elem új indexe: {current}")
            while word < list[before] or word > list[after]:
                print(f"Az elötte lévő nagyobb: '{word < list[before]}', Az utána lévő kisebb '{word > list[after]}'")
                print(f"{word} a szó, elöte: {list[before]}, utána: {list[after]}")
                print(f"{list}")
                if before == 0:
                    print(f"lista Eleje")
                    list[before],word = word,list[before]
                    break
                elif after == len(list)-1:
                    print(f"lista vége")
                    list[after],word = word,list[after]
                    break
                if word > list[after] and word < list[before]:
                    print("Helyén van")
                    break
                if word < list[before]:
                    print("elotte")
                    list[before],word= word,list[before]
                    current -= 1
                    before -= 1
                    after -= 1
                elif word > list[after]:
                    print("utana")
                    list[after],word= word,list[after]
                    current +=1
                    before +=1
                    after += 1
                time.sleep(0.1)

numbers = []
words = []
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
            words.append(item)
        elif Type =='number':
            numbers.append(int(item))

if correct_chars == False:
    print('Helytelen adathalmaz.')
sequence = int(input('Növekvő = 1, Csökkenő = 0: '))
if Type == 'number':
    arrangement(numbers)
    if sequence == 0:
        numbers = numbers[::-1]
        print(numbers)
else:
    arrangement2(words)
    if sequence == 0:
        words = words[::-1]
        print(words)