# 2000 + 2000 * %18

urunAFiyat = 4000
urunBFiyat = 3000
kdvOrani = 0.20

print(urunAFiyat + (urunAFiyat * kdvOrani))     # ürün A
print(urunBFiyat + (urunBFiyat * kdvOrani))     # ürün B

urunToplami = urunAFiyat + urunBFiyat
print(urunToplami + (urunToplami * kdvOrani))