import re
def check_phone(phone):
    pattern = r'^\+7-\d{3}-\d{3}-\d{2}-\d{2}$'
    
    if re.match(pattern, phone):
        return True
    else:
        return False

phone_number = input("Введите номер телефона в формате +7-999-123-45-67: ")

if check_phone(phone_number):
    print("✓ Номер телефона соответствует формату")
else:
    print("✗ Номер телефона НЕ соответствует формату")