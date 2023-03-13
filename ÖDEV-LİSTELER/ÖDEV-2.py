# 1. 1-100 arasında 20 adet rastgele sayı üretin ve
# aynı numara içerde olmadan listeye atın.

from random import randint


sayilar: list = list()

while len(sayilar) <= 20:
    sayi: int = randint(1, 101)
    if sayi not in sayilar:
        sayilar.append(sayi)

print(sayilar)