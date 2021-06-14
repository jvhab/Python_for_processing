def deposit(name, sum):
    bank[name] = bank.get(name, 0) + int(sum)

def income (per):
    percent = int(per)
    for i, j in bank.items():
        if j > 0:
            bank[i] = int(bank.get(i, 0) + (bank.get(i, 0) * percent) / 100)

def withdraw(name, minus):
    bank[name] = bank.get(name, 0) - int(minus)

def balance(name):
    if name in bank:
        return bank[name]
    else:
        return 'ERROR'

def transfer(name1, name2, sum):
    bank[name1] = bank.get(name1, 0) - int(sum)
    bank[name2] = bank.get(name2, 0) + int(sum)

bank = {}
vivod = []
kolOp = int(input())
for i in range(kolOp):
    myStr = tuple(map(str, (input().split())))
    if myStr[0] == 'INCOME':
        income(myStr[1])

    elif myStr[0] == 'DEPOSIT':
        deposit(myStr[1], myStr[2])

    elif myStr[0] == 'WITHDRAW':
        withdraw(myStr[1], myStr[2])

    elif myStr[0] == 'BALANCE':
         vivod.append(balance(myStr[1]))

    elif myStr[0] == 'TRANSFER':
        transfer(myStr[1], myStr[2], myStr[3])
print('\n'.join(map(str, vivod)))
