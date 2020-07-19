import random

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def encrypt(text, a, b):
    cipher = ""
    for character in text:
        n = ord(character)-97
        c = ((n*a+b)%26) + 97
        cipher = cipher + chr(c)

    return cipher

def decrypt(cipher, a, b):
    text = ""
    a = modinv(a,26)
    for character in cipher:
        n = ord(character)-97
        t = ((n-b)*a)%26 + 97
        text = text + chr(t)

    return text


if __name__ == "__main__":
    text = input("Enter the plain text : ")
    a = 17
    b = 25
    #a = random.randint(0,61)
    #b = random.randint(0,61)
        
    cipher_text = encrypt(text, a, b)
    print ( "cipher text : " + cipher_text )
    plain_text = decrypt(cipher_text, a, b)
    print ( "plain text  : " + plain_text )

