
print('This is a program that finds the average')
print("type 'Done' or 'done' to stop\n")

total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    elif inp == 'Done':
        break
    value = float(inp)
    total = total + value
    count += 1

average = total / count
print('Average', average)
print('\n')


num_list = []
while True:
    inp = input('Enter a number: ')
    if inp == 'Done': break
    elif inp == 'done': break
    value = float(inp)
    num_list.append(value)
average = sum(num_list) / len(num_list)
print('Average', average)