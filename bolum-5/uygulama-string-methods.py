kursAdi = "BtkAkademi Python ile Programlama Dersleri çalışmaları"
website = "https://www.btkakademi.gov.tr/"

# 1- ' Btk Akademi ' karakter dizisinin baş ve sondaki boşluk karakterlerini siliniz. (strip)
sonuc = ' Btk Akademi '.strip()

# 2- kursAdi değişkenindeki tüm karakterleri küçük harfe çeviriniz.
sonuc = kursAdi.lower()

# 3- website değişkeninde kaç tane '.' karakteri vardır?
sonuc = website.count('.')

# 4- website değişkeni 'https' ile mi başlıyor?
sonuc = website.startswith('https')

# 5- website 'tr' ile mi bitiyor?
sonuc = website.endswith('tr')

# 6- kursAdi içerisindeki tüm karakterler harflerden mi oluşuyor?
sonuc = kursAdi.isalpha()

# 7- kursAdi değişkenindeki tüm boşlukları '-' ile değiştiriniz.
sonuc = kursAdi.replace(' ', '-').replace('ç','c').replace('ı','i').replace('ş','s').lower()

# 8- kursAdi değişkenindeki Python kelimesini ReactJs ile değiştiriniz.
sonuc = kursAdi.replace('Python','ReactJs')

# 9- website değişkeni 'www' içeriyor mu?
sonuc = website.find('aaa')
# sonuc = website.index('aaa')

# 10- kursAdi değişkenini listeye çeviriniz.
sonuc = kursAdi.split()

print(sonuc[2])
print(sonuc)
