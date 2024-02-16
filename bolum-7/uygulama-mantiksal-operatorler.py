# 1- Yaşı 18' den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz.

veli_izni = False
yas = 18
sonuc = (veli_izni) or (yas >= 18)

# 2- Ders notu 50-100 arasındaysa geçti değilse kalsın bilgisini yazdırınız.
dersNotu = 55
sonuc = (dersNotu >= 50 and dersNotu <= 100)
print(f"ders geçme durumu: {sonuc}")

# 3- Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol ediniz.
ortalama = 75
zayifSayisi = 0
sonuc = (ortalama >= 70) and (zayifSayisi == 0)

# 4- İşe girmek için en az önlisans ya da lisans mezunu olma durumunu kontrol ediniz. Sigara kullanmama koşulu.
egitim = "önlisans"
sigara_icme = False

sonuc = (egitim == "önlisans" or egitim == "lisans") and (not(sigara_icme))

# 5- Uygulamaya giriş kontrolünü "username yada email" ve "parola" için yapalım.

email = "info@sadikturan.com"
username = "sadikturan"
password = "12345"

girilen_bilgi = input("email yada username: ")
girilen_parola = input("parola: ")

sonuc = (email == girilen_bilgi or username == girilen_bilgi) and (password == girilen_parola)

print(sonuc)