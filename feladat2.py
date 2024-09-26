import string
ABC = string.ascii_letters
NUM = [1,2,3,4,5,6,7,8,9,0]

f = open('ki.txt','r',encoding='utf8')
lines = f.readlines()
f.close

random_numbers = []
random_words = []
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
            random_words.append(item)
        elif Type =='number':
            random_numbers.append(int(item))
        
if correct_chars == False:
    print('Hibás adathalmaz.')

# asc = int(input('Növekvő = 1, Csökkrnő = 0: '))

for c,i in enumerate(random_numbers):
    if c != 0:
        place = c
        place2 = c-1 
        while random_numbers[place] <= random_numbers[place2]:
            place -=1
            place2 -=1
            if place2 == 0:
                random_numbers[place2],random_numbers[place] = random_numbers[place],random_numbers[place2]
                break
            if random_numbers[place] < random_numbers[place2]:
                random_numbers[place2],random_numbers[place] = random_numbers[place],random_numbers[place2]
            else:
                break
            print(i,random_numbers[place],place)
        print(random_numbers)


# if asc == 0:
#     random_numbers = random_numbers[0:0:-1]
print(random_numbers)






