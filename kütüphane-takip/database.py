import sqlite3
baglanti = sqlite3.connect("database.db")
baglanti.execute(
    "CREATE TABLE IF NOT EXISTS database "
    "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "kitap_adi text,"
    "yazar text,"
    "kategori text,"
    "fiyat INTEGER, "
    "stok INTEGER)"
)
baglanti.commit()
baglanti.close()

def kitap_ekle():
    kitap_adi = input("Kitap adı: ")
    yazar = input("Yazar: ")
    kategori = input("Kategori: ")
    fiyat = int(input("Fiyat: "))
    stok = int(input("Stok: "))

    baglanti = sqlite3.connect("database.db")
    cursor =baglanti.cursor()
    cursor.execute(
        "INSERT INTO database (kitap_adi, yazar, kategori, fiyat, stok) "
        "VALUES (?, ?, ?, ?, ?)",
        (kitap_adi, yazar, kategori, fiyat, stok),
    )
    baglanti.commit()
    baglanti.close()

    def kitaplari_listele():
        baglanti=sqlite3.connect("database.db")
        cursor=baglanti.cursor()
        cursor.execute(
            "SELECT * FROM database"
        )
        if not result:
            print("Henüz kitap bulunmuyor.")
        else:
            for kitap in result:
                print(kitap)
        result=cursor.fetchall()
        baglanti.close()
        return result
    def silme():
        
    