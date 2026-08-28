import sqlite3
baglanti = sqlite3.connect("finans.db")

baglanti.execute("""
CREATE TABLE IF NOT EXISTS harcamalar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tarih TEXT NOT NULL,
    kategori TEXT NOT NULL,
    tutar REAL NOT NULL,
    aciklama TEXT
)
""")

baglanti.commit()
print("çalıştı")
baglanti.close()