# BÖLÜM 2: Veritabanı ve Tablo Tasarımı Kavramları

## Excel ve İlişkisel Veritabanı Arasındaki Temel Farklar
1. **Veri Bütünlüğü ve İlişkiler:** Excel tabloları bağımsızdır ve veriler arasında güçlü ilişkiler kurmak zordur. İlişkisel veritabanları (RDBMS) ise tabloları birbirine yabancı anahtarlarla (Foreign Key) bağlayarak veri tekrarını önler ve bütünlüğü korur.
2. **Eş Zamanlı Erişim (Concurrency):** Excel dosyaları aynı anda birden fazla kişi tarafından düzenlendiğinde çakışmalar ve veri kayıpları yaşanabilir. Veritabanları ise aynı anda binlerce kullanıcının güvenle işlem yapmasına olanak tanır.
3. **Ölçeklenebilirlik:** Milyonlarca satırlık veride Excel yavaşlar ve kilitlenir; veritabanı sistemleri ise büyük veri setlerini hızlı sorgularla yönetebilir.

## Birincil Anahtarın (Primary Key) Önemi
Primary Key, bir tablodaki her bir satırı benzersiz (unique) olarak tanımlayan sütundur. Asla boş (`NULL`) olamaz ve aynı değerden iki tane bulunamaz. Veritabanında verilerin karışmasını önler, arama işlemlerini hızlandırır ve tablolar arası doğru bağlantı kurulmasını sağlar.