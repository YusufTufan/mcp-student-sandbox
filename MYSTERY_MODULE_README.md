# 📐 Mystery Module - İkinci Dereceden Denklem Çözücüsü

## 📋 İçindekiler

1. [Giriş](#giriş)
2. [Matematiksel Temeller](#matematiksel-temeller)
3. [Kurulum ve Kullanım](#kurulum-ve-kullanım)
4. [API Referansı](#api-referansı)
5. [Örnekler](#örnekler)
6. [Hata Yönetimi](#hata-yönetimi)
7. [Temiz Kod Prensipleri](#temiz-kod-prensipleri)
8. [Test Örnekleri](#test-örnekleri)

---

## 🎯 Giriş

**Dosya Adı:** `mystery_module.py`

Bu modül, **ikinci dereceden denklemleri** (`ax² + bx + c = 0`) çözen profesyonel bir Python kütüphanesidir.

### Temel Özellikler

✅ **Hata Yönetimi** - Geçersiz girdileri yakalar
✅ **Anlaşılır İsimler** - `fn_x()` değil, `solve_quadratic_equation()`
✅ **Dokumentasyon** - Kapsamlı docstring'ler ve örnekler
✅ **Constants** - Magic number'lar yerine anlamlı sabitler
✅ **Type Kontrol** - Girdilerin sayısal olduğunu doğrular

---

## 📐 Matematiksel Temeller

### İkinci Dereceden Denklem

Standart formda: **ax² + bx + c = 0**

Burada:
- **a** = x² katsayısı (sıfır olamaz!)
- **b** = x katsayısı
- **c** = Sabit terim

### Diskriminant (Δ)

Çözümün türünü belirler:

```
Δ = b² - 4ac
```

| Δ Değeri | Sonuç | Kökler |
|----------|-------|--------|
| Δ > 0 | İki farklı gerçek kök | x₁ ≠ x₂ |
| Δ = 0 | Tek (çift) gerçek kök | x₁ = x₂ |
| Δ < 0 | Gerçek kök yok | Karmaşık kökler |

### Kök Formülü

```
x = (-b ± √Δ) / 2a

x₁ = (-b + √Δ) / 2a
x₂ = (-b - √Δ) / 2a
```

---

## 🚀 Kurulum ve Kullanım

### Basit Kullanım

```python
from mystery_module import solve_quadratic_equation

# x² - 5x + 6 = 0 denklemini çöz
kökler = solve_quadratic_equation(a=1, b=-5, c=6)
print(kökler)  # (3.0, 2.0)
```

### Modülü Çalıştırma

```bash
python mystery_module.py
```

**Çıktı:**
```
✓ x² - 5x + 6 = 0
  → x₁ = 3.0000, x₂ = 2.0000

✓ x² + 2x + 1 = 0
  → Çift kök: x = -1.0000

✓ x² + 1 = 0
  → Gerçek kök yoktur (diskriminant < 0)

✓ 2x² - 4x + 2 = 0
  → Çift kök: x = 1.0000
```

---

## 🔌 API Referansı

### 1. `validate_coefficients()`

Katsayıların geçerli olduğunu doğrular.

```python
def validate_coefficients(coefficient_a, coefficient_b, coefficient_c):
    """
    Denklem katsayılarının geçerliliğini kontrol et.

    Args:
        coefficient_a: x² katsayısı (sıfır olmamalı)
        coefficient_b: x katsayısı
        coefficient_c: Sabit terim

    Raises:
        QuadraticEquationError: Katsayılar geçersizse
    """
```

**Kontroller:**
- ❌ `a == 0` → Hata (denklem ikinci dereceden değil)
- ❌ Sayısal olmayan değerler → Hata
- ✅ Geçerli katsayılar → Hiçbir şey

---

### 2. `solve_quadratic_equation()`

Ana fonksiyon - denklemi çözer.

```python
def solve_quadratic_equation(coefficient_a, coefficient_b, coefficient_c):
    """
    İkinci dereceden denklemi çöz: ax² + bx + c = 0

    Args:
        coefficient_a: x² katsayısı
        coefficient_b: x katsayısı
        coefficient_c: Sabit terim

    Returns:
        tuple: (x1, x2) gerçek kökleri veya None (gerçek kök yoksa)

    Raises:
        QuadraticEquationError: Geçersiz katsayılarsa
    """
```

**Döndürülen Değerler:**
- `(float, float)` - İki gerçek kök
- `None` - Gerçek kök yok (karmaşık kökler)

---

### 3. `format_solution()`

Çözümü okunaklı metne dönüştürür.

```python
def format_solution(roots):
    """
    Çözümü okunaklı şekilde biçimlendir.

    Args:
        roots: Çözüm tuple'ı veya None

    Returns:
        str: Formatlı sonuç metni
    """
```

**Örnekler:**
```python
format_solution((3.0, 2.0))      # "x₁ = 3.0000, x₂ = 2.0000"
format_solution((-1.0, -1.0))    # "Çift kök: x = -1.0000"
format_solution(None)              # "Gerçek kök yoktur (diskriminant < 0)"
```

---

### 4. `QuadraticEquationError`

Özel hata sınıfı.

```python
class QuadraticEquationError(Exception):
    """İkinci dereceden denklem çözme hatası."""
    pass
```

---

## 💡 Örnekler

### Örnek 1: Klasik Denklem

**Problem:** x² - 5x + 6 = 0

```python
from mystery_module import solve_quadratic_equation, format_solution

roots = solve_quadratic_equation(1, -5, 6)
print(format_solution(roots))
# Çıktı: x₁ = 3.0000, x₂ = 2.0000
```

**Matematiksel Doğrulama:**
- x₁ = 3: 3² - 5(3) + 6 = 9 - 15 + 6 = 0 ✓
- x₂ = 2: 2² - 5(2) + 6 = 4 - 10 + 6 = 0 ✓

---

### Örnek 2: Çift Kök (Δ = 0)

**Problem:** x² + 2x + 1 = 0

```python
roots = solve_quadratic_equation(1, 2, 1)
print(format_solution(roots))
# Çıktı: Çift kök: x = -1.0000
```

**Matematiksel Doğrulama:**
- Diskriminant: Δ = 2² - 4(1)(1) = 4 - 4 = 0
- Tek kök: x = -2 / 2 = -1

---

### Örnek 3: Gerçek Kök Yok (Δ < 0)

**Problem:** x² + 1 = 0

```python
roots = solve_quadratic_equation(1, 0, 1)
print(format_solution(roots))
# Çıktı: Gerçek kök yoktur (diskriminant < 0)
```

**Matematiksel Doğrulama:**
- Diskriminant: Δ = 0² - 4(1)(1) = -4 < 0
- Sonuç: Karmaşık kökler (±i)

---

### Örnek 4: Hata Durumları

```python
from mystery_module import solve_quadratic_equation, QuadraticEquationError

# ❌ a = 0 (Geçersiz)
try:
    solve_quadratic_equation(0, 2, 1)
except QuadraticEquationError as e:
    print(f"Hata: {e}")
    # Çıktı: a (x² katsayısı) sıfır olamaz, bu ikinci dereceden denklem olmaz

# ❌ String değer (Geçersiz)
try:
    solve_quadratic_equation("1", 2, 1)
except QuadraticEquationError as e:
    print(f"Hata: {e}")
    # Çıktı: Tüm katsayılar sayısal olmalı
```

---

## 🛡️ Hata Yönetimi

### `QuadraticEquationError`

Tüm hatalar bu özel exception ile işlenir:

```python
try:
    roots = solve_quadratic_equation(0, 5, 3)
except QuadraticEquationError as e:
    print(f"Denklem çözme hatası: {e}")
    # Çıktı: Denklem çözme hatası: a (x² katsayısı) sıfır olamaz...
```

### Hata Türleri

| Hata Durumu | Hata Mesajı |
|-------------|-------------|
| a = 0 | `a (x² katsayısı) sıfır olamaz...` |
| Sayısal olmayan değer | `Tüm katsayılar sayısal olmalı` |

---

## ✨ Temiz Kod Prensipleri

Bu modül şu temiz kod prensiplerini uygular:

### 1. **Anlaşılır İsimler** (Meaningful Names)

❌ **Kötü:**
```python
def fn_x(a, b, c):
    d = b**2 - 4*a*c
    ...
```

✅ **İyi:**
```python
def solve_quadratic_equation(coefficient_a, coefficient_b, coefficient_c):
    discriminant = coefficient_b**2 - 4 * coefficient_a * coefficient_c
    ...
```

### 2. **Bağımlılıklar (Magic Numbers)**

❌ **Kötü:**
```python
discriminant = b**2 - 4*a*c  # 4 nereden geldi?
```

✅ **İyi:**
```python
QUADRATIC_DISCRIMINANT_COEFFICIENT = 4
discriminant = b**2 - QUADRATIC_DISCRIMINANT_COEFFICIENT*a*c
```

### 3. **Hata Yönetimi** (Error Handling)

❌ **Kötü:**
```python
def average_ratios(numbers):
    total = 100 / numbers[0]  # ZeroDivisionError!
```

✅ **İyi:**
```python
def validate_coefficients(...):
    if coefficient_a == 0:
        raise QuadraticEquationError("a sıfır olamaz...")
```

### 4. **Kapsamlı Dokümantasyon** (Documentation)

```python
def solve_quadratic_equation(coefficient_a, coefficient_b, coefficient_c):
    """
    İkinci dereceden denklemi çöz: ax² + bx + c = 0

    Denklemin çözümü diskriminantın değerine göre belirlenir:
    - Δ > 0: İki farklı gerçek kök
    - Δ = 0: Tek (çift) gerçek kök
    - Δ < 0: Gerçek kök yok (karmaşık kökler)

    Args:
        coefficient_a: x² katsayısı
        coefficient_b: x katsayısı
        coefficient_c: Sabit terim

    Returns:
        tuple: (x1, x2) gerçek kökleri veya None (gerçek kök yoksa)

    Raises:
        QuadraticEquationError: Geçersiz katsayılarsa

    Example:
        >>> solve_quadratic_equation(1, -5, 6)
        (3.0, 2.0)
    """
```

### 5. **Tekrar Etmeyen Kod (DRY)**

```python
# ⚠️ FIX: sqrt() sadece BİR kez hesaplanıyor, daha sonra yeniden kullanılıyor
sqrt_discriminant = math.sqrt(discriminant)
first_root = (-coefficient_b + sqrt_discriminant) / divisor
second_root = (-coefficient_b - sqrt_discriminant) / divisor
```

### 6. **Tek Sorumluluk** (Single Responsibility)

Modüldeki her fonksiyonun tek bir sorumluluğu var:
- `validate_coefficients()` → Doğrulama
- `solve_quadratic_equation()` → Çözme
- `format_solution()` → Biçimlendirme

---

## 🧪 Test Örnekleri

### Otomatik Test Çalıştırma

```bash
python mystery_module.py
```

### Test Durumları

| Test | Denklem | Katkı | Beklenen Sonuç |
|------|---------|-------|-----------------|
| 1 | x² - 5x + 6 = 0 | (1, -5, 6) | (3.0, 2.0) |
| 2 | x² + 2x + 1 = 0 | (1, 2, 1) | (-1.0, -1.0) |
| 3 | x² + 1 = 0 | (1, 0, 1) | None |
| 4 | 2x² - 4x + 2 = 0 | (2, -4, 2) | (1.0, 1.0) |

### Manual Test

```python
# Test 1: Normal durum
assert solve_quadratic_equation(1, -5, 6) == (3.0, 2.0)

# Test 2: Çift kök
roots = solve_quadratic_equation(1, 2, 1)
assert roots[0] == roots[1]  # Kökler eşit

# Test 3: Gerçek kök yok
assert solve_quadratic_equation(1, 0, 1) is None

# Test 4: Hata durumu
try:
    solve_quadratic_equation(0, 2, 1)
    assert False, "Hata olması gerekti"
except QuadraticEquationError:
    pass  # Beklenen hata
```

---

## 📦 İçe Aktarma (Import)

### Seçenek 1: Tüm Modülü İçe Aktar

```python
import mystery_module

result = mystery_module.solve_quadratic_equation(1, -5, 6)
```

### Seçenek 2: Spesifik İşlevleri İçe Aktar

```python
from mystery_module import solve_quadratic_equation, format_solution, QuadraticEquationError

try:
    roots = solve_quadratic_equation(1, -5, 6)
    print(format_solution(roots))
except QuadraticEquationError as e:
    print(f"Hata: {e}")
```

---

## 📊 Constants Referansı

```python
# Sabitler - magic number'ları açıkla
QUADRATIC_DISCRIMINANT_COEFFICIENT = 4      # Δ formülünde kullanılan 4
DEFAULT_PRECISION = 4                        # format_solution() hassasiyeti
EPSILON_FOR_EQUAL_ROOTS = 1e-10             # Floating-point karşılaştırması
```

---

## 🎓 Temiz Kod Dersleri

Bu modül şunları öğretir:

1. **Adlandırma Önemlidir** - `fn_x()` yerine `solve_quadratic_equation()`
2. **Doğrulama İlk Gelir** - `validate_coefficients()` hata yakalamayı önler
3. **Dokumentasyon Hayat Kurtarır** - Docstring'ler gelecekteki geliştirmeleri kolaylaştırır
4. **Constants Magic Number'ları Değiştirir** - "Neden 4?" sorusu ortaya kalmaz
5. **Hata Yönetimi Sağlamdır** - `try-except` blokları yerinde kullanılır

---

## 🔗 İlgili Dosyalar

- `spaghetti_logic.py` - Modülerlik örnekleri
- `failing_calculator.py` - Hata yönetimi örnekleri
- `secret_leak.py` - Güvenlik en iyi uygulamaları

---

## 📝 Versiyon Tarihi

| Versiyon | Tarih | Değişiklikler |
|----------|-------|---------------|
| 1.0 | 2026-03-19 | ✨ Başlangıç versionu |

---

## 📞 Destek

Bu modülü kullanırken sorun yaşarsanız:

1. **Dokümantasyon** - Bu README'yi kontrol edin
2. **Docstring'ler** - Python'da `help(solve_quadratic_equation)` yazın
3. **Test Örnekleri** - `python mystery_module.py` çalıştırın

---

**Temiz kod, açık amaç, net sonuç! 🎯**
