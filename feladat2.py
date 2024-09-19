f = open('ki.txt','r',encoding='utf8')
lines = f.readlines()
f.close
ABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
NUMBERS = [0,1,2,3,4,5,6,7,8,9]
random_numbers = []
random_words = []
correct_chars = True
for line in lines: 
    line  = line.strip().split(';')
    for item in line:
        print(item[0])
        if item[0].upper() in ABC:
            Type = 'text'
            
        elif int(item[0]) in NUMBERS:
            Type = 'number'
        for char in item:
            if correct_chars:
                if Type == 'text':
                    if char not in ABC:
                        correct_chars = False
                    else:
                        print('betu')
                        random_words.append(str(item))
                if Type == 'number':
                    if char not in NUMBERS:
                        correct_chars = False
                    else:
                        print('szam')
                        random_numbers.append(int(item))
print(random_numbers)
print(random_words)
if correct_chars == False:
    print('Hibás adathalmaz.')


