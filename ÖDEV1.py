# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.

markalar = ["toyata", "Bmw", "Renault", "Mercedes"]

#2- Liste kaç elemanlıdır?

print(len(markalar))

# 3- Listenin ilk ve son elemanı nedir?

print(markalar[0])
print(markalar[-1])

# 4- "Renault" markasını "Togg" ile güncelleyiniz.

markalar[2]= "togg"

# 5- "Togg" listenin bir elemanı mıdır?

sonuc= "togg" in markalar
print(sonuc)

# 6- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.

print(markalar + ["ford" , "citroen"])


# 7- Listenin son elemanını siliniz.

del(markalar[-1])
print(markalar)

# 8- Aşağıdaki verileri liste içerisinde saklayınız (Liste içinde liste mümkündür.).

    # öğrenci1: Yiğit Bilgi 2010 [70,80,90]
    # öğrenci2: Ada Bilgi   2011 [70,70,80]
    # öğrenci3: Çınar Turan 2017 [60,60,90]

ogrenci1=["Yiğit", "Bilgi", 2010, [70,80,90]]
ogrenci2=["Ada", "Bilgi", 2011, [70,70,80]]
ogrenci3=["Çınar", "Turan", 2017, [60,60,90]]

# 9- Öğrencilerin yaşlarını hesaplayınız.

ogrenci1yas=2024-ogrenci1[2]
ogrenci2yas=2024-ogrenci2[2]
ogrenci3yas=2024-ogrenci3[2]

print(ogrenci1yas)
print(ogrenci2yas)
print(ogrenci3yas)

# 10- Öğrencilerin not ortalamalarını hesaplayınız.

yigitin_ortalamasi=(ogrenci1[3][0] + ogrenci1[3][1]+ ogrenci1[3][2])/3
adanin_ortalamasi=(ogrenci2[3][0]+ ogrenci2[3][1]+ ogrenci2[3][2])/3
cinarin_ortalamsi=(ogrenci3[3][0]+ ogrenci3[3][1]+ ogrenci3[3][2])/3

print(yigitin_ortalamasi)
print(adanin_ortalamasi)
print(cinarin_ortalamsi)


