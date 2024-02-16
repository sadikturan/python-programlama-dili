# 1- Girilen 2 sayıdan hangisi büyüktür?
# sayi1 = int(input("sayı 1:"))
# sayi2 = int(input("sayı 2:"))

# sonuc = (sayi1 > sayi2)
# print(f"{sayi1} {sayi2} den büyük {sonuc}")

# 2- Girilen bir sayının tek çift kontrolünü yapınız.

# sayi = int(input("sayı: "))
# sonuc = (sayi % 2 == 0)
# print(f"sayı çift: {sonuc}")

# 3- Bir öğrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz. 50 ve üstünde başarılı.

not1 = int(input("not 1: "))
not2 = int(input("not 2: "))
not3 = int(input("not 3: "))

ortalama = (not1 + not2 + not3) / 3

print(f"öğrencinin not ortalaması: {round(ortalama,2)}, başarı durumu {ortalama >= 50}")