zakres_min=-5
zakres_max=5

lista = []
for i in range(zakres_min, zakres_max):
        lista.append(i+2)
        while i > zakres_max:
            break
print(lista)

# lista z zakresu - liczby lustrzane
a = list(range(zakres_min,zakres_max+1, 2))
print(a)

# wyświetlanie co drugi element od końca
print(a[::-2])

# odwracanie funkcją reversed
b=list(reversed(a))
print(b)

# modyfikuje oryginalną listę
a.reverse()
print(a)

# liczenie znaków w wyrażeniu
from collections import Counter

wyrazenie = "Programuję w Pythonie i nie pogardzę gitem."
counter = Counter(wyrazenie)

najpopularniejszy=counter.most_common(1)
najrzadszy=counter.most_common()[-1]

# wystąpienia znaków
for znak, wystapienie in counter.items():
    print(znak, wystapienie / len(wyrazenie)*100)

print(najpopularniejszy)
print(najrzadszy)


# lista
evens = list(range(0,101,2))

div_by_6 = []
for n in evens:
    if n %6 == 0:
        div_by_6.append(n)
print(div_by_6)
print('---'*25)
# list comprehension
podzielne_przez_6 = [n for n in evens if n %6 == 0]
print('podzielne przez 6:', podzielne_przez_6)

do_kwadratu = [n**2 for n in podzielne_przez_6]
print('do kwadratu:', do_kwadratu)

# wszystko w jednej linii
wszystko = [n**2 for n in evens if n %6 == 0]

print('wszystko:', wszystko)