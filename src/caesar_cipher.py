def caesarCipher(s, k):
    k = k % 26
    cipher_text = []
    for char in s:
        if "A" <= char <= "Z":
            shifted = (ord(char) - ord("A") + k) % 26 + ord("A")
            cipher_text.append(chr(shifted))
        elif "a" <= char <= "z":
            shifted = (ord(char) - ord("a") + k) % 26 + ord("a")
            cipher_text.append(chr(shifted))
        else:
            cipher_text.append(char)
    return "".join(cipher_text)
