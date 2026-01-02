# Collatz Dizisine Dayalı Şifreleme (Collatz Şifreleme)

## Genel Bakış

Bu program, Collatz varsayımına dayalı özel bir şifreleme algoritması uygular. Pozitif bir tam sayıyı girdi olarak alır ve Collatz dizilerini kullanan bir dizi matematiksel dönüşüm aracılığıyla ikili bir şifreli dize oluşturur.

## Algoritma Açıklaması

### Collatz Dizisi Nedir?

Collatz varsayımı, herhangi bir pozitif tam sayı için aşağıdakini belirtir:
- Sayı çift ise 2'ye böl
- Sayı tek ise 3 ile çarp ve 1 ekle
- 1'e ulaşana kadar tekrarla

### Şifreleme Süreci

1. **Girdi Doğrulaması**: Program sadece en az 4 basamaklı pozitif tam sayıları kabul eder
2. **Dizi Oluşturma**: 
   - Girdi numarasından bir Collatz dizisi oluşturur
   - Girdi numarası + 1'den ikinci bir Collatz dizisi oluşturur
   - Her iki dizi de maksimum 16 elemana sınırlıdır
   - Bir sayı 2'nin kuvveti ise dizi erken durur (sonsuz benzeri davranışı önlemek için optimizasyon)
3. **Dizi Birleştirme**: Her iki diziyi tek bir listeye birleştirir
4. **Şifreleme**:
   - Birleştirilmiş dizideki her sayı için rakamlarının toplamını hesaplar
   - Rakamlar toplamı çift ise → `1` ile değiştirir
   - Rakamlar toplamı tek ise → `0` ile değiştirir
5. **Çıktı**: İkili dizgiyi (şifreli sonuç) döndürür

## Fonksiyonlar

### `collatz_sequence(n, liste)`

Verilen bir sayı için Collatz dizisini oluşturur.

**Parametreler:**
- `n` (int): Collatz dizisinin başlangıç numarası
- `liste` (list): Dizi elemanlarını depolamak için bir liste

**Döndürür:**
- `liste` (list): Oluşturulan Collatz dizisi (maksimum 16 eleman)

**Davranış:**
- `n` 2'nin kuvveti ise işlemden önce `n`'i 1 ile artırır
- `n` 1'e ulaştığında veya liste 16 elemana ulaştığında durur
- Çift sayılardaki 2'nin kuvvetlerini eklemeyi atlar

### `cryption_process(sayi)`

Tam şifreleme sürecini gerçekleştirir.

**Parametreler:**
- `sayi` (int): En az 4 basamaklı pozitif bir tam sayı

**Döndürür:**
- `sonuc` (str): Şifreli sonucu temsil eden bir ikili dize

**İşlem:**
1. `sayi` ve `sayi+1` için Collatz dizilerini oluşturur
2. Her iki diziyi birleştirir
3. Her elemanı rakamlar toplamının paritesine dönüştürür (tek için 0, çift için 1)
4. Sonucu 0'lar ve 1'ler dizisi olarak döndürür

## Girdi Gereksinimleri

- **Tür**: Pozitif tam sayı
- **Minimum Basamak**: 4 basamak (aralık: 1000 ve üzeri)
- **Doğrulama**: Program şunları reddeder:
  - Sayısal olmayan girdiler
  - Negatif sayılar
  - 4'ten az basamağa sahip sayılar

## Kullanım Örneği

```python
# Örnek girdi
Bir sayı girin: 1234

# Örnek çıktı (ikili şifreli dize)
# örn: 1010101110010101
```

## Global Değişkenler

- `liste` (list): Girdi numarasının Collatz dizisini depolar
- `liste2` (list): Girdi numarası + 1'in Collatz dizisini depolar

Bu listeler her şifreleme işleminden sonra temizlenir.

## Program Akışı

```
Başla
  ↓
Kullanıcı Girdi Doğrulaması
  ├─ Sayısal olup olmadığını kontrol et
  ├─ Pozitif olup olmadığını kontrol et
  ├─ En az 4 basamağa sahip olup olmadığını kontrol et
  ↓
Collatz Dizileri Oluştur
  ├─ Dizi 1: n'den
  ├─ Dizi 2: n+1'den
  ↓
Dizileri Birleştir
  ↓
İkili'ye Dönüştür (rakamlar toplamı paritesi)
  ↓
Şifreli Diziyi Çıkart
  ↓
Listeleri Temizle & Tekrarla
```

## Notlar

- Program sonsuz bir döngü içinde çalışır ve yeniden başlatmadan birden fazla şifrelemeye izin verir
- Her şifreleme veri kontaminasyonunu önlemek için listeleri temizler
- Algoritma, 2'nin kuvvetlerinde Collatz dizilerini durdurmak için bir optimizasyon kullanır
- Maksimum dizi uzunluğu dizi başına 16 elementtir (bu nedenle birleştirdikten sonra maksimum 32 eleman)

## Güvenlik Uyarısı

Bu, bir matematiksel kavramın eğitim amaçlı bir uygulamasıdır ve **gerçek şifreleme amaçları için kullanılmamalıdır**. Güvenli şifreleme için gerekli özellikleri yoksundur:
- Geri döndürülemezlik
- İstatistiksel rastgelelik
- Bilinen saldırılara karşı direnç
- Uygun anahtar yönetimi
