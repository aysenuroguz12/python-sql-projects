import sqlite3

baglanti = sqlite3.connect("harcamalar.db")
baglanti.execute("CREATE TABLE IF NOT EXISTS harcamalar (id INTEGER PRIMARY KEY AUTOINCREMENT, fiyat INTEGER)")


def menu_goster():
    print("\n KİŞİSEL FİNANS TAKİP SİSTEMİ ")
    print("1. Harcama Ekle")
    print("2. Harcamaları Listele")
    print("3. Harcama Sil")
    print("4. Çıkış")
    print("------------------------------")


def harcama_ekle():
    try:
        fiyat = int(input("Ürün fiyatı: "))
        if fiyat < 0:
            print("Fiyat negatif olamaz.")
            return
    except ValueError:
        print("Geçerli bir fiyat girin.")
        return

    baglanti.execute("INSERT INTO harcamalar (fiyat) VALUES (?)", (fiyat,))
    baglanti.commit()
    print("Harcama eklendi.")


def harcamalari_listele():
    cursor = baglanti.cursor()
    cursor.execute("SELECT id, fiyat FROM harcamalar ORDER BY id")
    harcamalar = cursor.fetchall()

    if not harcamalar:
        print("Henüz harcama bulunmuyor.")
        return

    print("\n--- Harcamalar ---")
    toplam = 0
    for harcama_id, fiyat in harcamalar:
        print(f"{harcama_id}. {fiyat} TL")
        toplam += fiyat
    print(f"Toplam: {toplam} TL")


def harcama_sil():
    try:
        harcama_id = int(input("Silinecek harcama ID'si: "))
    except ValueError:
        print("Geçerli bir ID girin.")
        return

    cursor = baglanti.execute("DELETE FROM harcamalar WHERE id = ?", (harcama_id,))
    baglanti.commit()
    if cursor.rowcount:
        print("Harcama silindi.")
    else:
        print("Bu ID ile eşleşen harcama bulunamadı.")


while True:
    menu_goster()
    secim = input("Seçiminiz (1-4): ")

    if secim == "1":
        harcama_ekle()
    elif secim == "2":
        harcamalari_listele()
    elif secim == "3":
        harcama_sil()
    elif secim == "4":
        print("Görüşürüz!")
        break
    else:
        print("Geçersiz seçim.")

baglanti.close()