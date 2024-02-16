"""
Aşağıdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde saklayınız.
Toplam ödenen ücret nedir?
Ödenen miktarın kdv oranı nedir? (%18)

Sadık Turan
05321234567
info@sadikturan.com
Kocaeli

Satın Alınan Ürünler

Ürün adı: Kablosuz Mouse
Fiyatı: 550 TL

Ürün adı: Kablosuz Klavye
Fiyatı: 650 TL

Ürün adı: Dizüstü Bilgisayar
Fiyatı: 55.000 TL

"""

musteriAd = "Sadık"
musteriSoyad = "Turan"
musteriTelefon = "05321234567"
musteriEmail = "info@sadikturan.com"
musteriAdres = "Kocaeli"

urun1Ad = "Kablosuz Mouse"
urun1Fiyat = 550

urun2Ad = "Kablosuz Klavye"
urun2Fiyat = 650

urun3Ad = "Dizüstü Bilgisayar"
urun3Fiyat = 55000

toplamOdenenUcret = urun1Fiyat + urun2Fiyat + urun3Fiyat
print("Toplam ödenen miktar: " + str(toplamOdenenUcret))
print("Toplam kdv oranı: " + str(toplamOdenenUcret * 0.18))

# str(100) => "100" + "Ali" => 100Ali