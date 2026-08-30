# 🐍 Python SQL Projects

Python ve SQL kullanarak gerçekçi veri yönetimi uygulamalarını barındıran bir koleksiyon. SQLite ve PostgreSQL ile veritabanı tasarımı, CRUD operasyonları ve veri analizi örnekleri içerir.

---

## 📋 İçerik Yapısı

```
python-sql-projects/
├── finans-takip/              # Finansal işlem yönetim sistemi
├── kütüphane-takip/           # Kütüphane yönetim ve ödünç takip
├── ürün-stok-takibi/          # Ürün envanter yönetim sistemi
├── database.db                # SQLite veritabanı
├── requirements.txt           # Python bağımlılıkları
└── README.md                  # Bu dosya
```

---

## 🚀 Projeler

### 1️⃣ Finans Takip (`finans-takip/`)
Kişisel veya işletme finansmanı yönetimi için uygulamadır.

**Özellikler:**
- ✅ Gelir ve gider kaydı
- ✅ Kategori bazlı filtreleme
- ✅ Aylık/yıllık rapor
- ✅ Bütçe takibi

**Teknoloji:** Python, SQLite

---

### 2️⃣ Kütüphane Takip (`kütüphane-takip/`)
Kütüphane kaynakları ve üye yönetim sistemi.

**Özellikler:**
- ✅ Kitap katalog ve envanteri
- ✅ Üye kayıt ve yönetim
- ✅ Ödünç ve iade işlemleri
- ✅ Gecikme cezası hesaplama

**Teknoloji:** Python, SQLite

---

### 3️⃣ Ürün Stok Takibi (`ürün-stok-takibi/`)
Perakende veya e-ticaret işletmesi için envanter yönetim sistemi.

**Özellikler:**
- ✅ Ürün ekle/güncelle/sil (CRUD)
- ✅ Stok seviyesi izleme
- ✅ Düşük stok uyarıları
- ✅ Satış raporu analizi

**Teknoloji:** Python, SQLite

---

## 📦 Kurulum

### Sistem Gereksinimleri
- Python 3.8+
- pip paket yöneticisi

### Adım Adım Kurulum

1. **Depoyu klonlayın:**
```bash
git clone https://github.com/aysenuroguz12/python-sql-projects.git
cd python-sql-projects
```

2. **Sanal ortam oluşturun (önerilir):**
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

4. **Proje klasörüne girin ve çalıştırın:**
```bash
cd finans-takip
python main.py
```

---

## 💻 Kullanım

Her proje klasörü kendi `README.md` ve örnek dosyaları içerir. Başlamak için:

```bash
# Proje klasörüne girin
cd [proje-adı]

# İlgili Python dosyasını çalıştırın
python main.py
```

### Örnek Veritabanı Sorgusu
```python
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Veri sorgulama
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()
```

---

## 🛠️ Teknoloji Stack

| Bileşen | Teknoloji |
|---------|-----------|
| **Dil** | Python 3.8+ |
| **Veritabanı** | SQLite 3 |
| **Kütüphaneler** | sqlite3, pandas, sqlalchemy |

---

## 📚 Öğrenme Kaynakları

- [SQLite Resmi Dokümantasyonu](https://www.sqlite.org/docs.html)
- [Python sqlite3 Modülü](https://docs.python.org/3/library/sqlite3.html)
- [SQL Temel Kavramlar](https://www.w3schools.com/sql/)

---

## 🤝 Katkıda Bulunma

Katkılar hoş karşılanır! Lütfen aşağıdakileri yapın:

1. Depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'i push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request açın

### Katkı Yönergeleri
- Kod stil olarak PEP 8'e uyun
- Yeni özellikler için test yazın
- README dosyasını güncelleyin

---

## 📄 Lisans

Bu proje şu anda lisans altında değildir. Kullanım için repo sahibiyle iletişime geçin.

---

## 👤 İletişim

**Geliştirici:** [@aysenuroguz12](https://github.com/aysenuroguz12)  
**E-posta:** Sorularınız için GitHub Issues kullanın

---

## 📝 Notlar

- Veritabanı dosyası (`database.db`) depoyla birlikte getirilir
- Her proje bağımsız olarak kullanılabilir
- Örnek veriler öğrenme amaçlıdır

**Son Güncelleme:** Ağustos 2026

---

⭐ Bu projeyi beğendiyseniz, lütfen yıldız vermeyi unutmayın!
