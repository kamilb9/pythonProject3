a = list(range(1,11))
print(a)

counter=0

while counter < 11:
    print(counter)
    counter +=1

name='Py'
nr=0

print('Hello '+name+'!'+" moduł "+str(nr))
print(f'Hello {name}! moduł {nr+1}')

print('_'*40)
salary=9800
hours=160
print(f'stawka godzinowa wynosi {salary/hours:.2f} netto')
print(f'stawka godzinowa wynosi {14000/hours:.2f} brutto')

total=salary*12*35
print(f'Łącznie zarobię {total:,.2f}')



