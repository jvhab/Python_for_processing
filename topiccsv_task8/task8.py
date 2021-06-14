fin = open('input_6_3_1.csv', 'r', encoding='utf8')     # Чтение файла
vals = {}
vals2 = {}
vals3 = {}
finish = {}

for line in fin:                                        # Перебор всех строк из файла
    now = line.split(';')                               # Разделение строк по знаку ';'
    vals2[now[0]] = vals2.get(now[0], 0) + 1            # Подсчет одинаковых ключей
    vals[now[0]] = vals.get(now[0], 0) + int(now[1])    # Сумма зачений одинаковых ключей
    vals3[now[0]] = vals[now[0]], vals2[now[0]]         # Запись в словарь в виде: / ключ: (сумма, количество)

fin.close()

for i, j in vals3.items():                              # Перебор словаря
    znach = j[0] // j[1]
    finish[i] = znach
MySort = sorted(finish, key=lambda x: finish[x])        # Сортировка по значению в ключе
print('\n'.join(MySort))
