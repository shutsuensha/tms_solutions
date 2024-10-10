def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char 
    return encrypted_message


def caesar_cipher_decrypt(message, shift):
    return caesar_cipher_encrypt(message, -shift) 


def caesar_cipher(message, shift, action):
    if action == "encrypt":
        return caesar_cipher_encrypt(message, shift)
    elif action == "decrypt":
        return caesar_cipher_decrypt(message, shift)
    else:
        return "Неверное действие!"


message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))
action = input("Выберите действие (encrypt или decrypt): ")

result = caesar_cipher(message, shift, action)
print(f"Результат: {result}")