print("""*******************
HESAP MAKINESI PROGRAMI
       Islemler:
    1)Toplama islemi
    2)Cikarma islemi
    3)Carpma islemi
    4)Bolme ıslemi
**********************************""")
a = int(input("Birinci sayi: "))
b = int(input("Ikinci sayi: "))

islem = input("islem giriniz: ")

if islem==1 :
    print("{} ile {} in toplamı {} dır".format(a,b,a+b))

if islem==2 :
    print("{} ile {} in çıktısı {} dır".format(a,b,a-b))

if islem==3 :
    print("{} ile {} in çarpımı {} dır".format(a,b,a*b))

if islem==4 :
    print("{} ile {} in bölümü {} dır".format(a,b,a/b))