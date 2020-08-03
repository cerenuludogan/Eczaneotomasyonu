#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
a=int(input("birinci sayiyi giriniz: "))
b=int(input("ikinci sayiyi giriniz: "))
c=int(input("üçüncü sayiyi giriniz: "))

if a<b and a<c :
    print("en küçük sayi: ",format(a))

if b<a and b<c :
    print("en küçük sayi:",format(b))

if c<a and  c<b :
    print("en küük sayi:",format(c))

