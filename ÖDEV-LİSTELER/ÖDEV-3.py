# SORU: Klavyeden alınan 5 kelimeyi bir listeye atın.
# Girilen 6. kelimenin listede olup olmadığını ekrana yazdırınız.

kelimeler: list = list()
sayac: int = 1

while sayac < 7:
    kelime = input("Bir kelime girin: ")

    if sayac < 6:
        if kelime not in kelimeler:
            kelimeler.append(kelime)
            sayac += 1
        else:
            print(f"Girmiş olduğunuz {kelime} kelimeler listesinde mevcut")
    else:
        if kelime in kelimeler:
            print(f"{kelime}  kelimesi kelimeler listesinde mevcut")
            break
        else:
            print(f"{kelime}  kelimesi kelimeler listesinde mevcut değil")
            break