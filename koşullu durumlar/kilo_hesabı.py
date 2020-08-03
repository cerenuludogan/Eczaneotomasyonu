#Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 #Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 #BKİ 18.5'un altındaysa -------> Zayıf

# BKİ 18.5 ile 25 arasındaysa ------> Normal

 #BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 #BKİ 30'un üstündeyse -------------> Obez

boy= float(input("boyunuzu giriniz: "))
kilo= float(input("kilonuzu giriniz: "))

bki=(kilo/(boy*boy))
if bki<18.5 :
    print("zayıf")

if 18.5 < bki < 25:
    print("normal")

if 25 < bki < 30:
    print("fazla kilolu")

if bki > 30:
    print("obez")
