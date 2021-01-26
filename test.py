
found = False
print('Before', found)
for value in [3, 52, 18, 94, 16, 7]:
    if value == 18:
        found = True
        print(found, value)
    else:
        found = False
    print(found, value)
print('After', found)

print('\n')
found = False
foundcount=0
print('Before', found)
for value in [9,41,12,3,74,15]:
    if value==3:
        found = True
        foundcount=foundcount+1
    print(found,value)
    found = False
print('Found',foundcount,'True')

print('\n')
found = False
print('Before', found)
while found == False:
    for value in [9, 41, 12, 3, 74, 15]:
        if value == 3:
            found = True
    print(found, value)
print('After', found)