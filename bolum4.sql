-- BÖLÜM 4: GROUP BY ve NULL İşlemleri

-- 1. Her modelin toplam robot sayısı ve ortalama enerji seviyesi
SELECT model, COUNT(*) AS toplam_robot, AVG(enerji_seviyesi) AS ortalama_enerji
FROM robotlar
GROUP BY model;

-- 2. Bakım tarihi girilmemiş (NULL olan) robotları listeleme
SELECT robot_adi, model
FROM robotlar
WHERE son_bakim_tarihi IS NULL;

-- 3. Modollere göre gruplama yapıp sadece ortalama enerjisi 60'tan büyük olanları getirme (HAVING kullanımı)
SELECT model, AVG(enerji_seviyesi) AS ort_enerji
FROM robotlar
GROUP BY model
HAVING AVG(enerji_seviyesi) > 60;