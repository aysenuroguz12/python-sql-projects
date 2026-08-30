import sqlite3


def baglanti_ac():
    return sqlite3.connect("database.db")


def tablo_olustur():
    baglanti = baglanti_ac()
    baglanti.execute(
        "CREATE TABLE IF NOT EXISTS database "
        "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "kitap_adi TEXT, "
        "yazar TEXT, "
        "kategori TEXT, "
        "fiyat INTEGER, "
        "stok INTEGER)"
    )
    baglanti.commit()
    baglanti.close()


tablo_olustur()


def kitap_ekle():
    kitap_adi = input("Kitap adı: ")
    yazar = input("Yazar: ")
    kategori = input("Kategori: ")
    fiyat = int(input("Fiyat: "))
    stok = int(input("Stok: "))

    baglanti = baglanti_ac()
    cursor = baglanti.cursor()
    cursor.execute(
        "INSERT INTO database (kitap_adi, yazar, kategori, fiyat, stok) "
        "VALUES (?, ?, ?, ?, ?)",
        (kitap_adi, yazar, kategori, fiyat, stok),
    )
    baglanti.commit()
    baglanti.close()


def kitaplari_listele():
    baglanti = baglanti_ac()
    cursor = baglanti.cursor()
    cursor.execute("SELECT * FROM database")
    result = cursor.fetchall()

    if not result:
        print("Henüz kitap bulunmuyor.")
    else:
        for kitap in result:
            print(kitap)

    baglanti.close()
    return result


def silme():
    kitap_id = int(input("Silinecek kitap ID: "))
    baglanti = baglanti_ac()
    cursor = baglanti.cursor()
    cursor.execute("DELETE FROM database WHERE id = ?", (kitap_id,))

    if cursor.rowcount == 0:
        print("Kitap ID bulunmuyor.")
    else:
        print(f"Kitap ID {kitap_id} silindi.")

    baglanti.commit()
    baglanti.close()

def kitap_güncelleme():
    kitap_id = int(input("Güncellenecek kitap ID: "))
    kitap_adi = input("Yeni kitap adı: ")
    yazar = input("Yeni yazar: ")
    kategori = input("Yeni kategori: ")
    fiyat = int(input("Yeni fiyat: "))
    stok = int(input("Yeni stok: "))

    baglanti = baglanti_ac()
    cursor = baglanti.cursor()
    cursor.execute(
        "UPDATE database SET "
        "kitap_adi = ?, "
        "yazar = ?, "
        "kategori = ?, "
        "fiyat = ?, "
        "stok = ? "
        "WHERE id = ?",
        (kitap_adi, yazar, kategori, fiyat, stok, kitap_id),
    )
    baglanti.commit()
    baglanti.close()


def menu():
    while True:
        secim = input(
            "İşlem yapmak istediğiniz numarayı seçiniz:\n"
            "1 → Kitap ekle\n"
            "2 → Kitapları listele\n"
            "3 → Kitap güncelle\n"
            "4 → Kitap sil\n"
            "5 → Programdan çık\n"
            "Seçiminiz: "
        )

        if secim == "1":
            kitap_ekle()
        elif secim == "2":
            kitaplari_listele()
        elif secim == "3":
            kitap_güncelleme()
        elif secim == "4":
            silme()
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim.")


menu()



    