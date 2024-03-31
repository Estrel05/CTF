from random import randint
import sys

cipher = [
    131553,
    993956,
    964722,
    1359381,
    43851,
    1169360,
    950105,
    321574,
    1081658,
    613914,
    0,
    1213211,
    306957,
    73085,
    993956,
    0,
    321574,
    1257062,
    14617,
    906254,
    350808,
    394659,
    87702,
    87702,
    248489,
    87702,
    380042,
    745467,
    467744,
    716233,
    380042,
    102319,
    175404,
    248489,
]


def generator(g, x, p):
    return pow(g, x) % p


def decrypt(ciphertext, key):
    plain = []
    for char in ciphertext:
        plain.append(chr(char // (key * 311)))
    return plain


def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True


def dynamic_xor_decrypt(ciphertext, text_key):
    plain_text = ""
    key_length = len(text_key)
    for i, char in enumerate(ciphertext):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        plain_text = decrypted_char + plain_text
    return plain_text


def test(cipher_text, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = 94
    b = 21
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    semi_plain = decrypt(cipher_text, shared_key)
    plain = dynamic_xor_decrypt(semi_plain, text_key)
    print(f"plain is: {plain}")


test(cipher, "trudeau")
