"""Veri işleme modülü - her fonksiyon tek sorumluluğa sahip."""

# Magic numbers'ları tanımla
DEFAULT_PERCENTAGE = 15
PERCENTAGE_DIVISOR = 100
CURRENCY_PRECISION = 2


def apply_percentage(value, percentage=DEFAULT_PERCENTAGE):
    """
    Verilen değere yüzde ekle.

    Args:
        value: Temel değer
        percentage: Eklenecek yüzde (varsayılan: 15)

    Returns:
        float: Hesaplanan yeni değer
    """
    return value * (1 + percentage / PERCENTAGE_DIVISOR)


def format_currency(amount):
    """
    Tutarı para formatında düzenle.

    Args:
        amount: Tutarın sayısal değeri

    Returns:
        str: Formatlı para stringi
    """
    return f"Total: {amount:.{CURRENCY_PRECISION}f}"


def log_results(results, filename="log.txt"):
    """
    Sonuçları dosyaya kaydet (TOCTOU güvenliğıne uygun).

    Args:
        results: Kaydedilecek sonuçlar listesi
        filename: Hedef dosya adı

    Raises:
        OSError: Dosya yazma hatası
    """
    if not results:
        return  # Boş liste, yazma gerek yok

    try:
        # TOCTOU fix: Check ve write'ı atomic tutmaya çalış
        # Append mode zaten dosya yoksa create eder
        with open(filename, "a", encoding="utf-8") as f:
            f.write(str(results) + "\n")
    except OSError as e:
        print(f"Dosya yazma hatası: {e}", flush=True)
        raise


def process_data(data, percentage=DEFAULT_PERCENTAGE, show_output=False):
    """
    Veri listesini işle, yüzde ekle ve sonuçları döndür.

    FIX - HOT PATH OPTIMIZASYONU:
    - Print'ler loop dışında taşındı (I/O overhead azaldı)
    - Formatting sadece show_output=True ise yapılıyor
    - Sonuçlar buffered şekilde döndürülüyor

    Args:
        data: İşlenecek sayısal veriler listesi
        percentage: Uygulanacak yüzde
        show_output: Sonuçları ekrana yazdırma (default: False)

    Returns:
        list: Hesaplanan değerler listesi
    """
    results = []

    # HOT PATH: sadece hesaplama (I/O yok!)
    for value in data:
        calculated_value = apply_percentage(value, percentage)
        results.append(calculated_value)

    # Output işleri loop dışında yapılıyor (batched I/O)
    if show_output:
        formatted_results = [format_currency(val) for val in results]
        for formatted_text in formatted_results:
            print(formatted_text)

    # Sonuçları dosyaya kaydet
    log_results(results)

    return results
