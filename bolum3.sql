-- BÖLÜM 3: SQL SELECT ve WHERE Sorguları
-- Senaryo: Robot Takip Sistemi Veritabanı

-- 1. Tüm aktif robotları listeleme
SELECT * 
FROM robotlar 
WHERE durum = 'Aktif';

-- 2. Belirli bir model ve enerji seviyesindeki robotları getirme
SELECT robot_adi, model, enerji_seviyesi 
FROM robotlar 
WHERE model = 'Model-X' AND enerji_seviyesi > 50;

-- 3. İsmi 'A' harfiyle başlayan veya bataryası kritik seviyede olanlar
SELECT * 
FROM robotlar 
WHERE robot_adi LIKE 'A%' OR enerji_seviyesi < 20;