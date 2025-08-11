def month_to_season(month):
    """Возвращает сезон по номеру месяца (1..12)."""
    try:
        m = int(month)
    except (TypeError, ValueError):
        raise ValueError("Номер месяца должен быть целым числом от 1 до 12")
    if not 1 <= m <= 12:
        raise ValueError("Номер месяца должен быть в диапазоне 1..12")
    if m in (12, 1, 2):
        return "Зима"
    if 3 <= m <= 5:
        return "Весна"
    if 6 <= m <= 8:
        return "Лето"
    return "Осень"


print(month_to_season(2))
