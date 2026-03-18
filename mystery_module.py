"""
İkinci dereceden denklem çözücüsü modülü.

Bu modül ax² + bx + c = 0 formundaki ikinci dereceden denklemleri çözer.
"""

import math

# Sabitler - magic number'ları açıkla
QUADRATIC_DISCRIMINANT_COEFFICIENT = 4
DEFAULT_PRECISION = 4
EPSILON_FOR_EQUAL_ROOTS = 1e-10


class QuadraticEquationError(Exception):
    """İkinci dereceden denklem çözme hatası."""

    pass


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
    if coefficient_a == 0:
        raise QuadraticEquationError(
            "a (x² katsayısı) sıfır olamaz, bu ikinci dereceden denklem olmaz"
        )
    if not all(
        isinstance(x, (int, float))
        for x in [coefficient_a, coefficient_b, coefficient_c]
    ):
        raise QuadraticEquationError("Tüm katsayılar sayısal olmalı")


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

        >>> solve_quadratic_equation(1, 2, 1)
        (-1.0, -1.0)

        >>> solve_quadratic_equation(1, 0, 1)
        None
    """
    validate_coefficients(coefficient_a, coefficient_b, coefficient_c)

    # Diskriminantı (Δ = b² - 4ac) hesapla
    discriminant = (
        coefficient_b**2
        - QUADRATIC_DISCRIMINANT_COEFFICIENT * coefficient_a * coefficient_c
    )

    # Gerçek kök olmadığını kontrol et
    if discriminant < 0:
        return None

    # ⚠️ FIX: sqrt() sadece BİR kez hesaplanıyor, daha sonra yeniden kullanılıyor
    sqrt_discriminant = math.sqrt(discriminant)

    # Kök formülü kullan: x = (-b ± √Δ) / 2a
    divisor = 2 * coefficient_a
    first_root = (-coefficient_b + sqrt_discriminant) / divisor
    second_root = (-coefficient_b - sqrt_discriminant) / divisor

    return (first_root, second_root)


def format_solution(roots):
    """
    Çözümü okunaklı şekilde biçimlendir.

    Args:
        roots: Çözüm tuple'ı veya None

    Returns:
        str: Formatlı sonuç metni
    """
    if roots is None:
        return "Gerçek kök yoktur (diskriminant < 0)"

    root1, root2 = roots
    if abs(root1 - root2) < EPSILON_FOR_EQUAL_ROOTS:  # Eşit kökler
        return f"Çift kök: x = {root1:.{DEFAULT_PRECISION}f}"
    else:
        return f"x₁ = {root1:.{DEFAULT_PRECISION}f}, x₂ = {root2:.{DEFAULT_PRECISION}f}"


# Test
if __name__ == "__main__":
    test_cases = [
        (1, -5, 6, "x² - 5x + 6 = 0"),
        (1, 2, 1, "x² + 2x + 1 = 0"),
        (1, 0, 1, "x² + 1 = 0"),
        (2, -4, 2, "2x² - 4x + 2 = 0"),
    ]

    for a, b, c, equation in test_cases:
        try:
            roots = solve_quadratic_equation(a, b, c)
            solution_text = format_solution(roots)
            print(f"✓ {equation}")
            print(f"  → {solution_text}\n")
        except QuadraticEquationError as e:
            print(f"✗ {equation}: {e}\n")
