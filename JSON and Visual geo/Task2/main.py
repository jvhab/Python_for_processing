import json

fin = open('task_9_2_1_input.json', 'r', encoding='utf8')
dct = json.loads(fin.read())
fin.close()
popup = dct['menu']['popup']
menuitem = popup['menuitem']
for now in menuitem:
    for key in sorted(now):
        print(key, now[key])