# Bankamatik Uygulaması

# Hesap bilgileri tutulacak. (dictionary)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.


# hesap = {
#     "ad" : "Feyza Melek ALAN",
#     "hesap_No" : 65026502,
#     "bakiye": 980000,
#     "ek_Hesap":65203
# }

# def menu():
#     print("Bankamatik Uygulaması")
#     print("Bakiye sorgulama")
#     print("Para Çekme")
#     print("Para Yatırma")
#     print("Çıkış")
#     return input("Lütfen yapmak istediğiniz işlemi seçin: ")

# def bakiye_sorgulama(hesap):
#     print(f"/n{hesap['ad']} TL- Hesap No: {hesap['hesapNo']}")
#     print (f"Bakiye: {hesap['ekHesap']} TL")
#     print(F"Ek Hesap Limiti: {hesap['ekHesap']} TL")

# def para_cekme(hesap):
#     miktar= float(input("çekmek istediğiniz tutarı giriniz: "))
#     if miktar <= hesap['bakiye']:
#         hesap['bakiye'] = miktar
#         print(f"{miktar} TL başarıyla çekildi. Güncel bakiye : {hesap['bakiye']} TL ")
#     else:
#         toplam_bakiye = hesap['bakiye'] + hesap['ekhesap']
#         if miktar<= toplam_bakiye:
#             kullan_ek_hesap = input("Hesap bakiyeniz yetersiz. Ek hesabı kullanmak ister misiniz? (E/H): ").lower()
#             if kullan_ek_hesap == "e":
#                 ek_hesap_kullanilan = miktar - hesap['bakiye']
#                 hesap['bakiye'] = 0
#                 hesap['ekHesap'] -= ek_hesap_kullanilan
#                 print(f"{miktar} TL başarıyla çekildi. Güncel ek hesap limiti: {hesap['ekHesap']} TL")
#             else:
#                 print("İşlem iptal edildi. Yetersiz bakiye.")
#         else:
#             print("Yetersiz bakiye. İşlem gerçekleştirilemedi.")


# def para_yatirma(hesap):
#     miktar = float(input("Yatırmak istediğiniz tutarı girin: "))
#     hesap['bakiye'] += miktar
#     print(f"{miktar} TL başarıyla yatırıldı. Güncel bakiye: {hesap['bakiye']} TL")


# def main():
#     print("Bankamatik Uygulamasina Hoşgeldiniz!")
#     while True:
#         secim = menu()
        
#         if secim == "1":
#             bakiye_sorgula(hesap)
#         elif secim == "2":
#             para_cekme(hesap)
#         elif secim == "3":
#             para_yatirma(hesap)
#         elif secim == "4":
#             print("Çıkış yapılıyor. İyi günler dileriz!")
#             break
#         else:
#             print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()