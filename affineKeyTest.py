import affineCipher
import cryptoMath

message = 'Make things as simple as possible, but not simpler.'
for keyA in range(2, 100):
    key = keyA * len(affineCipher.SYMBOLS) + 1
    if cryptoMath.gcd(keyA, len(affineCipher.SYMBOLS)) == 1:
        print(keyA, affineCipher.encryptMessage(key, message))