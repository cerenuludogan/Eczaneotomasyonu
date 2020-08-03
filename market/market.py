import sqlite3

con = sqlite3.connect("market.db")

cursor = con.cursor()


print(""" *******************************

Market Stok Yönetim Programına Hoşgeldiniz!

1)Ürün Ekle
2)Ürün Sil
3)Markaya Göre Stok Sorgula
4)Toplam Stok Sorgula
5)Satış Yap
6)İade Al
7)Günlük Müşteri Sayısı 
8)Günlük Alınan İade
9)Günlük Ciro
10)Programdan Çıkış
**********************************
                
""")
