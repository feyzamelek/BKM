
#*BankaHesabi isminde bir sınıf tanımlayınız.
# ** Üretilen her bir nesne "hesapSahibi" isminde biz özelliğe sahip olmalıdır. BankaHesabi("Ad Soyad")
#** Üretilen her bir nesne "bakiye" isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır.
#** Üretilen her bir nesne için "paraYatir" metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp bakiye
#  üzerine ekleyin ve bakiye miktarını geriye döndürün.
#** Üretilen her bir nesne için "paraCek" metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp bakiye
 #  değerinden çıkarıp geriye döndürün.

#hesap = BankaHesabi("Ad Soyad")
#hesap.hesapSahibi => Ad Soyad
#hesap.bakiye => 0.0
# #hesap.paraYatir(1000) => 1000.0
#hesap.paraCek(500) => 500.0

class BankaHesabi:
    def __init__(self, hesapSahibi):
        self.hesapSahibi = hesapSahibi
        self.bakiye = 0.0

    def paraYatir(self,miktar):
        if miktar > 0:
            self.bakiye += miktar
        return self.bakiye
    def para_cek (self, miktar):
        if miktar > 0 and miktar <= self.bakiye:
            self.bakiye = miktar
        return self.bakiye
    
hesap = BankaHesabi("Feyyaz")
print(hesap.hesapSahibi)
print(hesap.bakiye)
print(hesap.paraYatir(8520))
print(hesap.para_cek(950))
