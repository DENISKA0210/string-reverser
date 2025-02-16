def reverse_string(s: str) -> str:
    """Функція повертає рядок у зворотному порядку"""
    return s[::-1]

if __name__ == "__main__":
    user_input = input("Введіть рядок: ")
    print("Інверсований рядок:", reverse_string(user_input))