fin = open('input_6_3_2.csv', 'r', encoding='utf8')
fout = open('newfile.csv', 'w', encoding='utf8')
work = []
for line in fin:
    myLine = line.split(';')
    myLine[0], myLine[1] = int(myLine[1]), myLine[0]
    print(';'.join(map(str, myLine)), file=fout)