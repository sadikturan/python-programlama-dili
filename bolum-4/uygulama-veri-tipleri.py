"""
    Uygulama 1: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.
    Alan: πr²
    Çevre: 2πr

    Uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesaplayınız.
    mil = km / 1.609344
"""

# pi = 3.14

# r = float(input("Yarı çap: "))

# alan = pi * (r ** 2)
# cevre = 2 * pi * r

# print("Alan: " + str(alan))
# print("Çevre : " + str(cevre))

mesafeKm = input("km: ")
mesafeMil = float(mesafeKm) / 1.609344
mesafeMil = round(mesafeMil, 2)
print(mesafeKm + " km= " + str(mesafeMil) + " mil")