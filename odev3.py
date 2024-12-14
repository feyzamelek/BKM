sayilar = [3,5,7,2,12,32,45]

# 1- "sayilar" listesindeki her bir elemanı yazdırınız.
for x in sayilar:
    print(x)


# 2- "sayilar" listesinde hangi sayılar 3' ün katıdır?
ucun_katlari= [sayi for sayi in sayilar if sayi % 3 == 0]

print("3'ün katı olan sayılar:", ucun_katlari)



# 3- "sayilar" listesinde tüm sayıların toplamı nedir?

toplam =(3+5+7+2+12+32+45)

print("Sayıların toplamı:", toplam)



urunler = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]

# 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz. (index ve find komutlarından faydalanınız.)



# 5- "urunler" listesinde kaç adet samsung ürünü vardır? (find metodu)