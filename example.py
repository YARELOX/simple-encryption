from src.encryption import encrypt, decrypt
key = '10:20:30:40:50'
text = 'Hello! This is example of my encryption.'
print(text, len(text))
encryptedText = encrypt(key, text)
print(encryptedText, len(encryptedText))
decryptedText = decrypt(key, encryptedText)
print(decryptedText, len(decryptedText))