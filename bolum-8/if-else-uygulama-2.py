# Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen değerlendirmeyi yazdırınız.

#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

yazili1 = float(input("yazılı 1: "))
yazili2 = float(input("yazılı 2: "))
proje = float(input("proje: "))

ortalama = (yazili1 + yazili2 + proje) / 3

if(ortalama >= 0) and (ortalama < 25):
    print(f"ortalamanız: {ortalama} ve değerlendirme notu: 0")
elif(ortalama >= 25) and (ortalama < 45):
    print(f"ortalamanız: {ortalama} ve değerlendirme notu: 1")
elif(ortalama >= 45) and (ortalama < 55):
    print(f"ortalamanız: {ortalama} ve değerlendirme notu: 2")
elif(ortalama >= 55) and (ortalama < 70):
    print(f"ortalamanız: {ortalama} ve değerlendirme notu: 3")
elif(ortalama >= 70) and (ortalama < 85):
    print(f"ortalamanız: {ortalama} ve değerlendirme notu: 4")
elif(ortalama >= 85) and (ortalama <= 100):
    print(f"ortalamanız: {ortalama} ve değerlendirme notu: 5")
else:
    print("yanlış not bilgisi")

