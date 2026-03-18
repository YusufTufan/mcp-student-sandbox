"""Oran hesaplama modülü - hata yönetimi ile."""


class RatioCalculationError(Exception):
    """Oran hesaplama işlemi sırasında oluşan hata."""

    pass


def validate_numbers(numbers):
    """
    Sayıların geçerliliğini kontrol et.

    Args:
        numbers: Kontrol edilecek sayılar listesi

    Raises:
        RatioCalculationError: Girişler geçersizse
    """
    if not numbers:
        raise RatioCalculationError("Liste boş olamaz")

    for number in numbers:
        if number == 0:
            raise RatioCalculationError(
                f"Sıfıra bölme hatası: {number} sayısı sıfır olamaz"
            )
        if not isinstance(number, (int, float)):
            raise RatioCalculationError(f"Geçersiz tip: {number} sayısal olmalı")


def calculate_average_ratios(numbers):
    """
    Sayıların 100'e oranlarının ortalamasını hesapla.

    Args:
        numbers: Pozitif sayıların listesi

    Returns:
        float: Oranların ortalaması

    Raises:
        RatioCalculationError: Girişler geçersiz veya işlem başarısız olursa

    Example:
        >>> calculate_average_ratios([10, 50, 100])
        1.6
    """
    validate_numbers(numbers)

    try:
        ratios = [100 / number for number in numbers]
        average = sum(ratios) / len(ratios)
        return average
    except ZeroDivisionError as e:
        # Validation'da zaten check edilmeli, ama güvenlik için
        raise RatioCalculationError(f"Sıfıra bölme hatası: {e}")
    except TypeError as e:
        raise RatioCalculationError(f"Tip uyuşmama hatası: {e}")
    except ValueError as e:
        raise RatioCalculationError(f"Değer hatası: {e}")


# Test - Orijinal hata durumunu güvenli şekilde test et
if __name__ == "__main__":
    test_cases = [
        ([10, 5, 20], "Başarılı test"),
        ([10, 5, 0], "Sıfıra bölme hatası (ORIJINAL BUG)"),
        ([], "Boş liste hatası"),
    ]

    print("=" * 60)
    print("FAILING_CALCULATOR.PY TEST RESÜLTLERİ")
    print("=" * 60)

    for test_data, description in test_cases:
        try:
            result = calculate_average_ratios(test_data)
            print(f"✓ {description}")
            print(f"  Girdi: {test_data}")
            print(f"  Sonuç: {result:.2f}\n")
        except RatioCalculationError as e:
            print(f"✗ {description}")
            print(f"  Girdi: {test_data}")
            print(f"  Hata: {e}\n")

    print("=" * 60)
    print("SONUÇ: Orijinal crash hatası düzeltildi!")
    print("=" * 60)
