isbn = input("Enter ISBN No: ")

odd = isbn[::2]
even = isbn[1::2]

def add(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum

total = add(odd) + add(even) * 3
reminder = total % 10

if reminder == 0:
    print(f'Check Number = {reminder}')
else:
    check_no = 10 - reminder
    print(f'Check Number = {check_no}')
