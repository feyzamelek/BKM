# # 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
# def yazma():
#     for i in range(10):
#         print("Feyyaz")
# yazma()

# # 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
# kısa_kenar= 12
# uzun_kenar= 15

# def cevre():
#     return(12+15)*2
# sonuc1= cevre()
# print(sonuc1)

# def alan():
#     return(12*15)
# sonuc2= alan()
# print(sonuc2)


# # 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)

# import random
# def yazi_tura():
#     sonuc = random.choice(['yazı', 'tura'])
#     return sonuc
# print(yazi_tura())


# # 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
# sayi1 = 18
# sayi2 = 28
# def arasindaki_asal_sayilar(sayi1, sayi2):
#     def asal_kontrol(sayi):
#         if sayi < 2:
#             return False
#         for i in range(2, int(sayi ** 0.5) + 1):
#             if sayi % i == 0:
#                 return False
#             return True
#         baslangic = min(sayi1, sayi2) + 1
#         bitis = max(sayi1, sayi2)
#         return [sayi for sayi in range(baslangic, bitis) if asal_kontrol(sayi)]
#     print(arasindaki_asal_sayilar(sayi1, sayi2))



# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

sayi=65
def tamBolen(sayi):
    return[i for i in range (1, sayi +1) if sayi % i == 0]
print(tamBolen(sayi))