import base64

encrypted = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6YzRNalV3YUcxcWZRPT0nCg=="


def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord("a"):
                    shifted += 26
            elif char.isupper():
                if shifted < ord("A"):
                    shifted += 26
            decrypted += chr(shifted)
        else:
            decrypted += char
    return decrypted


first_decoded = base64.b64decode(encrypted).decode("utf-8").strip("b")
second_decoded = base64.b64decode(first_decoded).decode("utf-8")
flag = caesar_decrypt(second_decoded, ord("w") - ord("p"))
print(flag)
