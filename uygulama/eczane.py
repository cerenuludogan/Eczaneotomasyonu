import sqlite3

while (True):
    kullanıcı_adı = input("Geçerli bir kullanıcı adı giriniz: ")
    ad = "admin"
    sifre = int(input("Sifrenizi giriniz:"))
    giriş_şifresi = 12345
    #eğer kullanıcı adı ve şifre doğruysa break yaz.
    if giriş_şifresi==sifre and kullanıcı_adı==ad:
        break
    else:
        print("Hatalı kullanıcı !")

def listele():

    print("Ürün Listesi:")
    veri = baglanti.execute("Select * from Ilaclar")
    sayac = 1
    for i in veri:
        print(sayac, " ---> ID:", i[0], "Ad:", i[1], "Stok:", i[2], "Kategori:", i[3])
        sayac = sayac + 1

def urun_sil():
    print("Ürün sil")
    deger= int(input("Id degeri giriniz: "))

    cursor.execute("DELETE FROM Ilaclar WHERE IlacId=" + str(deger))
    baglanti.commit()

"""
    for i in veri:
        print("---> ID:", i[0], "Ad:", i[1], "Stok:", i[2], "Kategori:", i[3])
"""

def urun_guncelle():
    print("ürün güncelle")
    deger= int(input("Güncellemek İstediğiniz Id Degerini giriniz: "))


    ad = input("Güncellemek istediğiniz ürünün adını giriniz: ")
    Sayi = int(input("Güncellemek istediğiniz ürünün sayısını giriniz:"))
    alan = input("Güncellemek istediğiniz ürünün kategorisini giriniz:")
    # (str(k_id_son), str(onem_son), str(kural_basligi_son), str(aciklama_son), str(aranacak_icerik_son), str(cozum_son),)
    cursor.execute('''UPDATE Ilaclar SET ilacAdi=? , StokSayisi = ? , IlacKategorisi = ? WHERE IlacId=?''',
                   (str(ad), str(Sayi), str(alan),str(deger),))
    # veri = baglanti.execute("Select * from Ilaclar")
    baglanti.commit()


def urun_ekle():
    print("Ürün ekle")


    ad=input("Eklemek istediğiniz ürünün adını giriniz: ")
    Sayi=int(input("Eklemek istediğiniz ürünün sayısını giriniz:"))
    alan=input("Eklemek istediğiniz ürünün kategorisini giriniz:")
    #(str(k_id_son), str(onem_son), str(kural_basligi_son), str(aciklama_son), str(aranacak_icerik_son), str(cozum_son),)
    cursor.execute('''INSERT INTO Ilaclar (ilacAdi, StokSayisi, IlacKategorisi) VALUES (? , ?, ?)''', (str(ad),str(Sayi), str(alan),))
    #veri = baglanti.execute("Select * from Ilaclar")
    baglanti.commit()

while 1:
    try:
        baglanti = sqlite3.connect("C:\\Users\\Ceren\\deneme.db")
        cursor = baglanti.cursor()
        istek = int(input(""" 
Eczane Stok Yönetim Programına Hoşgeldiniz.
1- Tüm ürünleri listele
2- ID değeri girilen ürünü sil
3- ID değeri girilen ürünü güncelle
4- Ürün ekle
5- Çıkış

Hangi işlemi yapmak istiyorsunuz? Sayı giriniz:  """))

        if istek == 1:
            listele()
        elif istek == 2:
            urun_sil()
        elif istek == 3:
            urun_guncelle()
        elif istek == 4:
            urun_ekle()
        elif istek== 5:
           print("Güle Güle...")
           break

        else:
            print("Hatalı seçim yaptınız.")

        input("Devam etmek için enter a basınız..")
        baglanti.close()
    except Exception as hata:
        print("HATA Oluştu")
