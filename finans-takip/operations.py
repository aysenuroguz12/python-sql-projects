from database import baglanti_olustur

def harcama_ekle(tarih, kategori, tutar, aciklama):
	baglanti = baglanti_olustur()
	cursor = baglanti.cursor()
	cursor.execute(
		"INSERT INTO harcamalar (tarih, kategori, tutar, aciklama) VALUES (?, ?, ?, ?)",
		(tarih, kategori, tutar, aciklama),
	)
	baglanti.commit()
	baglanti.close()

def harcamalari_listele():
	baglanti = baglanti_olustur()
	cursor = baglanti.cursor()
	cursor.execute(
		"SELECT * FROM harcamalar ORDER BY tarih DESC;"
		)
	harcamalar = cursor.fetchall()
	baglanti.close()
	return harcamalar
def silme(id):
	baglanti = baglanti_olustur()
	cursor = baglanti.cursor()
	cursor.execute(
		"DELETE FROM harcamalar WHERE id = ?", (id,)
	)
	baglanti.commit()
	baglanti.close()