import sys
import os
from math import gcd

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
MODULO = len(ALPHABET)  # 27 znaków (A-Z + spacja)


# Znalezienie odwrotności modulo
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def caesar_cipher(text, shift):
    return "".join(ALPHABET[(ALPHABET.index(c) + shift) % MODULO] for c in text)


def caesar_decipher(text, shift):
    return "".join(ALPHABET[(ALPHABET.index(c) - shift) % MODULO] for c in text)


def affine_cipher(text, a, b):
    if gcd(a, MODULO) != 1:
        raise ValueError("Nieprawidłowy klucz: 'a' musi być względnie pierwsze z MODULO")
    return "".join(ALPHABET[(a * ALPHABET.index(c) + b) % MODULO] for c in text)


def affine_decipher(text, a, b):
    a_inv = mod_inverse(a, MODULO)
    if a_inv is None:
        raise ValueError("Brak multiplikatywnej odwrotności dla 'a'")
    return "".join(ALPHABET[(a_inv * (ALPHABET.index(c) - b)) % MODULO] for c in text)


def brute_force_affine(text):
    results = []
    for a in range(1, MODULO):
        if gcd(a, MODULO) == 1:  # 'a' musi być względnie pierwsze z MODULO
            for b in range(MODULO):
                try:
                    decrypted = affine_decipher(text, a, b)
                    results.append(f"a={a}, b={b}: {decrypted}")
                except ValueError:
                    continue
    return results


def known_plaintext_attack():
    with open("crypto.txt", "r") as f:
        crypto_text = f.read().strip()
    with open("extra.txt", "r") as f:
        known_text = f.read().strip()

    for a in range(1, MODULO):
        if gcd(a, MODULO) == 1:
            for b in range(MODULO):
                try:
                    decrypted = affine_decipher(crypto_text, a, b)
                    if decrypted.startswith(known_text):
                        with open("key-found.txt", "w") as kf:
                            kf.write(f"{a} {b}")
                        with open("decrypt.txt", "w") as df:
                            df.write(decrypted)
                        print("Klucz znaleziony i zapisany do key-found.txt")
                        return
                except ValueError:
                    continue
    print("Nie znaleziono klucza.")


def main():
    if len(sys.argv) < 3:
        print("Użycie: python cezar.py -c/-a -e/-d/-j/-k")
        sys.exit(1)

    mode = sys.argv[1]  # -c (Cezar) lub -a (Afiniczny)
    operation = sys.argv[2]  # -e (szyfrowanie), -d (deszyfrowanie), -j, -k

    if operation == "-k":
        with open("crypto.txt", "r") as f:
            crypto_text = f.read().strip()

        if mode == "-c":
            results = [f"Shift {i}: {caesar_decipher(crypto_text, i)}" for i in range(1, MODULO)]
        elif mode == "-a":
            results = brute_force_affine(crypto_text)
        else:
            print("Nieprawidłowy tryb szyfrowania.")
            sys.exit(1)

        with open("decrypt.txt", "w") as f:
            f.write("\n".join(results))
        print("Wyniki zapisane do decrypt.txt")
        sys.exit(0)

    if operation == "-j":
        known_plaintext_attack()
        sys.exit(0)

    # Wczytanie tekstu jawnego/kryptogramu
    if operation in ["-e", "-d"]:
        input_file = "plain.txt" if operation == "-e" else "crypto.txt"
        output_file = "crypto.txt" if operation == "-e" else "decrypt.txt"

        with open(input_file, "r") as f:
            text = f.read().strip()

        # Wczytanie klucza
        with open("key.txt", "r") as f:
            key_parts = list(map(int, f.read().strip().split()))

        if mode == "-c":
            shift = key_parts[0]
            result = caesar_cipher(text, shift) if operation == "-e" else caesar_decipher(text, shift)
        elif mode == "-a":
            a, b = key_parts
            result = affine_cipher(text, a, b) if operation == "-e" else affine_decipher(text, a, b)
        else:
            print("Nieprawidłowy tryb szyfrowania.")
            sys.exit(1)

        with open(output_file, "w") as f:
            f.write(result)
        print(f"Wynik zapisany do {output_file}")
    else:
        print("Nieobsługiwana operacja.")
        sys.exit(1)


if __name__ == "__main__":
    main()
