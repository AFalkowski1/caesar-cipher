# Caesar Cipher

This project is an implementation of the Caesar cipher algorithm in Python. The program allows for text encryption and decryption using a given key, as well as cryptanalysis, which is breaking the cipher without knowing the key, based on letter frequency analysis. It is an ideal project for learning basic cryptographic operations and text analysis.

---

## Key Features

* **Encryption:** Encrypts text from the `plain.txt` file using a key (shift) and saves the result to `crypto.txt`.
* **Decryption:** Decrypts text from the `crypto.txt` file using a key and saves the result to `decrypt.txt`.
* **Cryptanalysis:** Attempts to find the key and decrypt the text from the `crypto.txt` file without knowing the key. Breaking the cipher is based on letter frequency analysis, which is one of the simplest cryptanalysis methods. The found key is saved in `key-found.txt`, and the decrypted text in `decrypt.txt`.
* **Text Preparation:** Prepares plaintext by removing non-alphabetic characters and converting the text to lowercase, then saves it to `plain.txt`.

---

## Command Line Usage

The program is run with one of the following arguments:
* `-p`: Prepares the plaintext.
* `-e <key>`: Encrypts the text using the specified key (a number from 1 to 25).
* `-d <key>`: Decrypts the text using the specified key (a number from 1 to 25).
* `-k`: Cryptanalysis.

**Usage examples:**
`python caesar-cipher.py -e 3`
`python caesar-cipher.py -k`

---

## Files

* `orig.txt`: File with the original plaintext (used with the `-p` option).
* `plain.txt`: File with the prepared plaintext.
* `crypto.txt`: File with the encrypted text.
* `decrypt.txt`: File with the decrypted text.
* `key-found.txt`: File with the key found by cryptanalysis.
