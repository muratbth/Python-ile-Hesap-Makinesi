import math
import sys
class HesapMakinesi:
    def __init__(self):
        self.hafiza = 0
    
    def toplama(self, a, b):
        try:
            sonuc = a + b
            self.hafiza += sonuc
            return sonuc
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def cikarma(self, a, b):
        try:
            sonuc = a - b
            self.hafiza += sonuc
            return sonuc
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def carpma(self, a, b):
        try:
            sonuc = a * b
            self.hafiza += sonuc
            return sonuc
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def bolme(self, a, b):
        try:
            if b != 0:
                sonuc = a / b
                self.hafiza += sonuc
                return sonuc
            else:
                return "Hata: Bölme işlemi için bölen sıfır olamaz!"
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def karekok(self, a):
        try:
            if a > 0:
                sonuc = math.sqrt(a)
                self.hafiza += sonuc
                return sonuc
            else:
                return "Hata: Negatif bir sayının yada sıfırın karekökü alınamaz!"
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def kok_alma(self, a, b):
        try:
            if a > 0:
                sonuc = a ** (1/b)
                self.hafiza += sonuc
                return sonuc
            else:
                return "Hata: Negatif bir sayının yada sıfırın kökü alınamaz!"
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def yuzde_hesapla(self, a, b):
        try:
            sonuc = (a * b) / 100
            self.hafiza += sonuc
            return sonuc
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def grand_total(self):
        return self.hafiza
    
    def sifirla(self):
        self.hafiza = 0
        print("Hafıza sıfırlandı.")
    
    def cikis(self):
        print("Programdan çıkılıyor...")
        sys.exit()
    
    def islem_sec(self):
        while True:
            print("""
1: Toplama
2: Çıkarma
3: Çarpma
4: Bölme
5: Karekök Alma
6: Kök Alma
7: Yüzde Hesaplama
8: Grand total
9: Hafızayı Sıfırla
0: Çıkış
""")
            
            secim = input("Yapmak istediğiniz işlemi seçin: ")
            
            if secim == "1":
                a = float(input("Birinci sayıyı girin: "))
                b = float(input("İkinci sayıyı girin: "))
                print("Sonuç: ", self.toplama(a, b))
            elif secim == "2":
                a = float(input("Birinci sayıyı girin: "))
                b = float(input("İkinci sayıyı girin: "))
                print("Sonuç: ", self.cikarma(a, b))
            elif secim == "3":
                a = float(input("Birinci sayıyı girin: "))
                b = float(input("İkinci sayıyı girin: "))
                print("Sonuç: ", self.carpma(a, b))
            elif secim == "4":
                a = float(input("Bölünecek sayıyı girin: "))
                b = float(input("Böleni girin: "))
                print("Sonuç: ", self.bolme(a, b))
            elif secim == "5":
                a = float(input("Karekökünü almak istediğiniz sayıyı girin: "))
                print("Sonuç: ", self.karekok(a))
            elif secim == "6":
                a = float(input("Kökünü almak istediğiniz sayıyı girin: "))
                b = float(input("Kökün derecesini girin: "))
                print("Sonuç: ", self.kok_alma(a, b))
            elif secim == "7":
                a = float(input("Yüzdesini hesaplamak istediğiniz sayıyı girin: "))
                b = float(input("Yüzde değerini girin: "))
                print("Sonuç: ", self.yuzde_hesapla(a, b))
            elif secim == "8":
                print("Hafızadaki Toplam Sonuç: ", self.grand_total())
            elif secim == "9":
                self.sifirla()
            elif secim == "0":
                self.cikis()
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    hesap_makinesi = HesapMakinesi()
    hesap_makinesi.islem_sec()
