"""Veri işleme modülü - her fonksiyon tek sorumluluğa sahip."""


def apply_percentage(value, percentage=15):
    """
    Verilen değere yüzde ekle.

    Args:
        value: Temel değer
        percentage: Eklenecek yüzde (varsayılan: 15)

    Returns:
        float: Hesaplanan yeni değer
    """
    return value * (1 + percentage / 100)


def format_currency(amount):
    """
    Tutarı para formatında düzenle.

    Args:
        amount: Tutarın sayısal değeri

    Returns:
        str: Formatlı para stringi
    """
    return f"Total: {amount:.2f}"


def log_results(results, filename="log.txt"):
    """
    Sonuçları dosyaya kaydet.

    Args:
        results: Kaydedilecek sonuçlar listesi
        filename: Hedef dosya adı
    """
    try:
        with open(filename, "a") as f:
            f.write(str(results) + "\n")
    except IOError as e:
        print(f"Dosya yazma hatası: {e}")


def process_data(data, percentage=15):
    """
    Veri listesini işle, yüzde ekle ve sonuçları göster/kaydet.

    Args:
        data: İşlenecek sayısal veriler listesi
        percentage: Uygulanacak yüzde

    Returns:
        list: Hesaplanan değerler listesi
    """
    results = []

    for value in data:
        calculated_value = apply_percentage(value, percentage)
        formatted_text = format_currency(calculated_value)
        print(formatted_text)
        results.append(calculated_value)

    log_results(results)
    return results
