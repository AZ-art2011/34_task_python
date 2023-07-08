# 34_task

def check_rhythm(string):
    string = string.split()
    temp_list = []
    
    for word in string:
        res = 0
    
        for i in word:
            if i in 'аеёиоуыэюя':
                res += 1
        temp_list.append(res)
    return len(temp_list) == temp_list.count(temp_list[0])

string = input('Пример для ввода: пара-ра-рам рам-пам-папам па-ра-па-дам ')

if check_rhythm(string):
    print('Парам пам-пам')
else:
    print('Пам парам')