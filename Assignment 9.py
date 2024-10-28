row = 5
column = 5

for i in range(row):
    for j in range(column):
        if i % 2 == 0:
            print('1',end='')
        else:
            print('0',end='')
    print()