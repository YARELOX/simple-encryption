def parseKey(key):
    parsedKey = [int(i) for i in key.split(':')]
    return parsedKey

def encrypt(key, text):
    encryptedText = ''
    parsedKey = parseKey(key)
    i = 1
    for char in text:
        if i > len(parsedKey):
            i = 1
        additive = 0
        currentKeyElement = parsedKey[i - 1]
        if currentKeyElement % i == 0:
            additive = currentKeyElement
        else:
            additive = i
        encryptedText = encryptedText + chr(ord(char) + additive)
        i += 1
    return encryptedText

def decrypt(key, text):
    return encrypt(':'.join([str(-i) for i in parseKey(key)]), text)