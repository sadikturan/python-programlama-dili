# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
markalar = ["Toyota","Bmw","Renault","Mercedes"]

# 2- Liste kaç elemanlıdır?
sonuc = len(markalar)

# 3- Listenin ilk ve son elemanı nedir?
sonuc = markalar[0]
sonuc = markalar[-1]

# 4- "Renault" markasını "Togg" ile güncelleyiniz.
markalar[2] = "Togg"
sonuc = markalar

# 5- "Togg" listenin bir elemanı mıdır?
sonuc = "Togg" in markalar
sonuc = "Togg" not in markalar

# 6- Listenin ilk 2 elemanını alınız.
sonuc = markalar[:2]

# 7- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
sonuc = markalar + ["Ford","Citroen"]

# 8- Listenin son elemanını siliniz.
del markalar[-1]
sonuc = markalar

# 9- Aşağıdaki verileri liste içerisinde saklayınız.

    # öğrenci1: Yiğit Bilgi 2010 [70,80,90]
    # öğrenci2: Ada Bilgi   2011 [70,70,80]
    # öğrenci3: Çınar Turan 2017 [60,60,90]

ogrenci1 = ["Yiğit","Bilgi",2010,[70,80,90]]
ogrenci2 = ["Ada","Bilgi",2012,[70,70,80]]
ogrenci3 = ["Çınar","Turan",2017,[60,60,90]]

ogrenciler = [ogrenci1,ogrenci2,ogrenci3]

# 10- Öğrencilerin yaşlarını hesaplayınız.
# yasYigit = 2024 - ogrenci1[2]
# yasAda = 2024 - ogrenci2[2]
# yasCinar = 2024 - ogrenci3[2]

yasYigit = 2024 - ogrenciler[0][2]
yasAda = 2024 - ogrenciler[1][2]
yasCinar = 2024 - ogrenciler[2][2]

print(yasYigit, yasAda, yasCinar)

# 11- Öğrencilerin not ortalamalarını hesaplayınız.

notYigit = (ogrenciler[0][3][0] + ogrenciler[0][3][1] + ogrenciler[0][3][2]) / 3
notAda = (ogrenciler[1][3][0] + ogrenciler[1][3][1] + ogrenciler[1][3][2]) / 3
notCinar = (ogrenciler[2][3][0] + ogrenciler[2][3][1] + ogrenciler[2][3][2]) / 3

print(notYigit, notAda, notCinar)
