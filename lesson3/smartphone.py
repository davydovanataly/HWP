class Smartphone:
    def __init__(self, brand: str, model: str, phone_number: str):
        if not (
            isinstance(brand, str)
            and isinstance(model, str)
            and isinstance(phone_number, str)
        ):
            raise TypeError("Аргументы должны быть строками")

        if not (phone_number.startswith("+79") and len(phone_number) == 12
                and phone_number[1:].isdigit()):
            raise ValueError
        ("Неверный формат номера." +
         "Ожидается '+79' и всего 12 цифр например '+79161234567'")

        self.brand = brand
        self.model = model
        self.phone_number = phone_number
