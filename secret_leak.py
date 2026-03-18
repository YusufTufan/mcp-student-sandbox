"""
AWS bağlantı modülü - güvenlik ve bağımlılık injection ile.

UYARI: Gizli bilgileri ASLA source code'da hardcode etmeyin!
       Bunun yerine .env dosyasını veya ortam değişkenlerini kullanın.
"""

import os
import logging


class ConnectionError(Exception):
    """Bağlantı kurma hatası."""

    pass


class AWSConnector:
    """AWS hizmetlerine güvenli bağlantı yöneticisi."""

    # Magic numbers için sabitler
    MASK_FILL_CHAR = "*"
    MIN_VISIBLE_CHARS = 0  # Security için hiçbir şey gösterme

    def __init__(self, secret_key=None, logger=None):
        """
        AWS Connector başlat.

        Args:
            secret_key: AWS anahtarı (None ise ortam değişkeninden okur)
            logger: Logging objesi (None ise varsayılan oluşturulur)

        Raises:
            ConnectionError: Gerekli bilgiler yoksa
        """
        self._secret_key = secret_key or os.getenv("AWS_SECRET_KEY")
        self.logger = logger or self._setup_logger()

        if not self._secret_key:
            raise ConnectionError(
                "AWS_SECRET_KEY ortam değişkeni tanımlanmalı. "
                ".env dosyasını kontrol et!"
            )

    @staticmethod
    def _setup_logger():
        """Basit logger oluştur."""
        logging.basicConfig(level=logging.INFO)
        return logging.getLogger(__name__)

    def _mask_key_for_logging(self):
        """
        Güvenlik için anahtarı tamamen maskele.

        FIX: Artık hiçbir karakteri göstermiyoruz (daha güvenli)
        Eski: secret[:10] + "*" * len(secret[10:]) ← VERİ SIZZINTISI!
        Yeni: "*" * len(secret) ← TAM MASKELEME
        """
        if not self._secret_key:
            return "[EMPTY]"

        key_length = len(self._secret_key)
        return self.MASK_FILL_CHAR * key_length

    def connect(self):
        """
        AWS'ye bağlan (güvenli logging ile).

        Returns:
            str: Bağlantı durumunu gösteren mesaj

        Raises:
            ConnectionError: Bağlantı başarısız olursa
        """
        try:
            masked_key = self._mask_key_for_logging()
            key_length = len(self._secret_key) if self._secret_key else 0

            # Log: sadece key uzunluğunu söyle, değerini değil
            self.logger.info(f"AWS'ye bağlanılıyor... (key_length: {key_length})")

            # Gerçek bağlantı kodu burada olurdu
            return f"AWS bağlantısı başarılı"
        except ConnectionError:
            raise
        except ZeroDivisionError as e:
            error_msg = f"AWS bağlantısı başarısız (matematik hatası): {e}"
            self.logger.error(error_msg)
            raise ConnectionError(error_msg)
        except TypeError as e:
            error_msg = f"AWS bağlantısı başarısız (tip hatası): {e}"
            self.logger.error(error_msg)
            raise ConnectionError(error_msg)
        except Exception as e:
            # Unexpected hataları da yakaladık
            error_msg = f"AWS bağlantısı başarısız (bilinmeyen hata)"
            self.logger.error(error_msg, exc_info=e)
            raise ConnectionError(error_msg)


# Test fonksiyonu - güvenli ve bağımsız
if __name__ == "__main__":
    try:
        # Test: Yazılı anahtarla (ortam değişkeni olmadan)
        connector = AWSConnector(secret_key="test_key_12345")
        result = connector.connect()
        print(f"✓ Test başarılı: {result}")
    except ConnectionError as e:
        print(f"✗ Test hatası: {e}")
