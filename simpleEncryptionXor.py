def xor_encrypt_decrypt(data, key):
    data_bytes = data.encode()  
    key_bytes = key.encode()  

    if len(key_bytes) < len(data_bytes):
        key_bytes = (key_bytes * (len(data_bytes) // len(key_bytes) + 1))[:len(data_bytes)]

    encrypted = bytearray()
    for i in range(len(data_bytes)):
        encrypted.append(data_bytes[i] ^ key_bytes[i])
    
    return bytes(encrypted)

plain_text = "Hello, World!"
key = "mysecretkey"

cipher_text = xor_encrypt_decrypt(plain_text, key)
print("Encrypted:",cipher_text)

decrypted_text = xor_encrypt_decrypt(cipher_text.decode(), key)
print("Decrypted:", decrypted_text)
