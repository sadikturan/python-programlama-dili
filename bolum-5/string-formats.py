# string concat
ad = "Sadık"
soyad = "Turan"
yas = 40

# msj = "My name is " + ad + " " + soyad + "." + "I'm " + str(yas) + " years old."

# string format
# msj = "My name {} {}. I'm {} years old.".format(ad, soyad, yas)
# msj = "My name {0} {1}. I'm {2} years old.".format(ad, soyad, yas)
# msj = "My name {a} {s}. I'm {y} years old.".format(a=ad, s=soyad, y=yas)

# f-string
msj = f"My name {ad} {soyad}. I'm {yas} years old."

print(msj)
