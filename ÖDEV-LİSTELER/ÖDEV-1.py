# SORU: Kullanicidan 10 adet sayı alıp listeye
# atın ve sonrasında listenin aritmetik ortalamasını bulun.

sayi_listesi: list = list()

for i in range(1, 11):
    sayi = int(input(f"{i}. sayı: "))
    sayi_listesi.append(sayi)

print(sum(sayi_listesi) / len(sayi_listesi))
