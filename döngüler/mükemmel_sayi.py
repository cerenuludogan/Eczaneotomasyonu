"""Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
 Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)"""

sayi = int(input("bir sayi giriniz:"))
toplam=0
i=1
if i<sayi:
   if sayi %i == 0 :
      toplam=toplam+i
      i+=1
if sayi == toplam :
    print(sayi , "sayi mükemmel sayidir")
else :
    print(sayi , "sayi mükemmel sayi değildir")
