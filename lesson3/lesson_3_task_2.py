from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79001234567"),
    Smartphone("Samsung", "Galaxy S23", "+79161234567"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79261234567"),
    Smartphone("Google", "Pixel 7a", "+79371234567"),
    Smartphone("Huawei", "P60 Pro", "+79501234567"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
