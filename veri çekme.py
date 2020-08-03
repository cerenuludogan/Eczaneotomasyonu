import sqlite3


baglanti = sqlite3.connect("veritabani.db")

veriler = baglanti.execute("Select * from kisiler")

for i in veriler:
    print(i[1], i[2])