

# BÖLÜM 1: Python Algoritmaları ve Takip
# 1. Soru: Sayı Serisi Analizi
baslangic = 1
bitis = 50
tek_toplam = 0
cift_toplam = 0

for sayi in range(baslangic, bitis + 1):
    if sayi % 2 == 0:
        cift_toplam += sayi
    else:
        tek_toplam += sayi

print(f"Tek sayıların toplamı: {tek_toplam}")
print(f"Çift sayıların toplamı: {cift_toplam}")

# 2. Soru: En Uzun Seriyi Bulma (Collatz Örneği)
def en_uzun_seriyi_bul(n):
    adimlar = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        adimlar.append(n)
    return adimlar

baslangic_sayisi = 12
sonuc_serisi = en_uzun_seriyi_bul(baslangic_sayisi)
print(f"{baslangic_sayisi} için üretilen seri: {sonuc_serisi}")
print(f"Adım sayısı: {len(sonuc_serisi)}")

# 3. Soru: Sözlük (Dictionary) Kullanarak Veri Gruplama
ogrenciler = [
    {"isim": "Ahmet", "not": 85},
    {"isim": "Ayşe", "not": 90},
    {"isim": "Mehmet", "not": 70},
    {"isim": "Fatma", "not": 95}
]

toplam_not = sum(ogr["not"] for ogr in ogrenciler)
ortalama = toplam_not / len(ogrenciler)
print(f"Öğrenci Not Ortalaması: {ortalama}")