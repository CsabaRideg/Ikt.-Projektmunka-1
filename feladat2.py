import string
ABC = string.ascii_letters
NUM = [0,1,2,3,4,5,6,7,8,9]

f = open('ki.txt','r',encoding='utf8')
lines = f.readlines()
f.close()

def arrangement_numbers(list):
    for count,char in enumerate(list):
        if count != 0:
            current = count
            before = count-1
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
    print('Hibás adathalmaz.')

sequence = int(input('Növekvő = 1, Csökkenő = 0: '))
arrangement_numbers(numbers)

if sequence == 0:
    numbers = numbers[::-1]
print(numbers)